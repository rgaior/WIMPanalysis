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


############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("--run", type=str, nargs='*',default=['run100ks1'], help="runs")
#parser.add_argument("--dataset", type=str, nargs='*', help="runs")
args = parser.parse_args()
runs = args.run
#datasets = args.dataset
# if datasets == None:
#     print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
#     print 'specify the dataset to be produced'
#     print 'exiting the code'
#     print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
#     sys.exit()
# else:
#     print 'the datasets: ' , datasets , ' will be produced ' 

for r in runs:
    print 'run: ', r
    folder = constant.usedfolder[r]
    processfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
    runname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    all = pd.read_pickle(processfolder + 'rem_allsplit2_2.pkl')
    simzero = pd.read_pickle(processfolder + 'rem_rem_sim0blanksplit2_2.pkl')
    misrec = pd.read_pickle(processfolder + 'rem_misrecsplit2_2.pkl')
    
