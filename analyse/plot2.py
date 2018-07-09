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
def f(x, height,mu,sigma): return height * np.exp(-((x-mu)/sigma)**2)
from scipy import optimize


############################
##  argument parser       ##
############################
#parser = argparse.ArgumentParser()

# parser.add_argument("folder", type=str, nargs='?',default='/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run2/cluster_sim/', help="root file folder")
# args = parser.parse_args()

# folder = args.folder
# run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
# print 'rune = ', run
# file1 = folder + '/pkl/' + 'simall.pkl'
# file2 = '/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run2/old/' + 'rem_misrecsplit2_2.pkl'


# df1 = pd.read_pickle(file1) 
# df2 = pd.read_pickle(file2) 
# bins = np.arange(0,250,5)
# plt.hist(df1.ll, bins=bins, histtype= 'step', lw=3, log=True,label='all clusters')
# plt.hist(df2.ll, bins=bins, histtype= 'step', lw=2, log=True,label='misrec & not split')
# plt.xlabel('LL')
# plt.legend()
# plt.show()




# ############################
# ##  argument parser       ##
# ############################
# parser = argparse.ArgumentParser()
# parser.add_argument("--run", type=str, nargs='*',default=['run100ks1'], help="runs")
# #parser.add_argument("--dataset", type=str, nargs='*', help="runs")
# args = parser.parse_args()
# runs = args.run
# for r in runs:
#     print 'run: ', r
#     folder = constant.usedfolder[r]
#     processfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
#     runname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
#     df1 = pd.read_pickle(processfolder + 'rem_allsplit2_2.pkl')
# #    df2 = pd.read_pickle(processfolder + 'pbclusters2_2.pkl')
#     df2 = pd.read_pickle(processfolder + 'rem_rem_sim0blanksplit2_2.pkl')
#     df3 = pd.read_pickle(processfolder + 'rem_misrecsplit2_2.pkl')
#     df2 = df2[df2.ll - df2.llc < -15]
#     df3 = df3[df3.ll - df3.llc < -15]
#     df3 = df3[df3.touchmask == 0]
#     df2 = df2[df2.touchmask == 0]
#     df3 = df3[df3.centerx - df3.meanx < 2.5]
#     df2 = df2[df2.centerx - df2.meanx < 2.5]

# #    df2 = df2[df2.ll < 50]
# #    df3 = df3[df3.ll < 50]
    
# #     bins = np.arange(-4,4,0.1)
# #     plt.hist(df1.centerx - df1.meanx, bins=bins, histtype= 'step', lw=3, log=True,label='all clusters (not split and not blank)')
# #     plt.hist(df2.centerx - df2.meanx, bins=bins, histtype= 'step', lw=3, log=True,label='sim=0 (not split and not blank)')
# #     plt.hist(df3.centerx - df3.meanx, bins=bins, histtype= 'step', lw=3, log=True,label='misrec (not split and not blank)')
    
#     print '=================df3 = ' , df3.shape[0]

#     bins = np.arange(0,300,5)
#     plt.hist(df1.ll, bins=bins, histtype= 'step', lw=2, log=True,label='all clusters (not split and not blank)')
#     plt.hist(df3.ll, bins=bins, histtype= 'step', lw=2, log=True,label='misrec (not split and not blank)')


# plt.legend()
# plt.show()

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("--run", type=str, nargs='*',default=['run100ks1'], help="runs")
#parser.add_argument("--dataset", type=str, nargs='*', help="runs")
args = parser.parse_args()
runs = args.run

for r in runs:
    print 'run: ', r
    folder = constant.usedfolder[r]
    runname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    a = pd.read_pickle(folder + '/pkl/simgood.pkl')
    a = a[ (a.sime>0) & (a.success==1) & (a.touchmask==0) & (a.RUNID!=2482)  & (a.ll-a.llc<-20) & (a.multir==0) ]
    b = a[ (a.sime>0) & (a.success==1) & (a.touchmask==0) & (a.RUNID!=2482)  & (a.ll-a.llc<-20) & (a.multir==0) & (a.ll> 100) ]
    bins = np.arange(0,4000,1)
    print bins
    plt.hist(a.simdist,bins=bins,log=True,label='all')
    plt.hist(b.simdist,bins=bins,log=True,label=' LL > 100 ')
    
plt.xlabel('X distance from another simulated cluster [pixel]')
plt.ylabel('entries')
plt.xscale("log")
plt.legend()
plt.show()
