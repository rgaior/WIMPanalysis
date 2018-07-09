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
runMoriond = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
run3 = ['run30ks3']
run4 = ['run30ks4']
run5 = ['run30ks5']
dlllimit = -23
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
##### common cuts
dllcut = ' ll - llc < ' + str(dlllimit) 
fidcut = 'sigma > 0.3 & sigma < 0.8'

DCfile = '/Users/gaior/DAMIC/data/DC/DC.pkl'
dfDC = pd.read_pickle(DCfile)
dclimvalue = 0.1
imcuts = utils.produceimagecut(dfDC,dclimvalue)
print imcuts
extcut = '& ( (RUNID != 3162  & EXTID != 2) )'

binsize = 0.02
bins = np.arange(0,10,binsize)


names = ['Moriond','run4']
allruns = [runMoriond,run4]
#names = ['Moriond','run3','run4','run5']
#allruns = [runMoriond,run3,run4,run5]
for runs,n in zip(allruns,names):
    # get the format of the dataframe
    df = utils.initialize_dataframe(exemplepath)
    # merge the runs
    df = utils.mergeruns(runs,folder,fname,df)
    dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut)
    for imc in imcuts:
        print imc
#    dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut + extcut)
        dfsel = dfsel.query(imc)
#        print dfsel
    exp = 0
    for index,row in dfsel.iterrows():
        exp += row.exposuretime

    print exp    
    norm = (1./float(exp))*np.ones(len(dfsel.ene1))
    plt.hist(dfsel.ene1,bins=bins,weights=norm,histtype='step',label=n)

plt.legend()
plt.show()
