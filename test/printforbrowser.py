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
args = parser.parse_args()
runs = args.run

for r in runs:
    print 'run: ', r
    folder = constant.usedfolder[r]
    processfolder = folder +  '/pkl2/'
    dfall = pd.read_pickle(processfolder  + "simgood.pkl")
    # conditio  LL > 200
    llcut = 100
    
    dfsel = dfall[ (dfall.ll > llcut) & (dfall.RUNID!=2482 ) & (dfall.ll -dfall.llc < -20) & (dfall.success==1)]
    for i in range(dfsel.shape[0]):
        dft = dfsel.iloc[i]
        runid = dft.RUNID
        extid = dft.EXTID
        
        for rname, ids in constant.runid.iteritems():
            if runid in ids:
                runname = rname
        if runname == 'run100ks2':
            ind = str(constant.runid[runname].index(runid) + 1 + 9)
        else:
            ind = str(constant.runid[runname].index(runid) + 1 )

        filesec = '100' if ('100000' in constant.usedfolder[runname]) else '30'
        if (dft.sime < 1):
            filename = 'sim'+ filesec + '_0-1_' + str(ind.zfill(3)) + '_' + str(int(extid))  + '.root'
        else:
            filename = 'sim'+ filesec + '_0-9_' + str(ind.zfill(3)) + '_' + str(int(extid))  + '.root'
        folder = constant.usedfolder[runname]
        file = folder + filename
        print file , ' ' , dft.cid ,' ', dft.centery , ' ' , dft.centerx 

#        runpathname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
#    fileelec = '/Users/gaior/DAMIC/data/processed/processed/'+runpathname + '/roots/'  + filename


 #       file = 
 #       print 'EventBrowser  ' ,
