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

iteration = 4
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
#runsall = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks4']
runs = ['run30ks4']
dlllimit = -23
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
# get the format of the dataframe
dfall = utils.initialize_dataframe(exemplepath)
# merge the runs
dfall = utils.mergeruns(runs,folder,fname,dfall)
#define the cut related to the DLL 
dllcut = ' ll - llc < ' + str(dlllimit) 
dllcut2 = ' ll - llc  > ' +  '-1000'
fidcut = 'sigma > 0.3 & sigma < 0.8'
# perform 
dfsel = dfall.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut )
df = dfsel[['RUNID','EXTID','cid','ll','llc','ene1']]
print 'nr of events = ' , dfsel.shape[0] 
print df

