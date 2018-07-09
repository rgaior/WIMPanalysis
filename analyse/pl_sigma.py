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

savefig=False

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

dlllimit = -30
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
##### common cuts
dllcut = ' ll - llc < ' + str(dlllimit) 
fidcut = 'sigma > 0.3 & sigma < 0.8'
E1 = 0 
E2 = 10
deltaE = E2 - E1
Ecut = 'ene1 > '+str(E1)+' & ene1 < ' + str(E2) 
extcut = 'EXTID== 6'
plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20180604/'

DCfile = '/Users/gaior/DAMIC/data/DC/DC_vs_runID_2473_3576.pkl'
dfDC = pd.read_pickle(DCfile)
dclimvalue = 0.1
s_dclimvalue = str(dclimvalue).replace('.','_')

imcuts = utils.produceimagecut(dfDC,dclimvalue)

binsize = 0.05
bins = np.arange(0,10,binsize)

efficiencyfile ='/Users/gaior/DAMIC/data/efficiency/extracted.pkl'
eff = pd.read_pickle(efficiencyfile)
#e_eff = eff.e
#eff_eff = eff.eff

#names = ['arunMorind','run30ks3','run30ks4','run30ks5']
#allruns = [runMoriond,run30ks3,run30ks4,run30ks5]
#names = ['run30ks5']
#allruns = [run30ks5]

#names = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks3','run30ks4','run30ks5']
#allruns = [run100ks1,run100ks2,run100ks3,run30ks1,run30ks2,run30ks3,run30ks4,run30ks5]

#names = ['run1Moriond','runafter','run30ks3']
#allruns = [runMoriond,runafter,run30ks3]

#names = ['runall']
#allruns = [runsall]
names = ['run1Moriond','runafter']
allruns = [runMoriond,runafter]

#names = ['run1Moriond','run30ks3']
#allruns = [runMoriond,run30ks3]

#allruns = [run1,run2,run12]
#names = ['Moriond','run4']
#allruns = [runMoriond,run4]
#names = ['Moriond','run3','run4','run5']
#allruns = [runMoriond,run3,run4,run5]
extnr = len(constant.extensionlist)
a_rate = np.array([])
a_errrate = np.array([])

fspec, axspec = plt.subplots()
first = True
for runs,n in zip(allruns,names):
    # get the format of the dataframe
    df = utils.initialize_dataframe(exemplepath)
    # merge the runs
    df = utils.mergeruns(runs,folder,fname,df)
    expo = 0
    for r in runs:
        expo += utils.getrunexposure(r,extnr)

        rmexpo = utils.removedexpofromDC(r,dfDC,dclimvalue)
#        print 'rmexpo = ' , rmexpo
        expo -= rmexpo
    print 'expo =  ', expo
    dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut + '&' + Ecut )
    for imc in imcuts:
        dfsel = dfsel.query(imc)
        
    rate = float(len(dfsel))/expo
    errrate = np.sqrt(float(len(dfsel)))/expo
    a_rate = np.append(a_rate,rate)
    a_errrate = np.append(a_errrate,errrate)
    #    norm = (1./float(expo))*np.ones(len(dfsel.ene1))
    #    plt.hist(dfsel.ene1,bins=bins,weights=norm,histtype='step',label=n)
    bins = np.arange(0.25,0.85,0.05)
    plt.hist(dfsel.sigma,bins=bins,histtype='step',lw=2,label=n)

plt.legend(loc=2)
plt.show()
