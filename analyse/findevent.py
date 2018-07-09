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
runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
runsall = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks4']
#runs = ['run30ks4']
dlllimit = -23
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
# get the format of the dataframe
dfmoriond = utils.initialize_dataframe(exemplepath)
dfall = utils.initialize_dataframe(exemplepath)
dflast = utils.initialize_dataframe(exemplepath)
# merge the runs
dfmoriond = utils.mergeruns(runs,folder,fname,dfmoriond)
dfall = utils.mergeruns(runsall,folder,fname,dfall)
dflast = utils.mergeruns(['run30ks4'],folder,fname,dflast)
#define the cut related to the DLL 
dllcut = ' ll - llc < ' + str(dlllimit) 
fidcut = 'sigma > 0.3 & sigma < 0.8'
# perform 
dfsel = dfall.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut)
dfselM = dfmoriond.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut)
dfselL = dflast.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut)

dfselM.to_pickle(constant.outfolder + 'event/' + 'evmoriond.pkl')
dfsel.to_pickle(constant.outfolder + 'event/' + 'evall.pkl')
dfselL.to_pickle(constant.outfolder + 'event/' + 'ev_run30ks4.pkl')

print 'my event = ' , dfsel.shape[0] 
print 'my event = ' , dfselM.shape[0]
binsize = 0.02
bins = np.arange(0,10,binsize)
#w =((1/binsize)/(4.6/2))*np.ones(len(dfallfidnolast.ene1))
#w = 1*np.ones(len(dfallfidnolast.ene1))
#bins = np.arange(-dlllimit,500,5)
#plt.hist(dfsel.llc - dfsel.ll,bins=bins,histtype='step',label='Moriond + New')
#plt.hist(dfselM.llc - dfselM.ll,bins=bins,histtype='step',label='Moriond')
#plt.yscale('log')
plt.hist(dfsel.ene1,bins=bins,histtype='step',label='Moriond + New')
plt.hist(dfselM.ene1,bins=bins,histtype='step',label='Moriond data set')



# f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
# ax1.hist(dfselL[dfselL.RUNID < 3345].ene1,bins=bins,histtype='step',label='run30ks4 before 3345')
# ax1.legend()
# ax2.hist(dfselL[dfselL.RUNID > 3345].ene1,bins=bins,histtype='step',label='run30ks4 after 3345')
# ax2.legend()
# print dfselL[dfselL.RUNID < 3345].shape[0]
# print dfselL[dfselL.RUNID > 3347].shape[0]
# plt.xlabel('energy [keV]')


#plt.xlabel('-DLL (llc - ll)')
#fig = plt.figure()
#plt.hist(dfall.ll - dfall.llc)
#plt.plot(dfall.centerx, dfall.centery,'o',label='moi')
plt.legend()
plt.show()
