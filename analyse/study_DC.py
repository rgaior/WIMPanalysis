import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
import constant
import glob 
import argparse
from mpl_toolkits.axes_grid1 import make_axes_locatable

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("efficiency", type=str, nargs='?',choices=['y', 'n'] ,help="accounts for efficiency")
parser.add_argument("exposure", type=str, nargs='?',choices=['y', 'n'] ,help="accounts for exposure")
args = parser.parse_args()
efficiencynorm = args.efficiency
exposurenorm = args.exposure

savefig=True

iteration = 4
# define runs association:
runsall = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks3','run30ks4','run30ks5']
runMoriond = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
runafter = ['run30ks3','run30ks4','run30ks5']
run100ks1 = ['run100ks1']
run100ks2 = ['run100ks2']
run100ks3 = ['run100ks3']
run30ks1 = ['run30ks1']
run30ks2 = ['run30ks2']
run30ks3 = ['run30ks3']
run30ks4 = ['run30ks4']
run30ks5 = ['run30ks5']

# choose runs:
#names = ['runall']
#allruns = [runsall]
names = ['run1Moriond','runafter']
allruns = [runMoriond,runafter]

fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
##### common cuts
dlllimit = -30
dllcut = ' ll - llc < ' + str(dlllimit) 
fidcut = 'sigma > 0.3 & sigma < 0.8'
#fidcut = 'sigma > 0 & sigma < 1.5'
E1 = 0
s_E1 = str(E1).replace('.','_')
E2 = 10
deltaE = E2 - E1
Ecut = 'ene1 > '+str(E1)+' & ene1 < ' + str(E2) 
extcut = 'EXTID== 6'
plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20180619/'

DCfile = '/Users/gaior/DAMIC/data/DC/DC_vs_runID_2473_3576.pkl'
dfDC = pd.read_pickle(DCfile)
dclimvalue = 0.01
s_dclimvalue = str(dclimvalue).replace('.','_')

imcuts = utils.produceimagecut(dfDC,dclimvalue)

binsize = 0.05
bins = np.arange(E1,10,binsize)

efficiencyfile ='/Users/gaior/DAMIC/data/efficiency/extracted.pkl'
eff = pd.read_pickle(efficiencyfile)

extnr = len(constant.extensionlist)
a_rate = np.array([])
a_errrate = np.array([])

fspec, axspec = plt.subplots()
fsig, axsig = plt.subplots()
if efficiencynorm == 'y' and exposurenorm == 'y':
    addinfo = 'expo and efficiency'
if efficiencynorm == 'y' and exposurenorm == 'n':
    addinfo = 'efficiency only'
if efficiencynorm == 'n' and exposurenorm == 'y':
    addinfo = 'expo only'
if efficiencynorm == 'n' and exposurenorm == 'n':
    addinfo = 'raw'
fspec.suptitle(str(names)+ ' Emin = ' + str(E1) + ' DLL cut: ' +str(dlllimit) + ' DC cut: ' +str(dclimvalue) + addinfo)
first = True
for runs,n in zip(allruns,names):
    # get the format of the dataframe
    df = utils.initialize_dataframe(exemplepath)
    # merge the runs
    df = utils.mergeruns(runs,folder,fname,df)
    expo = 0
    for r in runs:
        expo += utils.getrunexposure(r,extnr)

        rmexpo = utils.removedexpofromDC(r,dfDC,dclimvalue)
#        print 'rmexpo = ' , rmexpo
        expo -= rmexpo
#    print 'expo =  ', expo
    dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut + '&' + Ecut )
    for imc in imcuts:
        dfsel = dfsel.query(imc)
        
    rate = float(len(dfsel))/expo
    errrate = np.sqrt(float(len(dfsel)))/expo
    a_rate = np.append(a_rate,rate)
    a_errrate = np.append(a_errrate,errrate)
    #    norm = (1./float(expo))*np.ones(len(dfsel.ene1))
    #    plt.hist(dfsel.ene1,bins=bins,weights=norm,histtype='step',label=n)



    #################################
    ### position plot ###############
    #################################
    print ' dfsel.shape[0] = ', dfsel.shape[0]
    print 'dccut = ' , dclimvalue
    print 'top : ' , dfsel[dfsel.centery > 21].shape[0]
    print 'bottom : ' , dfsel[dfsel.centery < 21].shape[0]
    
    if dfsel.shape[0] > 0:
        xlow = 4000
        xhigh = 9000
        ylow = 1
        yhigh = 44
        xbinning = 100
        ybinning = 1 
        xedges = np.arange(xlow,xhigh,xbinning)
        yedges = np.arange(ylow,yhigh,ybinning)
        x = dfsel.centerx
        y = dfsel.centery
        
        H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
        H = H.T
        
        
        fig, ax2dhist = plt.subplots(figsize=(10, 8))
        plt.suptitle(n)
        max = H.max()
        the2dhist= ax2dhist.imshow(H,  cmap='Blues',vmin=0, vmax=max,interpolation='nearest', origin='low', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], aspect='auto')
        
        # create new axes on the right and on the top of the current axes               
        # The first argument of the new_vertical(new_horizontal) method is              
        # the height (width) of the axes to be created in inches.                       
        divider = make_axes_locatable(ax2dhist)
        axHistx = divider.append_axes("top", 1.2, pad=0.1, sharex=ax2dhist)
        axHisty = divider.append_axes("right", 1.2, pad=0.1, sharey=ax2dhist)
        
    # make some labels invisible                                                                           
        axHistx.xaxis.set_tick_params(labelbottom=False)
        axHisty.yaxis.set_tick_params(labelleft=False)
        
    # now determine nice limits by hand:                                                                   
        binwidth = 1
        
        xbins = np.arange(xlow,xhigh,xbinning)
        ybins = np.arange(ylow,yhigh,ybinning)
        axHistx.hist(x, bins=xbins,histtype='step',lw=1,color='k')
        axHisty.hist(y, bins=ybins, histtype='step',lw=1,color='k', orientation='horizontal')
        
        
        ticks=np.linspace(0,max,max+1)
        fig.colorbar(the2dhist, ax=ax2dhist,ticks=ticks)
        ax2dhist.set_xlabel('X [re-binned per ' +str(xbinning) + ' pixels]' )
        ax2dhist.set_ylabel('Y [pixel]')
#########################################
###### position 
#########################################

    
#    norm = (1./float(expo))*np.ones(len(dfsel.ene1))
        norm = (1*np.ones(len(dfsel.ene1)))
#    print len(dfsel.ene1)
#    norm = ((1./binsize)/(float(expo/86400)*6e-3))*np.ones(len(dfsel.ene1))
    
        effnorm = np.interp(dfsel.ene1,eff.e,eff.eff)
#        print effnorm
#        norm = ((1./binsize)/(float(expo/86400)*6e-3))/effnorm
        if first == True:
            axspec.hist(dfsel.ene1,bins=bins,weights=norm,alpha=0.5,label=n)
        else:
            axspec.hist(dfsel.ene1,bins=bins,weights=norm,histtype='step',lw=2,label=n)
        first = False

# #plt.legend()
#     print 'run: ', n, 'exposure = ' , exp , ' nr of event = ' , dfsel.shape[0]
# plt.show()
        figext,  axext= plt.subplots()
        plt.suptitle(n)
        a_evperext = np.array([])
        for ext in constant.extensionlist:
            dftemp = dfsel.query('EXTID == '+ str(ext))
            a_evperext = np.append(a_evperext,dftemp.shape[0])
        axext.errorbar(constant.extensionlist,a_evperext,yerr=np.sqrt(a_evperext),fmt='o')
        axext.set_ylabel('# clusters')
        axext.set_xlabel('extension')

        figrunid,  axrunid = plt.subplots()
        plt.suptitle(n)
        plt.suptitle(n)
        runids = pd.unique(dfsel.RUNID)
        runids = np.array(runids.astype(int))
        a_evperrunid = np.array([])
        for rid in runids:
            dftemp = dfsel.query('RUNID == '+ str(rid))
            a_evperrunid = np.append(a_evperrunid,dftemp.shape[0])
#        axrunid.errorbar(runids,a_evperrunid,yerr=np.sqrt(a_evperrunid),fmt='o')
        axrunid.errorbar(np.arange(len(runids)),a_evperrunid,yerr=np.sqrt(a_evperrunid),fmt='o')
        plt.xticks(np.arange(len(runids))[::2], runids[::2],rotation='vertical',fontsize=10)
        axrunid.set_ylabel('# clusters')
        axrunid.set_xlabel('run id')
        if savefig == True:
           figrunid.savefig(plotfolder+ 'evVsRunid_'+n+ '_dll_'+str(dlllimit) + '_DClimit_'+str(s_dclimvalue))
           figext.savefig(plotfolder+ 'evVsExt_'+n+ '_dll_'+str(dlllimit) + '_DClimit_'+str(s_dclimvalue))
           fig.savefig(plotfolder+ 'position_'+n+ '_dll_'+str(dlllimit) + '_DClimit_'+str(s_dclimvalue))

        outfolder = '/Users/gaior/DAMIC/code/data_analysis/'
        outfile  = outfolder + n+ 'dll_'+ str(dlllimit) + '_DC_'+s_dclimvalue + '.txt'
        print outfile
        utils.writebrowsercommand(dfsel, outfile, runs[0], iteration)
#        for index,row in dfsel.iterrows():
#            print '-------------'
#            print row.qmax/(row.ene1*1000./3.77)


        sigbin = np.arange(0,1.5,0.05)
        axsig.hist(dfsel.sigma,bins=sigbin,histtype='step')



frate, ax = plt.subplots()
ax.errorbar(names, a_rate,yerr=a_errrate,fmt='o')
frate.savefig(plotfolder+ 'rates_dll_'+str(dlllimit) + '_DClimit_'+str(s_dclimvalue))
#ax.set_title('Simple plot')
axspec.legend()
plt.show()

