import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
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

# def expo(x,a,b,c,d):
#     return a*(np.exp((x - b)/c)) + d

def expo(x,a,b,c):
    return a*(np.exp((x - b)/c)) 

def expo_1(x,a,b,c):
    return c*np.log(x/a) + b

iteration = 4
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
#runs = ['run30ks1','run30ks2']
runs = ['run30ks4']
dlllimit = 0
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
df = utils.initialize_dataframe(exemplepath)
df = utils.mergeruns(runs,folder,fname,df)
fidcut = 'sigma > 0.3 & sigma < 0.8'
colors = ['r','b','g','y','cyan']
#dlllimits = [-5,-7,-10,-12,-13]
dlllimits = [-5]
ad_hoccut = 'RUNID < 3337'

#dfsel = df.query(constant.basecuts + ' & '+ fidcut + ' & '+ ad_hoccut)
dfsel = df.query(constant.basecuts + ' & '+ ad_hoccut)
listofid = pd.unique(dfsel.RUNID)
DCfile = '/Users/gaior/DAMIC/data/DC/DC.pkl'
dfDC = pd.read_pickle(DCfile)
dfDC = dfDC[dfDC.image.isin(listofid)]
for ext in constant.extid:
    dfDCtemp = dfDC.query('ext == '+str(ext))
    plt.plot(dfDCtemp.image,dfDCtemp.DC,'.')
plt.show()
