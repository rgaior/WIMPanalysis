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
import seaborn as sns
import ROOT as R
produce = True
#produce = False
dllcut = -25
plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20180116/'
fignr, arnr = plt.subplots(figsize=(8,6))     
delX = 2
delY = 2
plotname = 'splitted_cut_' + str(dllcut) + 'dx_'+str(delX) + 'dy_'+str(delY) 
#for r in ['run30ks1','run100ks1','run100ks2']:
for r in ['run100ks1']:
#for r in ['run30ks1']:
#for r in ['run100ks2']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    folder = folder[:folder.rfind('cluster_sim')] 
    fakefile = folder + '/processed/' + 'fake.pkl'
    splittedfile = folder + '/processed/' + 'splitted_dx'+str(delX) + '_dy'+str(delY)+'.pkl'
    dffake= pd.read_pickle(fakefile)
    dfsplitted = pd.read_pickle(splittedfile)
    if produce == True:
        dfcomm = pd.DataFrame(columns=dffake.columns)
        dfrest = pd.DataFrame(columns=dffake.columns)
        fakesize = dffake.shape[0]
        splittedsize = dfsplitted.shape[0]
        for ifake in range(fakesize):
            dfaketemp = dffake.iloc[ifake]
            com = False
            for isplitted in range(splittedsize):
                dsplittedtemp = dfsplitted.iloc[isplitted]
                if ( (dsplittedtemp.RUNID == dfaketemp.RUNID) and (dsplittedtemp.EXTID == dfaketemp.EXTID) and dsplittedtemp.centerx == dfaketemp.centerx) and (dsplittedtemp.centery == dfaketemp.centery):                
                    print 'dsplittedtemp.ext' , dsplittedtemp.EXTID, 'dfaketemp.ext' , dfaketemp.EXTID
                    com = True
            if com == True:
                dfcomm = dfcomm.append(dfaketemp)                
            else:
                dfrest = dfrest.append(dfaketemp)                
#    df = dfori[dfori.simx == 0]
        dfcomm.to_pickle(folder + '/processed/' + 'comm_fake_splitted.pkl')
        dfrest.to_pickle(folder + '/processed/' + 'rest_fake_splitted.pkl')

    else:
        dfcomm = pd.read_pickle(folder  + '/processed/' + 'comm_fake_splitted.pkl')
        dfrest = pd.read_pickle(folder + '/processed/' + 'rest_fake_splitted.pkl')


    dfcomm = dfcomm[(dfcomm.ll - dfcomm.llc < dllcut)]
    dfrest= dfrest[(dfrest.ll - dfrest.llc < dllcut)]
    print 'len rest = ' , len(dfrest)
    count = 0 
    for index, row in dfrest.iterrows():        
#    for index, row in dfcomm.iterrows():        
#        if count == 50:
#            break
        count+=1
        fig = plt.figure()

        filesec = '100' if ('100000' in constant.usedfolder[r]) else '30'
        
#        filesec = '100' if ('10000' in  'skjdnf1000') else  '30'
        print 'filesec = ' , filesec
#sim30_0-1_012_12.root
        runid = row['RUNID']
        extid = row['EXTID']
        if r == 'run100ks2':
            ind = str(constant.runid[r].index(runid) + 1 + 9)
        else:
            ind = str(constant.runid[r].index(runid) + 1 )
        print 'runid = ' , runid
        print 'ind = ' , ind
        imfile = constant.usedfolder[r] + 'sim'+ filesec + '_0-1_' + str(ind.zfill(3)) + '_' + str(int(extid))  + '.root'

        f = R.TFile(imfile)
        im = f.Get("image")
        fig.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid))
        delta_x = 15
        delta_y = 4
        centralbin_x = int(row['centerx'])
        centralbin_y = int(row['centery'])
#        print 'centralbin_x = ',centralbin_x,'centralbin_y = ',centralbin_y
        image = utils.getimagepart(im,centralbin_x,centralbin_y,delta_x,delta_y)
#        print ' ' , np.min(image[0]), ' ' , np.max(image[0]), ' ' , np.min(image[1]), ' ', np.max(image[1])        
        plt.imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
        plt.xlabel("X [pixel]")
        plt.ylabel("Y [pixel]")
        plt.colorbar()
        fig.savefig(plotfolder + 'ev_r_'+r+'_run_'+str(runid) + '_ext_'+str(extid) + '_'+str(count)+ '.png')
# plt.show()



#    print dfcomm['sime']
#    print dfrest['sime']

### nr of fake vs extension:
    a_nroffake = np.array([])
    a_nrofblank = np.array([])
    a_ext = np.array([])
    for ext in constant.extensionlist:
        dfcommtemp= dfcomm[dfcomm.EXTID==ext]
        dfresttemp= dfrest[dfrest.EXTID==ext]
#        dforitemp = dfori[dfori.EXTID==ext]
        a_nroffake = np.append(a_nroffake,dfresttemp.shape[0] )
        a_ext = np.append(a_ext,ext)
        a_nrofblank = np.append(a_nrofblank,float(dfcommtemp.shape[0]))
    arnr.plot(a_ext,a_nrofblank,'*',label='splitted ' + r)
    arnr.plot(a_ext,a_nroffake,'o',label='non splitted of ' + r)
    #arnr.plot(a_ext,a_nroffake,'o',label=r)

### Energy of fake and energy of all:
    figE, arE = plt.subplots(figsize=(8,6))     
    figE.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(0,2,0.05)
    arE.hist(dfcomm.efit,bins=bins,histtype='step',lw=2,label='splitted',log=True)
    arE.hist(dfrest.efit,bins=bins,histtype='step',lw=2,label='non splitted',log=True)
    arE.set_xlabel('energy [keV]')

### depth of fake and depth of all:
    figdLL, ardLL = plt.subplots(figsize=(8,6))     
    figdLL.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(-1000,0,5)
#    ardLL.hist(dfori.ll - dfori.llc,bins=bins,histtype='step',lw=2,label='all',log=True)
    ardLL.hist(dfcomm.ll - dfcomm.llc,bins=bins,histtype='step',lw=2,label='splitted',log=True)
    ardLL.hist(dfrest.ll - dfrest.llc,bins=bins,histtype='step',lw=2,label='non splitted',log=True)
    ardLL.set_xlabel('ll - llc')

### depth of fake and depth of all:
    figSigma, arSigma = plt.subplots(figsize=(8,6))     
    figSigma.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(0,3,0.1)
#    arSigma.hist(dfori.ll - dfori.llc,bins=bins,histtype='step',lw=2,label='all',log=True)
    arSigma.hist(dfcomm.sigma,bins=bins,histtype='step',lw=2,label='splitted',log=True)
    arSigma.hist(dfrest.sigma,bins=bins,histtype='step',lw=2,label='non splitted',log=True)
    arSigma.set_xlabel('sigma')

# ### depth of fake and depth of all:
#     figLL_E, arLL_E = plt.subplots(figsize=(8,6))     
#     figLL_E.subplots_adjust(left=0.170)
#     figLL_E.suptitle(run,fontsize=15,fontweight='bold')
#     bins = np.arange(-50,0,1)
#     arLL_E.plot(dfori.efit, dfori.ll - dfori.llc,'.',label='all')
#     arLL_E.plot(df.efit, df.ll - df.llc, 'o', label='in blank')
#     arLL_E.set_xlabel('reconstructed E [keV]')
#     arLL_E.set_ylabel('ll - llc')

### depth of fake and depth of all:
    figXY, arXY = plt.subplots(figsize=(8,6))     
    figXY.suptitle(run,fontsize=15,fontweight='bold')
    arXY.plot(dfcomm.centerx, dfcomm.centery,'s')
    arXY.plot(dfrest.centerx, dfrest.centery,'.')
    arXY.set_xlabel('X')
    arXY.set_ylabel('Y')


    arnr.legend()
#    arLL_E.legend()
    arE.legend()

    ardLL.legend()
    arSigma.legend()
    arE.annotate('DLL < ' +str(dllcut),xy=(0,1),xytext=(0,1), xycoords ='axes fraction', fontsize=20)
    arXY.annotate('DLL < ' +str(dllcut),xy=(0,1),xytext=(0,1), xycoords ='axes fraction', fontsize=20)
    arSigma.annotate('DLL < ' +str(dllcut),xy=(0,1),xytext=(0,1), xycoords ='axes fraction', fontsize=20)
    ardLL.annotate('DLL < ' +str(dllcut),xy=(0,1),xytext=(0,1), xycoords ='axes fraction', fontsize=20)
    figE.savefig(plotfolder + run + plotname +  '_E.png' )
    figdLL.savefig(plotfolder + run + plotname + '_LL.png')
    figSigma.savefig(plotfolder + run + plotname + '_Sigma.png' )
    figXY.savefig(plotfolder + run + plotname + '_XY.png' )
arnr.annotate('DLL < ' +str(dllcut),xy=(0,1),xytext=(0,1), xycoords ='axes fraction', fontsize=20)
#fignr.savefig(plotfolder + run + plotname + '_nr.png' )
    
plt.show()
