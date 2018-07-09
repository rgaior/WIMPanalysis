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
from scipy.optimize import curve_fit
def f(x, height,mu,sigma): return height * np.exp(-(0.5*(x-mu)/sigma)**2)
from scipy import optimize




############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("--run", type=str, nargs='*',default=['run100ks1'], help="runs")
#parser.add_argument("--dataset", type=str, nargs='*', help="runs")
args = parser.parse_args()
runs = args.run
dummy = pd.read_pickle('/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run1/processed/rem_misrecblank.pkl')

dfall = pd.DataFrame(columns=dummy.columns)
dfallold = pd.DataFrame(columns=dummy.columns)
for r in runs:
    print 'run: ', r
    folder = constant.usedfolder[r]
    processfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
    runname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    df2 = pd.read_pickle(processfolder + 'rem_allsplit2_2.pkl')
    df3 = pd.read_pickle(processfolder + 'mariversion/rem_allsplit2_2.pkl')
    dfall = dfall.append(df2)
    dfallold = dfallold.append(df3)

dfall = dfall[ (dfall.ll - dfall.llc < -15) & (dfall.touchmask == 0) & (dfall.centerx - dfall.meanx < 2.5)  & (dfall.ll < 100) ]
dfallold = dfallold[ (dfallold.ll - dfallold.llc < -15) & (dfallold.touchmask == 0) & (dfallold.centerx - dfallold.meanx < 2.5)  & (dfallold.ll < 100)  ]

deltab = 0.01
bins = np.arange(-1,1,deltab)
nnew, binsnew, patches  =  plt.hist( (dfall.ene1 - dfall.sime)/dfall.sime, bins=bins, color='blue',histtype= 'step', lw=2, log=True,label='new')
nold, binsold, patches  =  plt.hist( (dfallold.ene1 - dfallold.sime)/dfallold.sime, bins=bins, color='red', histtype= 'step', lw=2, log=True,label='old')
xnew = binsnew + deltab/2
xold = binsold + deltab/2
poptnew, pcovnew = curve_fit(f, xnew[:-1], nnew)    
poptold, pcovold = curve_fit(f, xold[:-1], nold)    

[munew,sigmanew] = [poptnew[1],poptnew[2]]
[muold,sigmaold] = [poptold[1],poptold[2]]
plt.plot(xnew,f(xnew,poptnew[0],poptnew[1],poptnew[2]),'b')
plt.plot(xold,f(xold,poptold[0],poptold[1],poptold[2]),'r')
plt.ylim(0.1,1e4)
print ' rms = ' , np.std((dfall.ene1 - dfall.sime)/dfall.sime)
print ' rms = ' , np.std((dfallold.ene1 - dfallold.sime)/dfallold.sime)
plt.text(-1, 1000, r'$\mu = ' +str(np.round(munew,3))+',\ \sigma=' + str(np.abs(np.round(sigmanew,3))) +'$',color='b',fontsize=15,backgroundcolor='white')
plt.text(-1, 200, r'$\mu = ' +str(np.round(muold,3))+',\ \sigma=' + str(np.abs(np.round(sigmaold,3))) +'$',color='r',fontsize=15,backgroundcolor='white')
plt.legend()
plt.show()
