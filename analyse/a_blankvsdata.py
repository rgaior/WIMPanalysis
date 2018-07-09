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
from mpl_toolkits.axes_grid1 import make_axes_locatable

savefig=True

iteration = 4
runsall = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks3','run30ks4','run30ks5']
runMoriond = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
runafter = ['run30ks3','run30ks4','run30ks5']
run3 = ['run30ks3']
run4 = ['run30ks4']
run5 = ['run30ks5']

run100ks1 = ['run100ks1']
run100ks2 = ['run100ks2']
run100ks3 = ['run100ks3']
run30ks1 = ['run30ks1']
run30ks2 = ['run30ks2']
run30ks3 = ['run30ks3']
run30ks4 = ['run30ks4']
run30ks5 = ['run30ks5']

dlllimit = -25
fname = 'data'
fnameblank = 'blank'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
##### common cuts
dllcut = ' ll - llc < ' + str(dlllimit) 
fidcut = 'sigma > 0.3 & sigma < 0.8'
E1 = 0.1
E2 = 10
deltaE = E2 - E1
Ecut = 'ene1 > '+str(E1)+' & ene1 < ' + str(E2) 

DCfile = '/Users/gaior/DAMIC/data/DC/DC_vs_runID_2473_3576.pkl'
dfDC = pd.read_pickle(DCfile)
dclimvalue = 0.2
s_dclimvalue = str(dclimvalue).replace('.','_')

imcuts = utils.produceimagecut(dfDC,dclimvalue)
binsize = 0.35
#bins = np.arange(0.05,10,binsize)
bins = np.arange(-100,0,binsize)
 

#names = ['runMoriond']
#allruns = [runMoriond]


names = ['run30ks5']
allruns = [run30ks5]


extnr = len(constant.extensionlist)
a_rate = np.array([])
a_errrate = np.array([])

fspec, axspec = plt.subplots()
first = True
for runs,n in zip(allruns,names):
    
    # get the format of the dataframe
    df = utils.initialize_dataframe(exemplepath)
    dfb = utils.initialize_dataframe(exemplepath)
    # merge the runs
    df = utils.mergeruns(runs,folder,fname,df)
    dfb = utils.mergeruns(runs,folder,fnameblank,dfb)

#    dfsel = df.query(constant.basecuts)
#    dfselb = dfb.query(constant.basecuts)
    dfsel = df.query(constant.basecuts + ' & ' + fidcut)
    dfselb = dfb.query(constant.basecuts + ' & ' + fidcut)

    for imc in imcuts:
        dfsel = dfsel.query(imc)
        dfselb = dfselb.query(imc)


plt.hist(dfsel.ll - dfsel.llc,bins=bins,histtype='step',log=True)
plt.hist(dfselb.ll - dfselb.llc,bins=bins,histtype='step',log=True)
plt.show()
