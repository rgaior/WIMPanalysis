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
########
##good && dll<-23 && ll_14<90 && centery>2 && centery<42 && qmax/(ene1*1000./3.77)>0.2
##
# ############################
# ##  argument parser       ##
# ############################
# parser = argparse.ArgumentParser()
# parser.add_argument("datatype", type=str, nargs='?',choices=['sim', 'data', 'blank'] ,help="type of data tag")
# args = parser.parse_args()
# datatype = args.datatype


iteration = 4
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
runsall = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks4']
#runs = ['run30ks4']
dlllimit = -30
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'

fidcut = 'sigma > 0.3 & sigma < 0.8'
dlllimits = [-23,-30,-40]
fmts = ['o','s','x']
for dlllimit,fmt in zip(dlllimits,fmts):
    dllcut = ' ll - llc < ' + str(dlllimit) 
    a_rate = np.array([])
    a_errrate = np.array([])
    for r in runsall:
        df = utils.initialize_dataframe(exemplepath)
        df = utils.mergeruns([r],folder,fname,df)
        listofid = pd.unique(df.RUNID)
        print ' run : ' ,r
        print ' nr of run == ' , len(listofid)
#define the cut related to the DLL 
# perform 
        dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut)
        rinfo = constant.runinfo[r]
#        exposure = rinfo[0]*rinfo[1]
        exposure = rinfo[0]*len(listofid)
        print 'exposure = ', exposure , ' s'
        evnr = dfsel.shape[0]
        print 'evnr = ' , evnr
        rate = evnr/exposure
        errrate = np.sqrt(evnr)/exposure
        a_rate = np.append(a_rate,rate)
        a_errrate = np.append(a_errrate,errrate)
    plt.errorbar(runsall,a_rate,a_errrate,fmt=fmt,label='DLL cut = ' +str(dlllimit))

plt.legend()
plt.show()
