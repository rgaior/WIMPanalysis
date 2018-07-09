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
names = ['runall']
allruns = [runsall]
#names = ['run1Moriond','runafter']
#allruns = [runMoriond,runafter]

fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
##### common cuts
dlllimit = -23
dllcut = ' ll - llc < ' + str(dlllimit) 
fidcut = 'sigma > 0.3 & sigma < 0.8'
E1 = 0.05
s_E1 = str(E1).replace('.','_')
E2 = 10
deltaE = E2 - E1
Ecut = 'ene1 > '+str(E1)+' & ene1 < ' + str(E2) 
extcut = 'EXTID== 6'
plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20180619/'

DCfile = '/Users/gaior/DAMIC/data/DC/DC_vs_runID_2473_3576.pkl'
dfDC = pd.read_pickle(DCfile)
dclimvalue = 0.1
s_dclimvalue = str(dclimvalue).replace('.','_')

imcuts = utils.produceimagecut(dfDC,dclimvalue)

binsize = 0.05
bins = np.arange(E1,3,binsize)
binsize2 = 0.2
bins2 = np.arange(E1,10,binsize2)
binsize3 = 0.5
bins3 = np.arange(E1,10,binsize3)

efficiencyfile ='/Users/gaior/DAMIC/data/efficiency/extracted.pkl'
eff = pd.read_pickle(efficiencyfile)

extnr = len(constant.extensionlist)
a_rate = np.array([])
a_errrate = np.array([])

fspec, axspec = plt.subplots()
fspec2, axspec2 = plt.subplots()
fspec3, axspec3 = plt.subplots()
if efficiencynorm == 'y' and exposurenorm == 'y':
    addinfo = 'expo and efficiency'
if efficiencynorm == 'y' and exposurenorm == 'n':
    addinfo = 'efficiency only'
if efficiencynorm == 'n' and exposurenorm == 'y':
    addinfo = 'expo only'
if efficiencynorm == 'n' and exposurenorm == 'n':
    addinfo = 'raw'
fspec.suptitle(str(names)+ ' Emin = ' + str(E1) + ' DLL cut: ' +str(dlllimit) + ' DC cut: ' +str(dclimvalue) + addinfo)
fspec2.suptitle(str(names)+ ' Emin = ' + str(E1) + ' DLL cut: ' +str(dlllimit) + ' DC cut: ' +str(dclimvalue) + addinfo)
fspec3.suptitle(str(names)+ ' Emin = ' + str(E1) + ' DLL cut: ' +str(dlllimit) + ' DC cut: ' +str(dclimvalue) + addinfo)
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
#    print ' dfsel.shape[0] = ', dfsel.shape[0]
#    print 'dccut = ' , dclimvalue
#    print 'top : ' , dfsel[dfsel.centery > 21].shape[0]
#    print 'bottom : ' , dfsel[dfsel.centery < 21].shape[0]
    
    if dfsel.shape[0] > 0:

    
#    norm = (1./float(expo))*np.ones(len(dfsel.ene1))
#    norm = (1*np.ones(len(dfsel.ene1)))
#    print len(dfsel.ene1)
#    norm = ((1./binsize)/(float(expo/86400)*6e-3))*np.ones(len(dfsel.ene1))
    
        effnorm = np.interp(dfsel.ene1,eff.e,eff.eff)
        if efficiencynorm == 'y' and exposurenorm == 'y':
            norm = ((1./binsize)/(float(expo/86400)*6e-3))/effnorm
            norm2 = ((1./binsize2)/(float(expo/86400)*6e-3))/effnorm
            norm3 = ((1./binsize3)/(float(expo/86400)*6e-3))/effnorm
        if efficiencynorm == 'y' and exposurenorm == 'n':
            norm = (1./binsize)/(1)/effnorm
            norm2 = (1./binsize2)/(1)/effnorm
            norm3 = (1./binsize3)/(1)/effnorm
        if efficiencynorm == 'n' and exposurenorm == 'y':
            norm = (1*np.ones(len(dfsel.ene1)))*((1./binsize)/(float(expo/86400)*6e-3))
            norm2 = (1*np.ones(len(dfsel.ene1)))*((1./binsize2)/(float(expo/86400)*6e-3))
            norm3 = (1*np.ones(len(dfsel.ene1)))*((1./binsize3)/(float(expo/86400)*6e-3))
        if efficiencynorm == 'n' and exposurenorm == 'n':
            norm = (1*np.ones(len(dfsel.ene1)))
            norm2 = (1*np.ones(len(dfsel.ene1)))
            norm3 = (1*np.ones(len(dfsel.ene1)))



 
        if first == True:
            n1,b1,p1 = axspec.hist(dfsel.ene1,bins=bins,weights=norm,color='b',alpha=0.5,label=n)
            errors = utils.gethisterror(dfsel.ene1,norm,bins)
            width = 0.9 * (bins[1] - bins[0])
            center = (bins[:-1] + bins[1:]) / 2        
            
            n2,b2,p2 = axspec2.hist(dfsel.ene1,bins=bins2,weights=norm2,color='b',alpha=0.5,label=n)
            errors2 = utils.gethisterror(dfsel.ene1,norm2,bins2)
            width2 = 0.9 * (bins2[1] - bins2[0])
            center2 = (bins2[:-1] + bins2[1:]) / 2        
            
            n3,b3,p3 = axspec3.hist(dfsel.ene1,bins=bins3,weights=norm3,color='b',alpha=0.5,label=n)
            errors3 = utils.gethisterror(dfsel.ene1,norm3,bins3)
            width3 = 0.9 * (bins3[1] - bins3[0])
            center3 = (bins3[:-1] + bins3[1:]) / 2       
            axspec.errorbar(center, n1, yerr=errors,fmt='.',color='b')
            axspec2.errorbar(center2, n2, yerr=errors2,fmt='.',color='b')
            axspec3.errorbar(center3, n3, yerr=errors3,fmt='.',color='b')
            #        n1,b1 = np.histogram(dfsel.ene1,bins=bins,weights=norm)
            #        print 'n =  ', n , ' n1 = ' , n1
            
            first = False
        else:
            n1,b1,p1 = axspec.hist(dfsel.ene1,bins=bins,weights=norm,color='r',histtype='step',lw=1,label=n)
            errors = utils.gethisterror(dfsel.ene1,norm,bins)
            width = 0.9 * (bins[1] - bins[0])
            center = (bins[:-1] + bins[1:]) / 2        
            
            n2,b2,p2 = axspec2.hist(dfsel.ene1,bins=bins2,weights=norm2,color='r',histtype='step',lw=1,label=n)
            errors2 = utils.gethisterror(dfsel.ene1,norm2,bins2)
            width2 = 0.9 * (bins2[1] - bins2[0])
            center2 = (bins2[:-1] + bins2[1:]) / 2        
            
            n3,b3,p3 = axspec3.hist(dfsel.ene1,bins=bins3,weights=norm3,color='r',histtype='step',lw=1,label=n)
            errors3 = utils.gethisterror(dfsel.ene1,norm3,bins3)
            width3 = 0.9 * (bins3[1] - bins3[0])
            center3 = (bins3[:-1] + bins3[1:]) / 2       
            axspec.errorbar(center+0.1*width, n1, yerr=errors,fmt='.',color='r')
            axspec2.errorbar(center2+0.1*width2, n2, yerr=errors2,fmt='.',color='r')
            axspec3.errorbar(center3+0.1*width3, n3, yerr=errors3,fmt='.',color='r')

        axspec.set_xlabel('energy [keV]')
        axspec2.set_xlabel('energy [keV]')
        axspec3.set_xlabel('energy [keV]')
        if efficiencynorm == 'y' and exposurenorm == 'y':
            axspec.set_ylabel('event rate [d.r.u.]')
            axspec2.set_ylabel('event rate [d.r.u.]')
            axspec3.set_ylabel('event rate [d.r.u.]')
        else:
            axspec.set_ylabel('event')
            axspec2.set_ylabel('event')
            axspec3.set_ylabel('event')
            
        axspec.legend()
        axspec2.legend()
        axspec3.legend()

            
        if savefig == True:
            fspec.savefig(plotfolder+ 'spec_'+n+ 'Estart_'+str(s_E1)+ '_dll_'+str(dlllimit) + '_DClimit_'+str(s_dclimvalue) + '_eff_'+efficiencynorm + '_expo_'+exposurenorm)
            fspec2.savefig(plotfolder+ 'spec2_'+n+ 'Estart_'+str(s_E1)+ '_dll_'+str(dlllimit) + '_DClimit_'+str(s_dclimvalue) + '_eff_'+efficiencynorm + '_expo_'+exposurenorm)
            fspec3.savefig(plotfolder+ 'spec3_'+n+ 'Estart_'+str(s_E1)+ '_dll_'+str(dlllimit) + '_DClimit_'+str(s_dclimvalue) + '_eff_'+efficiencynorm + '_expo_'+exposurenorm)
                
#plt.show()
