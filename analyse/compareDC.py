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

#def expo(x,a,b,c,d):
#    return a*(np.exp((x + b)/c)) + d

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
#dlllimits = [-5,-7,-10,-12,-13,-23]
dlllimits = [-5,-15,-23]
#dlllimits = [-5]
ad_hoccut = 'RUNID < 3337'

#dfsel = df.query(constant.basecuts + ' & '+ fidcut + ' & '+ ad_hoccut)
dfsel = df.query(constant.basecuts + ' & '+ ad_hoccut)
listofid = pd.unique(dfsel.RUNID)
DCfile = '/Users/gaior/DAMIC/data/DC/DC.pkl'
dfDC = pd.read_pickle(DCfile)
dfDC = dfDC[dfDC.image.isin(listofid)]
dfDC = dfDC.query('ext == 1')
print dfDC.shape[0]
#for runid in listofid[::5]:    
dllcut2 = ' ll - llc > ' + str(-40) 
a_dc = np.linspace(dfDC['DC'].max(),dfDC['DC'].min(),100)

a_dcres  = np.array([])

for dlllimit,col in zip(dlllimits,colors):
    a_evnr = np.array([])
    dllcut = ' ll - llc < ' + str(dlllimit) 
    for runid in listofid:
        dfperid = dfsel.query('RUNID=='+str(runid)  + '&' + dllcut + '&' + dllcut2 )        
        evnr = dfperid.shape[0]
        a_evnr = np.append(a_evnr,evnr)
        
#    plt.plot(dfDC.DC/a_evnr)

# #    popt, pcov = curve_fit(expo, dfDC.DC, a_evnr, sigma=np.sqrt(a_evnr) )
    p0 = [1,0,1./1000,1]
#    bounds = ([]
    bounds=(0, [10., 1e-2,1e-2,10])
#    popt, pcov = curve_fit(expo, dfDC.DC, a_evnr, sigma=np.sqrt(a_evnr), p0=p0,bounds=bounds)
    #plt.scatter(dfDC.DC,a_evnr,c=dfDC.image)
#plt.colorbar()
    plt.errorbar(dfDC.DC,a_evnr,xerr=dfDC.DCerr,yerr=np.sqrt(a_evnr),fmt='o',color=col,label='DLL < '+ str(dlllimit))
#    plt.scatter(dfDC.DC,a_evnr,c=listofid)

#    plt.errorbar(listofid,dfDC.DC,yerr=dfDC.DCerr)
#    plt.plot(a_dc,expo(a_dc,*popt),'--',color=col) 
    plt.yscale('log')
#    print popt

    #print 'dc \ Y = 1e-2 = ',expo_1(1e-2,*popt)
#    a_dcres = np.append(a_dcres, expo_1(1e-2,*popt))    
    #plt.xscale('log')
plt.legend()

# figfit = plt.figure()
# fit = np.polyfit(dlllimits,a_dcres,1)
# pfit = np.poly1d(fit)
# x= np.linspace(-30,0,30)
# fitted = pfit(x)
# plt.plot(x,fitted,lw=2,color='k')
# plt.plot(dlllimits,a_dcres,'ro')
plt.show()
