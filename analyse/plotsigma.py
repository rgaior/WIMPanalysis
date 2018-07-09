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


# def onpick(event):ind = event.ind
# print ('index: %d\nobjective 1: %0.2f\nobjective 2: %0.2f\nobjective 3: %0.2f\nobjective 4: %0.2f\nobjective 5: %0.2f\nobjective 6: %0.2f' % (event.ind[0],data[ind,0],data[ind,1],data[ind,2],data[ind,3],data[ind,4],data[ind,5]))
# fig.canvas.mpl_connect('pick_event', onpick)
# plt.show



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
    dfgoodfile = folder + '/pkl/simgood.pkl'
    a = pd.read_pickle(dfgoodfile)
    b = a[ (a.success ==1) & (a.sime>0) & (a.ll -a.llc < -20) & (a.ene1/a.efit -1 < 2)  & (a.RUNID != 2482) & (a.ene1 < 9)]
#    b = a[ (a.success ==1) & (a.sime>0) & (a.ll -a.llc < -20) & (a.ene1/a.efit -1 < 2)  & (a.RUNID != 2482) & (a.ll <100) & (a.sigma_err < 1.5)]
#    b = a[ (a.success ==1) & (a.sime>0) & (a.ll -a.llc < -20) & (a.ene1/a.efit -1 < 2)  & (a.RUNID != 2482) & (a.ll <100) ]
#    c = b[b.ll > 100]
    fig,ax= plt.subplots()
    fig.suptitle(r,fontsize=15, fontweight='bold')
    fit = np.polyfit(b.simz,b.sigma, 1)
    pfit = np.poly1d(fit)
    recz = b.sigma - pfit(b.simz)

#    plt.hist(recz,bins=20,log=True)
#    plt.plot(recz,b.llg,'.')
    dfnew = b.copy()
#    print recz
    dfnew = dfnew.assign(recz=pd.Series(recz).values)
#    print dfnew.recz
    dfnew=dfnew[dfnew['simz'] < 0.02]
#    dfsel = dfnew[ (dfnew.ene1 < 0.1) & (dfnew.simz < 0.002) & (dfnew.sigma > 0.5) ]
#    dfsel = dfnew[ (dfnew.ene1 < 0.2) & (dfnew.ene1 > 0.1)  & (dfnew.sigma > 0.5) ]
#    dfsel = dfnew[ (dfnew.ene1 < 0.5) & (dfnew.ene1 > 0.1)  & ((dfnew.sigma -dfnew.simsigma)/dfnew.simsigma> 0.2) & (dfnew.simsigma > 0.01) ]
    dfsel = dfnew[ (dfnew.ene1 < 0.5) & (dfnew.ene1 > 0.1)  & (dfnew.sigma> 0.1) ]
    dfsel2 = dfnew[ (dfnew.ene1 < 0.2) & (dfnew.ene1 > 0.1)  & (dfnew.sigma < 0.1) ]
    for index, row in dfsel.iterrows():
        print constant.runidind[row['RUNID']], ' ' ,  row['EXTID'], ' ' , row['cid'], ' ' , row['ene1'], ' ', row['sigma'] , ' ' , row['simsigma']
    print ' the opther '
    for index, row in dfsel2.iterrows():
        print constant.runidind[row['RUNID']], ' ' ,  row['EXTID'], ' ' , row['cid'], ' ' , row['ene1'], ' ', row['sigma'] , ' ' , row['simsigma'] 

#, ' ', dfsel.simz

    
#    pl = ax.scatter(b.simsigma,b.sigma,c=b.simz)
#    plt.hist(b.sigma,bins=30,log=True)
#    pl = ax.scatter(dfnew.ene1,dfnew.simz,c=dfnew.npix,vmin=0,vmax=3)
    pl = ax.scatter(dfnew.simz,dfnew.sigma,c=dfnew.ene1,vmin=0,vmax=9)
#    pl = ax.plot(dfnew.simz,dfnew.sigma,'.')
#    ax.set_xlabel("simz")
#    ax.set_ylabel("sigma_err")
#     ax.legend()
    plt.colorbar(pl)


#plt.legend()
plt.show()
