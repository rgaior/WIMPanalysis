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

# ############################
# ##  argument parser       ##
# ############################
# parser = argparse.ArgumentParser()
# parser.add_argument("datatype", type=str, nargs='?',choices=['sim', 'data', 'blank'] ,help="type of data tag")
# args = parser.parse_args()
# datatype = args.datatype

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
dlllimits = [-23,-30,-40]
dlllimit  = -20
dllcut = ' ll - llc < ' + str(dlllimit) 

dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut)
listofid = pd.unique(dfsel.RUNID)
print listofid
a_evnr = np.array([])
#for runid in listofid[::5]:    
#for runid in listofid:   
listextid = constant.extensionlist
for extid in constant.extensionlist:
    dfperid = dfsel.query('EXTID=='+str(extid))
    evnr = dfperid.shape[0]
    print evnr
    a_evnr = np.append(a_evnr,evnr)
#    plt.hist(dfperid.ll - dfperid.llc,bins=np.arange(0,-100,1), label='runid = ' + str(runid) )
#    plt.hist(dfperid.ll - dfperid.llc,bins=np.arange(-100,0,1),histtype='step',log=True)
print np.max(a_evnr)
#plt.hist(a_evnr,bins=np.arange(0,np.max(a_evnr) + 2 , 1) )
print a_evnr
plt.plot(listextid,a_evnr,'x')
plt.ylim(0,np.max(a_evnr) + 1)
plt.xlabel('ext ID')
plt.ylabel('nr of event')
#plt.legend()
plt.show()
