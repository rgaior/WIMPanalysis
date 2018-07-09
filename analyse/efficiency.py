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

def calerror(k,n):
    k = float(k)
    n = float(n)
#    er =  np.sqrt( ((k**2)*(n+k))/n**3 )
    if k == 0 or n == 0:
        er =0
    else:
        er =  (k/n)*np.sqrt((1/k) + (1/n))
    return er

# def calerror(k,n):
#    k = float(k)
#    n = float(n)
#    er = (1/n)*np.sqrt( k*(1-(k/n) ))
#    return er

runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
#datatype == 'sim'
fname = 'sim'

first = True
dfex = pd.read_pickle('/Users/gaior/DAMIC/data/official2/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/sim.pkl')
dfexs = pd.read_pickle('/Users/gaior/DAMIC/data/official2/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/sim_s.pkl')
dfall = pd.DataFrame(columns=dfex.columns)
dfsimall = pd.DataFrame(columns=dfexs.columns)
iteration = 2
version = 3
for r in runs:
    if iteration == 1:
        folder = constant.basefolder + constant.runname[r] + '/pkl/'
    if iteration == 2:
        folder = constant.basefolder2 + constant.runname[r] + '/pkl/'
#    folder = constant.basefolder + constant.runname[r] + '/pkl/'
#    df = pd.read_pickle(folder + fname + 'sel.pkl')
    df = pd.read_pickle(folder + fname + '.pkl')
    dfs = pd.read_pickle(folder + fname + '_s.pkl')
    dfall = dfall.append(df)
    dfsimall = dfsimall.append(dfs)
    print dfall.shape[0], ' ' , dfsimall.shape[0]

dfall = dfall[(dfall.is_masked == 0) &
              (dfall.touchmask == 0) &
              (dfall.centery < 44 )  &
              (dfall.sime != 0)      &  
              (dfall.simdisty > 2)   & 
              (dfall.simdist > 5)    & 
              (dfall.success ==1)    &  
              (dfall.ll < 100)       & 
#              (dfall.multir==0) &
              (dfall.RUNID!=2482)    & 
              (dfall.RUNID!=2479)    & 
              (dfall.RUNID!=2577)    & 
              (dfall.RUNID!=2849)    & 
              (dfall.RUNID!=2902)    & 
              (dfall.RUNID!=2927) ]

dfsimall  = dfsimall[(dfsimall.is_masked == 0)  & 
                     (dfsimall.simdist > 5)     & 
                     (dfsimall.simdisty > 2)    & 
                     (dfsimall.simy < 44 )      & 
                     (dfsimall.success==1)      & 
                     (dfsimall.sime != 0)       & 
#                     (dfsimall.ll < 100)       & 
                     (dfsimall.RUNID!=2482)     &
                     (dfsimall.RUNID!=2479)        & 
                     (dfsimall.RUNID!=2577)    & 
                     (dfsimall.RUNID!=2849)    & 
                     (dfsimall.RUNID!=2902)    & 
                     (dfsimall.RUNID!=2927) ]

#dfall = dfall[(dfall.multir==0) & (dfall.centery < 44 )]
totnrofevent = dfsimall.shape[0]
deltaE = 0.05 #kev
emax = 9 #kev
a_e1 = np.arange(0,emax,deltaE)
a_e2 = np.arange(deltaE,emax+deltaE,deltaE)
a_eff = np.array([])
a_eff_dll = np.array([])
a_eff_dll_sig = np.array([])
a_eff_er = np.array([])
a_eff_dll_er = np.array([])
a_eff_dll_sig_er = np.array([])
a_e = np.array([])

#dfall = dfall[dfall.ll - dfall.llc >-100]
#plt.hist(dfall.ll -dfall.llc,bins =100)
siglow =0.3
sigup =0.8
for emin,emax in zip(a_e1,a_e2):
#    print 'e,in = ' , emin, ' emax = ' , emax
#    print emin + (emax-emin)/2
    dfsimtemp = dfsimall[ (dfsimall.sime> emin) & ( dfsimall.sime < emax)]
    dftemp = dfall[ (dfall.sime> emin ) & ( dfall.sime < emax)]
    dftempdll = dfall[ (dfall.sime> emin ) & ( dfall.sime < emax) & (dfall.ll - dfall.llc < -20)]
    dftempdllsig = dfall[ (dfall.sime> emin ) & ( dfall.sime < emax) & (dfall.ll - dfall.llc < -20) & (dfall.sigma > siglow)& (dfall.sigma < sigup)]
    
    eff = float(dftemp.shape[0])/float(dfsimtemp.shape[0])
    eff_dll = float(dftempdll.shape[0])/float(dfsimtemp.shape[0])
    eff_dll_sig = float(dftempdllsig.shape[0])/float(dfsimtemp.shape[0])
    a_eff = np.append(a_eff, eff)
    a_eff_dll = np.append(a_eff_dll, eff_dll)
    a_eff_dll_sig = np.append(a_eff_dll_sig, eff_dll_sig)
    a_eff_er = np.append(a_eff_er,calerror(dftemp.shape[0],dfsimtemp.shape[0]))
    a_eff_dll_er = np.append(a_eff_dll_er,calerror(dftempdll.shape[0],dfsimtemp.shape[0]))
    a_eff_dll_sig_er = np.append(a_eff_dll_sig_er,calerror(dftempdllsig.shape[0],dfsimtemp.shape[0]))

    a_e = np.append(a_e,emin + (emax-emin)/2)
    print len(dftemp) , ' ' , len(dfsimtemp),  ' ' , eff
plt.errorbar(a_e,a_eff,yerr=a_eff_er,fmt='o')
plt.errorbar(a_e,a_eff_dll,yerr=a_eff_dll_er,fmt='o')
plt.errorbar(a_e,a_eff_dll_sig,yerr=a_eff_dll_sig_er,fmt='o')

outfolder = constant.outfolder
np.savez(outfolder + 'out1_' + str(version),e=a_e,eff=a_eff,err=a_eff_er)
np.savez(outfolder + 'out2_' + str(version),e=a_e,eff=a_eff_dll,err=a_eff_dll_er)
np.savez(outfolder + 'out3_' + str(version),e=a_e,eff=a_eff_dll_sig,err=a_eff_dll_sig_er)

plt.grid()
plt.show()
    
#     for 
# #     print 'totnrofevent = ' , totnrofevent
#     binsize = 0.05 #keV
#     deltaE = 9 # keV
#     bins = np.arange(0,1,binsize)
#     nrofeventperbin = totnrofevent/(deltaE/binsize)
#     print 'nrofeventperbin  = ' , nrofeventperbin
# #     weight = 1/(np.ones(len(df.ene1))*nrofeventperbin)
# #     print weight
# #     n, b,  patches  = areff.hist(df.efit,weights=weight, bins = bins,histtype='step',label=r,lw=2)
# #     n, b,  patches  = areff.hist(df.sime,weights=weight, bins = bins,histtype='step',label='sim E',lw=2)
# #     print 'n = ' , n
# #     print 'average eff = ' , np.sum(n)/len(n)
# # #    print arsimE._get_lines.prop_cycler
# # #    wid = b[1:] - b[:-1] 
# # #    areff.bar(b[:-1],n, width=wid,color=c,fill=False,label=r,lw=2,log=True) 
# # #    areff.step(b[:-1],n,label=r,lw=2) 
# # #    plt.show() 
# # #plt.yscale('log')
# #     areff.set_xlabel('energy [keV]')
# #     areff.set_ylabel('efficiency')
# #     areff.legend(loc=4)

# # sns.regplot(x=dfall, y=y, x_bins=bins, fit_reg=None)
    
