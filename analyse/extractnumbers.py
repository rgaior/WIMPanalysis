import ROOT as R
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
import constant
import argparse

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("--run", type=str, nargs='*',default=['run100ks1'], help="runs")
args = parser.parse_args()
runs = args.run
print runs
centercut = 2.5
dllcut = -15
llcut = 100
for run in runs:
    folder = constant.usedfolder[run]
    processfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
    runname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    allfile = folder + '/pkl/' + 'simall.pkl'
    folderblank = folder[:folder.rfind('cluster_sim')] + '/blank/'
    dfall = pd.read_pickle(allfile)
    print '------------------------------------------------- '
    print '---------------------', run  ,' ------------------------'
    print '-------------------------------------------------'
    print 'all, all events: ', dfall.shape[0]
    dfrem_allblank = pd.read_pickle(processfolder + 'rem_allblank.pkl')
    print 'all, blank cut: ', dfrem_allblank.shape[0]
    dfrem_allsplit2_2 = pd.read_pickle(processfolder + 'rem_allsplit2_2.pkl')
    dfrem_allsplit4_2 = pd.read_pickle(processfolder + 'rem_allsplit4_2.pkl')
    dfrem_allsplit10_2 = pd.read_pickle(processfolder + 'rem_allsplit10_2.pkl')
    print 'all, blank cut, split 2/2: ', dfrem_allsplit2_2.shape[0]
    print 'all, blank cut, split 4/2: ', dfrem_allsplit4_2.shape[0]
    print 'all, blank cut, split 10/2: ', dfrem_allsplit10_2.shape[0]
    print 'all, blank cut, split 2/2 and dLL < dllcut: ', dfrem_allsplit2_2[dfrem_allsplit2_2.ll - dfrem_allsplit2_2.llc <dllcut].shape[0]
    print 'all, blank cut, split 2/2 and dLL < dllcut and center -mean < 2.5: ', dfrem_allsplit2_2[ (dfrem_allsplit2_2.centerx- dfrem_allsplit2_2.meanx <centercut) & (dfrem_allsplit2_2.ll - dfrem_allsplit2_2.llc <dllcut) & (dfrem_allsplit2_2.touchmask==0) ].shape[0]
    print 'all, blank cut, split 2/2 and dLL < dllcut and center -mean < 2.5 and ll < 100: ', dfrem_allsplit2_2[ (dfrem_allsplit2_2.centerx- dfrem_allsplit2_2.meanx <centercut) & (dfrem_allsplit2_2.ll - dfrem_allsplit2_2.llc <dllcut) & (dfrem_allsplit2_2.ll  < llcut) & (dfrem_allsplit2_2.touchmask==0) ].shape[0]
    
    dfsimzero =  pd.read_pickle(processfolder + 'simzero.pkl')
    print 'sim == 0, all events: ', dfsimzero.shape[0]
    dfrem_sim0blank = pd.read_pickle(processfolder + 'rem_sim0blank.pkl')
    print 'sim0, blank cut: ', dfrem_sim0blank.shape[0]
    dfrem_rem_sim0blanksplit2_2 = pd.read_pickle(processfolder + 'rem_rem_sim0blanksplit2_2.pkl')
    dfrem_rem_sim0blanksplit4_2 = pd.read_pickle(processfolder + 'rem_rem_sim0blanksplit4_2.pkl')
    dfrem_rem_sim0blanksplit10_2 = pd.read_pickle(processfolder + 'rem_rem_sim0blanksplit10_2.pkl')
    print 'sim0, blank cut, split 2/2: ', dfrem_rem_sim0blanksplit2_2.shape[0]
    print 'sim0, blank cut, split 4/2: ', dfrem_rem_sim0blanksplit4_2.shape[0]
    print 'sim0, blank cut, split 10/2: ', dfrem_rem_sim0blanksplit10_2.shape[0]
    print 'sim0, blank cut, split 2/2 and dLL < dllcut: ', dfrem_rem_sim0blanksplit2_2[dfrem_rem_sim0blanksplit2_2.ll - dfrem_rem_sim0blanksplit2_2.llc <dllcut].shape[0]
    print 'sim0, blank cut, split 2/2 and dLL < dllcut and center -mean < 2.5: ', dfrem_rem_sim0blanksplit2_2[(dfrem_rem_sim0blanksplit2_2.ll - dfrem_rem_sim0blanksplit2_2.llc <dllcut) & ( dfrem_rem_sim0blanksplit2_2.centerx - dfrem_rem_sim0blanksplit2_2.meanx <centercut) & ( dfrem_rem_sim0blanksplit2_2.ll < llcut) & ( dfrem_rem_sim0blanksplit2_2.touchmask==0)].shape[0]
    print 'sim0, blank cut, split 2/2 and dLL < dllcut and center -mean < 2.5 and LL < 100: ', dfrem_rem_sim0blanksplit2_2[(dfrem_rem_sim0blanksplit2_2.ll - dfrem_rem_sim0blanksplit2_2.llc <dllcut) & ( dfrem_rem_sim0blanksplit2_2.centerx - dfrem_rem_sim0blanksplit2_2.meanx <centercut) & ( dfrem_rem_sim0blanksplit2_2.touchmask==0)].shape[0]
    
    dfmisrec =  pd.read_pickle(processfolder + 'misrec.pkl')
    print 'misreconstructed, all events: ', dfmisrec.shape[0]
    dfrem_misrecblank = pd.read_pickle(processfolder + 'rem_misrecblank.pkl')
    print 'misreconstructed, blank cut: ', dfrem_misrecblank.shape[0]
    dfrem_misrecblanksplit2_2 = pd.read_pickle(processfolder + 'rem_misrecsplit2_2.pkl')
    dfrem_misrecblanksplit4_2 = pd.read_pickle(processfolder + 'rem_misrecsplit2_2.pkl')
    dfrem_misrecblanksplit10_2 = pd.read_pickle(processfolder + 'rem_misrecsplit2_2.pkl')
    print 'misrec, blank cut, split 2/2: ', dfrem_misrecblanksplit2_2.shape[0]
    print 'misrec, blank cut, split 4/2: ', dfrem_misrecblanksplit4_2.shape[0]
    print 'misrec, blank cut, split 10/2: ', dfrem_misrecblanksplit10_2.shape[0]
    print 'misrec, blank cut, split 2/2 and dLL < dllcut: ', dfrem_misrecblanksplit2_2[ dfrem_misrecblanksplit2_2.ll - dfrem_misrecblanksplit2_2.llc <dllcut].shape[0]
    print 'misrec, blank cut, split 2/2 and dLL < dllcut and center -mean < 2.5: ', dfrem_misrecblanksplit2_2[ (dfrem_misrecblanksplit2_2.ll - dfrem_misrecblanksplit2_2.llc <dllcut) &  (dfrem_misrecblanksplit2_2.centerx - dfrem_misrecblanksplit2_2.meanx <centercut) & (dfrem_misrecblanksplit2_2.touchmask==0)].shape[0]
    print 'misrec, blank cut, split 2/2 and dLL < dllcut and center -mean < 2.5 and LL < 100: ', dfrem_misrecblanksplit2_2[ (dfrem_misrecblanksplit2_2.ll - dfrem_misrecblanksplit2_2.llc <dllcut) &  (dfrem_misrecblanksplit2_2.centerx - dfrem_misrecblanksplit2_2.meanx <centercut)&  (dfrem_misrecblanksplit2_2.ll < llcut) &  (dfrem_misrecblanksplit2_2.touchmask==0)].shape[0]




