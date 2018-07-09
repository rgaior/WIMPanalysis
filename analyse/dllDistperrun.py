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
dlllimit = -7
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
df = utils.initialize_dataframe(exemplepath)
df = utils.mergeruns(runs,folder,fname,df)
fidcut = 'sigma > 0.3 & sigma < 0.8'
fidcutout = 'sigma < 0.3 |  sigma > 0.8'
colors = ['r','b','g','y','cyan']
dlllimits = [-5,-7,-10,-12,-13]
#ad_hoccut = 'RUNID > 3337'
ad_hoccut = 'RUNID > 3350'
dllcut2 = ' ll - llc > ' + str(-40) 

dfsel = df.query(constant.basecuts + ' & '+ fidcut + ' & '+ ad_hoccut)
#dfselout = df.query(constant.basecuts + ' & '+ fidcutout + ' & '+ ad_hoccut)
#dfsel = df.query(constant.basecuts + ' & '+ ad_hoccut + ' & ' + dllcut2)
listofid = pd.unique(dfsel.RUNID)
DCfile = '/Users/gaior/DAMIC/data/DC/DC.pkl'
dfDC = pd.read_pickle(DCfile)
dfDC = dfDC[dfDC.image.isin(listofid)]
dfDC = dfDC.query('ext == 1')
print dfDC.shape[0]
#for runid in listofid[::5]:    
a_dc = np.linspace(dfDC['DC'].max(),dfDC['DC'].min(),100)

a_dcres  = np.array([])
bins = np.arange(-30,0,1)
newlist = np.array(listofid[:1])
newlist2 = np.array(listofid[-3:])

#newlist = np.append(newlist,listofid[10])

print newlist
#for runid in newlist:
#for ext in [1,2,3,4,6,11,12]:
#dll = dfsel.ll - dfsel.llc
#plt.scatter(dfsel.ene1,dfsel.sigma,c=dll)
#plt.colorbar()


# for ext in [1,2,6,12]:
# #for ext in [2]:
# #for ext in [3,4,6,11]:
#     dfperid = dfsel.query(dllcut2 + ' & ' + 'EXTID==' +str(ext))        
#plt.hist(dfperid.ll - dfperid.llc, bins=bins, density=True,histtype='step')
plt.hist(dfsel.ll - dfsel.llc, bins=bins,histtype='step')
#plt.hist(dfselout.ll - dfselout.llc, bins=bins,histtype='step')
# plt.legend()
plt.yscale('log')
plt.show()
