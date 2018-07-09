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
runs = ['run30ks4']
run = runs[0]
dlllimit = -23
elimit = 2 # kev
fname = 'data'
iteration = 4
folder = constant.basefolders[iteration]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
# get the format of the dataframe
df = utils.initialize_dataframe(exemplepath)
df = utils.mergeruns(runs,folder,fname,df)

#define the cut related to the DLL 
dllcut = ' ll - llc < ' + str(dlllimit) 
fidcut = 'sigma > 0.3 & sigma < 0.8'
ecut =  ' ene1 < '+str(elimit)
# perform 
dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut + ' & ' + ecut)

outfile = constant.outfolder + '/eventlist/' + run+'ev_'+ 'E_' + str(elimit)+ 'dll_'+str(dlllimit) + '.txt'
utils.writebrowsercommand(dfsel, outfile, run, iteration)

