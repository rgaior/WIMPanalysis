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
    allfile = folder + '/pkl/' + 'simall.pkl'
    folderblank = folder[:folder.rfind('cluster_sim')] + '/blank/'
    fileblank = folderblank + '/pkl/simall.pkl'
    dfall = pd.read_pickle(allfile)
    dfblank = pd.read_pickle(fileblank)
    dfsimzero = pd.read_pickle(processfolder + 'simzero.pkl')
    dfsplit2_2 = pd.read_pickle(processfolder + 'split2_2.pkl')
    dfmisrec =pd.read_pickle(processfolder + 'misrec.pkl')



#     ###############################
#     ## produce blank and simzero ##
#     ###############################
    print 'len(dfsimzero) ', len(dfsimzero) 
    [dfsim0blank, dfrem_sim0blank] = utils.compareDF(dfsimzero, dfblank, constant.runid[r])
    print 'len(dfblankandsimzero) = ', len(dfsim0blank), ' len(dfrem_blanksimzero) = ', len(dfrem_sim0blank)
    dfrem_sim0blank.to_pickle(processfolder + 'rem_sim0blank.pkl')
    dfsim0blank.to_pickle(processfolder + 'sim0blank.pkl')
    
#     ##########################################
#     ## produce simzerononblank and splitted ##
#     ##########################################
    [dfrem_sim0blanksplit2_2, dfrem_rem_sim0blanksplit2_2] = utils.compareDF(dfrem_sim0blank,dfsplit2_2, constant.runid[r])
    print 'size of simzeronon blank and split2_2 ',  len(dfrem_sim0blanksplit2_2), ' remainder = ' , len(dfrem_rem_sim0blanksplit2_2)
    print 'cut at -15 : ', len(dfrem_rem_sim0blanksplit2_2[dfrem_rem_sim0blanksplit2_2.ll - dfrem_rem_sim0blanksplit2_2.llc < -15])
    dfrem_rem_sim0blanksplit2_2.to_pickle(processfolder + 'rem_rem_sim0blanksplit2_2.pkl')


    dfrem_rem_sim0blanksplit2_2c  = pd.DataFrame(columns=dfall.columns)

    dfrem_rem_sim0blanksplit2_2c = dfrem_rem_sim0blanksplit2_2[dfrem_rem_sim0blanksplit2_2.ll - dfrem_rem_sim0blanksplit2_2.llc < -15]

    dfrem_rem_sim0blanksplit2_2c.to_pickle(processfolder + 'rem_rem_sim0blanksplit2_2c.pkl')

    ############################
    ## check the cut in split ##
    ############################
    print 'len(dfall) = ' , len(dfall)
    [dfallblank,dfrem_allblank] = utils.compareDF(dfall, dfblank,constant.runid[r])
    dfallblank.to_pickle(processfolder + 'allblank.pkl')
    dfrem_allblank.to_pickle(processfolder + 'rem_allblank.pkl')
    print 'len(dfallblank) = ' , len(dfallblank), 'len(dfrem_allblank) = ' , len(dfrem_allblank)
    [dfallsplit2_2,dfrem_allsplit2_2] = utils.compareDF(dfrem_allblank, dfsplit2_2,constant.runid[r])
    print ' len(dfrem_allsplit2_2) = ', len(dfrem_allsplit2_2) 
    dfallsplit2_2.to_pickle(processfolder + 'allsplit2_2.pkl')
    dfrem_allsplit2_2.to_pickle(processfolder + 'rem_allsplit2_2.pkl')


    ################################
    ## check the misrec and split ##
    ################################
    print 'len(dfmisrec) = ' , len(dfmisrec)
    [dfmisrecblank,dfrem_misrecblank] = utils.compareDF(dfmisrec, dfblank,constant.runid[r])
    dfmisrecblank.to_pickle(processfolder + 'misrecblank.pkl')
    dfrem_misrecblank.to_pickle(processfolder + 'rem_misrecblank.pkl')
    print 'len(dfmisrecblank) = ' , len(dfmisrecblank), '  len(dfrem_misrecblank) = ',  len(dfrem_misrecblank) 
    [dfmisrecsplit2_2,dfrem_misrecsplit2_2] = utils.compareDF(dfrem_misrecblank, dfsplit2_2,constant.runid[r])
    print ' len(dfrem_misrecsplit2_2) = ', len(dfrem_misrecsplit2_2) 
    dfmisrecsplit2_2.to_pickle(processfolder + 'misrecsplit2_2.pkl')
    dfrem_misrecsplit2_2.to_pickle(processfolder + 'rem_misrecsplit2_2.pkl')
    print 'after dLL < -15:' ,len(dfrem_misrecsplit2_2[dfrem_misrecsplit2_2.ll - dfrem_misrecsplit2_2.llc < -15])

    dfrem_misrecsplit2_2c  = pd.DataFrame(columns=dfall.columns)

    dfrem_misrecsplit2_2c =  dfrem_misrecsplit2_2[dfrem_misrecsplit2_2.ll - dfrem_misrecsplit2_2.llc < -15]
    dfrem_misrecsplit2_2c.to_pickle(processfolder + 'rem_misrecsplit2_2c.pkl')

    pbclusters2_2 = pd.DataFrame(columns=dfall.columns)

    pbclusters2_2 = dfrem_misrecsplit2_2c.append(dfrem_rem_sim0blanksplit2_2c)

    pbclusters2_2.to_pickle(processfolder + 'pbclusters2_2.pkl')


#    print res



#     #################################
#     ## comparison simzero of split ##
#     #################################
#     [dfcomm, dfremainder] = utils.compareDF(dfsplit2_2, dfsimzero,constant.runid[r])
#     print len(dfcomm[dfcomm.ll - dfcomm.llc < 0]), ' ' ,len(dfremainder)
#     print len(dfsimzero[dfsimzero.ll - dfsimzero.llc < -15])
#     print len(dfsimzero)
    
