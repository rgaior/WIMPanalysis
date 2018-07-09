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
parser.add_argument("--dataset", type=str, nargs='*', help="runs")
args = parser.parse_args()
runs = args.run
datasets = args.dataset
if datasets == None:
    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    print 'specify the dataset to be produced'
    print 'exiting the code'
    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    sys.exit()
elif 'all' in datasets:
    datasets = ['simzero','split','misrec']
    
print 'the datasets: ' , datasets , ' will be produced ' 

for r in runs:
    print 'run: ', r
    folder = constant.usedfolder[r]
    processfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
    runname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    allfile = folder + '/pkl/' + 'simall.pkl'
    folderblank = folder[:folder.rfind('cluster_sim')] + '/blank/'
    print 'folder blank = ', folderblank
    fileblank = folderblank + '/pkl/simall.pkl'

    df = pd.read_pickle(allfile)
    dfblank = pd.read_pickle(fileblank)
    
    ##########################
    ## produce sim==0 file ##
    ##########################
    if 'simzero' in datasets:
        dfsime = df[df.sime==0]
        dfsime.to_pickle(processfolder + 'simzero.pkl')

    #########################
    ## produce split file  ##
    #########################
    if 'split' in datasets:
        files = glob.glob(folder + '/pkl/' + '*_0-*.pkl')
        dfsplit = pd.DataFrame(columns=df.columns)
        dfsplit2_2 = pd.DataFrame(columns=df.columns)
        for f in files:
            # reference dataframe
            dfref = pd.read_pickle(f)
            # loop over the DF
            allsize = dfref.shape[0]
            for iref in range(allsize):
                dftemp = dfref.iloc[iref]
                # loop over the remainder of the DF
                for iremainder in range(iref+1, allsize):
                    dfcomp = dfref.iloc[iremainder]
                    if ( (dftemp['EXTID'] == dfcomp['EXTID']) and (dftemp['RUNID'] == dfcomp['RUNID']) and ( np.abs(dftemp['centerx'] - dfcomp['centerx']) < 3) and ( np.abs(dftemp['centery'] - dfcomp['centery']) < 2) ):
                        dfsplit2_2 = dfsplit2_2.append(dftemp)
                        dfsplit2_2 = dfsplit2_2.append(dfcomp)
                        
        dfsplit2_2.to_pickle(processfolder + 'split2_2.pkl')
        
    ##############################
    ## produce misreconstructed ##
    ##############################
    if 'misrec' in datasets:
        dfmis = df[ (np.absolute((df.sime - df.efit)) > 0.13 ) & (df.sime!=0)]
        
        dfmis.to_pickle(processfolder + 'misrec.pkl')


    

