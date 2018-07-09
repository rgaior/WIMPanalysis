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

produce = False
dllcut = -25
plotname = 'cut_' + str(dllcut)
fignr, arnr = plt.subplots(figsize=(8,6))     

for r in ['run30ks1','run100ks1','run100ks2']:
#for r in ['run100ks1']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    file = folder + '/pkl/' + 'simall.pkl'
    folderblank = folder[:folder.rfind('cluster_sim')] + '/blank/'
    print 'folder blank = ', folderblank
    fileblank = folderblank + '/pkl/simall.pkl'
    dfori = pd.read_pickle(file)
    df = dfori[dfori.simx == 0]
    dfblank = pd.read_pickle(fileblank)
    outfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
    if produce == True:
        dfcomm = pd.DataFrame(columns=df.columns)
        dffake = pd.DataFrame(columns=df.columns)
        blanksize = dfblank.shape[0]
        simsize = df.shape[0]
        for dsim in range(simsize):
            dsimtemp = df.iloc[dsim]
            com = False
            for d in range(blanksize):
                dtemp = dfblank.iloc[d]
                if (dsimtemp.centerx == dtemp.centerx) and (dsimtemp.centery == dtemp.centery):                
#                print 'dtemp.centerx = ' , dtemp.centerx , ' dsimtemp.centerx = ' , dsimtemp.centerx
#                print 'dtemp.centery = ' , dtemp.centery , ' dsimtemp.centery = ' , dsimtemp.centery
                    com = True
            if com == True:
                dfcomm = dfcomm.append(dsimtemp)                
            else:
                dffake = dffake.append(dsimtemp)                
#    df = dfori[dfori.simx == 0]
        dfcomm.to_pickle(outfolder  + 'common.pkl')
        dffake.to_pickle(outfolder  + 'fake.pkl')

    else:
        dfcomm = pd.read_pickle(outfolder  + 'common.pkl')
        dffake = pd.read_pickle(outfolder  + 'fake.pkl')


    dfcomm = dfcomm[(dfcomm.ll - dfcomm.llc < dllcut)]
    dffake= dffake[(dffake.ll - dffake.llc < dllcut)]
### nr of fake vs extension:
    a_nroffake = np.array([])
    a_nrofblank = np.array([])
    a_ext = np.array([])
    for ext in constant.extensionlist:
        dfcommtemp= dfcomm[dfcomm.EXTID==ext]
        dffaketemp= dffake[dffake.EXTID==ext]
#        dforitemp = dfori[dfori.EXTID==ext]
        a_nroffake = np.append(a_nroffake,dffaketemp.shape[0] )
        a_ext = np.append(a_ext,ext)
        a_nrofblank = np.append(a_nrofblank,float(dfcommtemp.shape[0]))
    arnr.plot(a_ext,a_nrofblank,'*',label='in blank of ' + r)
    arnr.plot(a_ext,a_nroffake,'o',label='not in blank of ' + r)
    #arnr.plot(a_ext,a_nroffake,'o',label=r)

### Energy of fake and energy of all:
    figE, arE = plt.subplots(figsize=(8,6))     
    figE.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(0,2,0.05)
    arE.hist(dfcomm.efit,bins=bins,histtype='step',lw=2,label='in blank',log=True)
    arE.hist(dffake.efit,bins=bins,histtype='step',lw=2,label='not in blank',log=True)
    arE.set_xlabel('energy [keV]')

### depth of fake and depth of all:
    figdLL, ardLL = plt.subplots(figsize=(8,6))     
    figdLL.suptitle(run,fontsize=15,fontweight='bold')
#    bins = np.arange(dllcut,0,5)
    min = np.min(np.array([np.min(dfcomm.ll - dfcomm.llc),np.min(dffake.ll - dffake.llc)]))
    max = np.max(np.array([np.max(dfcomm.ll - dfcomm.llc),np.max(dffake.ll - dffake.llc)]))
    if len(dfcomm.ll) == 0 or len(dffake.ll) == 0  :
        bins = np.arange(-1000,0,5)
    else:
        bins = np.arange(min, max,5)
#    ardLL.hist(dfori.ll - dfori.llc,bins=bins,histtype='step',lw=2,label='all',log=True)
    ardLL.hist(dfcomm.ll - dfcomm.llc,bins=bins,histtype='step',lw=2,label='in blank',log=True)
    ardLL.hist(dffake.ll - dffake.llc,bins=bins,histtype='step',lw=2,label='not in blank',log=True)
    ardLL.set_xlabel('ll - llc')

### depth of fake and depth of all:
    figSigma, arSigma = plt.subplots(figsize=(8,6))     
    figSigma.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(0,3,0.1)
#    arSigma.hist(dfori.ll - dfori.llc,bins=bins,histtype='step',lw=2,label='all',log=True)
    arSigma.hist(dfcomm.sigma,bins=bins,histtype='step',lw=2,label='in blank',log=True)
    arSigma.hist(dffake.sigma,bins=bins,histtype='step',lw=2,label='not in blank',log=True)
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
    arXY.plot(dffake.centerx, dffake.centery,'.')
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
    plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20180115/'
    figE.savefig(plotfolder + run + plotname +  '_E.png' )
    figdLL.savefig(plotfolder + run + plotname + '_LL.png' )
    figSigma.savefig(plotfolder + run + plotname + '_Sigma.png' )
    figXY.savefig(plotfolder + run + plotname + '_XY.png' )
arnr.annotate('DLL < ' +str(dllcut),xy=(0,1),xytext=(0,1), xycoords ='axes fraction', fontsize=20)
fignr.savefig(plotfolder + run + plotname + '_nr.png' )
    
plt.show()
