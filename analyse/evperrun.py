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

# ############################
# ##  argument parser       ##
# ############################
# parser = argparse.ArgumentParser()
# parser.add_argument("datatype", type=str, nargs='?',choices=['sim', 'data', 'blank'] ,help="type of data tag")
# args = parser.parse_args()
# datatype = args.datatype
iteration = 4
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks4']
fname = 'data'
first = True
dfex = pd.read_pickle('/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl')
dfall = pd.DataFrame(columns=dfex.columns)
#runs =  ['run30ks4']
dlllimit =  -30
entriesperrun = np.array([])
rate = np.array([])
e_rate = np.array([])
for r in runs:
    if iteration == 1:
        folder = constant.basefolder + constant.runname[r] + '/pkl/'
    if iteration == 2:
        folder = constant.basefolder2 + constant.runname[r] + '/pkl/'
    if iteration == 4:
        folder = constant.basefolder4 + constant.runname[r] + '/pkl/'
#    folder = '/Users/gaior/DAMIC/data/20180412/' + constant.runname[r] + '/pkl/'
    print 'name of file = ', folder + fname + '.pkl'
    df = pd.read_pickle(folder + fname + '.pkl')
    dfsel = df[(df.is_masked == 0) & 
               (df.touchmask == 0) & 
               #              (df.centery < 44 )  & 
               (df.success ==1)    & 
               #              (df.centery > 1.5)  & 
               (df.multirows == 0)    &
               (df.ll < 100)       &
               (df.RUNID!=2482) &  (df.RUNID!=2479) & (df.RUNID!=2577)& (df.RUNID!=2849) & (df.RUNID!=2902) & (df.RUNID!=2927) & (df.RUNID!=3003) & (df.RUNID!=3059) & (df.RUNID!=3112) &
               (df.sigma > 0.3) & (df.sigma < 0.8) &
               (df.ll - df.llc < dlllimit)
               ]
    entriesperrun = np.append(entriesperrun, dfsel.shape[0])
    rate = np.append(rate, float(dfsel.shape[0]) /( constant.runinfo[r][0]*constant.runinfo[r][1]) )
    e_rate = np.append(e_rate, np.sqrt(dfsel.shape[0])/ ( constant.runinfo[r][0]*constant.runinfo[r][1]))

plt.ylabel('rate [ev/second]')
plt.errorbar(runs,rate,yerr=e_rate,fmt='o')

plt.legend()
plt.show()
