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
import seaborn as sns
import time as t

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("basename", type=str, nargs='?',default='', help="name of the plots")
args = parser.parse_args()

elim = 0.2
basename = args.basename
#for r in ['run100ks1','run100ks2','run30ks1']:
for r in ['run100ks1']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    file = folder + '/pkl/' + 'simall.pkl'
    dfori = pd.read_pickle(file)
    df = dfori[(dfori.simx != 0) & (dfori.sime < elim)]
    # & (dfori.ll-dfori.llc < -500) 




### Energy of fake and energy of all:
    figE, arE = plt.subplots(figsize=(8,6))     
    figE.suptitle(run,fontsize=15,fontweight='bold')
#    bins = np.arange(-0.3,0.3,0.005)
#    bins = np.arange(-0.5,0.5,0.005)
    bins = np.arange(-2,2,0.005)
#     arE.hist( (df.efit-df.sime),bins=bins,histtype='step',lw=2,label='efit',log=True)
#     arE.hist( (df.ene1-df.sime),bins=bins,histtype='step',lw=2,label='ene1',log=True)
#     arE.hist( (df.ene_integ-df.sime),bins=bins,histtype='step',lw=2,label='ene_integ',log=True)
    arE.hist( (df.efit-df.sime)/df.sime,bins=bins,histtype='step',lw=2,label='efit',log=True,color='b')
    arE.hist( (df.ene1-df.sime)/df.sime,bins=bins,histtype='step',lw=2,label='ene1',log=True,color='r')
 #   arE.hist( (df.ene2-df.sime)/df.sime,bins=bins,histtype='step',lw=2,label='ene2',log=True)
#    arE.hist( (df.ene_integ-df.sime)/df.sime,bins=bins,histtype='step',lw=2,label='ene_integ',log=True)
    arE.set_xlabel('delta E [relative to sim]')
    #arE.hist( (df.ene2-df.sime),bins=bins,histtype='step',lw=2,label='ene2',log=True)
    mu = np.mean((df.efit-df.sime)/df.sime)
    rms = np.std((df.efit-df.sime)/df.sime)
    mu2 = np.mean((df.ene1-df.sime)/df.sime)
    rms2 = np.std((df.ene1-df.sime)/df.sime)
    plt.text(1, 100, r'$\mu = ' +str(np.round(mu,3))+',\ \sigma=' + str(np.round(rms,3)) +'$',color='b',fontsize=15,backgroundcolor='white')
    plt.text(1, 50, r'$\mu = ' +str(np.round(mu2,3))+',\ \sigma=' + str(np.round(rms2,3)) +'$',color='r',fontsize=15,backgroundcolor='white')
#    plt.text(1, 100, 'asd;lgkfnalkgjfn')
    arE.text
    arE.legend(loc=2)
    plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20171213/'
    if basename == '':
        basename = str(t.time())
#    figE.savefig(plotfolder+ basename + '_' + r + '.png')
    
plt.show()
