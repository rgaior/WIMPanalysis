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


fignr, arnr = plt.subplots(figsize=(8,6))     

#for r in ['run100ks1','run100ks2','run30ks1']:
for r in ['run100ks1']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    file = folder + '/pkl/' + 'simall.pkl'
    dfori = pd.read_pickle(file)
#    df = dfori[dfori.simx == 0]
 #   df = dfori[dfori.simx == 0 & ((dfori.ll - dfori.llc) < -200) ]
    df = dfori[((dfori.ll - dfori.llc) < -200) & (dfori.simx == 0)]
    
    print df    
### nr of fake vs extension:
    a_nroffake = np.array([])
    a_ext = np.array([])
    for ext in constant.extensionlist:
        dftemp= df[df.EXTID==ext]
        dforitemp = dfori[dfori.EXTID==ext]
        a_nroffake = np.append(a_nroffake, float(dftemp.shape[0])/dforitemp.shape[0])
        a_ext = np.append(a_ext,ext)
    arnr.plot(a_ext,a_nroffake,'o',label=r)

### Energy of fake and energy of all:
    figE, arE = plt.subplots(figsize=(8,6))     
    figE.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(0,2,0.05)
    arE.hist(dfori.efit,bins=bins,histtype='step',lw=2,label='all',log=True)
    arE.hist(df.efit,bins=bins,histtype='step',lw=2,label='non simulated cluster',log=True)
    arE.set_xlabel('energy [keV]')

### depth of fake and depth of all:
    figSigma, arSigma = plt.subplots(figsize=(8,6))     
    figSigma.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(-500,0,5)
    arSigma.hist(dfori.ll - dfori.llc,bins=bins,histtype='step',lw=2,label='all',log=True)
    arSigma.hist(df.ll - df.llc,bins=bins,histtype='step',lw=2,label='non simulated cluster',log=True)
    arSigma.set_xlabel('ll - llc')

### depth of fake and depth of all:
    figLL_E, arLL_E = plt.subplots(figsize=(8,6))     
    figLL_E.subplots_adjust(left=0.170)
    figLL_E.suptitle(run,fontsize=15,fontweight='bold')
    bins = np.arange(-50,0,1)
    arLL_E.plot(dfori.efit, dfori.ll - dfori.llc,'.',label='all')
    arLL_E.plot(df.efit, df.ll - df.llc, 'o', label='non simulated cluster')
    arLL_E.set_xlabel('reconstructed E [keV]')
    arLL_E.set_ylabel('ll - llc')

### depth of fake and depth of all:
    figXY, arXY = plt.subplots(figsize=(8,6))     
    figXY.suptitle(run,fontsize=15,fontweight='bold')
    arXY.plot(df.centerx, df.centery,'s')
    arXY.set_xlabel('X')
    arXY.set_ylabel('Y')


    arnr.legend()
    arLL_E.legend()
    arE.legend()

    arSigma.legend()

#     plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20171219/'
#     fignr.savefig(plotfolder + '/CheckFalse' + run + '_nr.png' )
#     figE.savefig(plotfolder + '/CheckFalse' +run + '_E.png' )
#     figSigma.savefig(plotfolder + '/CheckFalse' + run + '_LL.png' )
#     figXY.savefig(plotfolder + '/CheckFalse' + run + '_XY.png' )
#     figLL_E.savefig(plotfolder + '/CheckFalse' + run + '_LLE.png' )
    
plt.show()
