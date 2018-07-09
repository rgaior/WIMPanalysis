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
import glob 
import argparse

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("folder", type=str, nargs='?',default='', help="root file folder")
parser.add_argument("type", type=str, nargs='?',choices=['sim', 'data', 'blank'] ,help="type of data tag")
args = parser.parse_args()
type = args.type
folder = args.folder

if type == 'sim':
    fbase = '*0-*.root*'
else:
    fbase = '*.root*'
    
files = glob.glob(folder + fbase)
first = True
outfolder = folder + '/pkl/'
for f in files:
#    if 'sim100_0-1_034_' in f:
#        continue
    outname = f[f.rfind('/'):-5] + '.pkl'
    print 'input  = ' , f 
    print 'output = ', outfolder  + outname
    if first == True:
        dfall = utils.readsimtree(f,type)
        first = False
        df = utils.readsimtree(f,type)
        df.to_pickle(outfolder  + outname)
    else:
        df = utils.readsimtree(f,type)
        
        df.to_pickle(outfolder  + outname)
        dfall = dfall.append(df)

dfall.to_pickle(outfolder + './simall.pkl')

#print df
