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

produce = False
dllcut = -15
plotname = 'cut_' + str(dllcut)
fignr, arnr = plt.subplots(figsize=(8,6))     
delX = 4
delY = 2

for r in ['run30ks1','run100ks1','run100ks2']:
#for r in ['run100ks2']:
#for r in ['run30ks1']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    files = glob.glob(folder + '/pkl/' + '*_0-1*.pkl')
    dffirst = pd.read_pickle(files[0])
    dfallsplitted = pd.DataFrame(columns=dffirst.columns)
    outfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
    simeegalzero = 0
    deltaY = np.array([])
    for f in files:
        dfori = pd.read_pickle(f)
        #        df = dfori[dfori.simx == 0]
        # check for splitted event in all the events
        allsize = dfori.shape[0]
        for itori in range(allsize):
            dftemp = dfori.iloc[itori]
            for itrest in range(itori+1, allsize):
                dfcomp = dfori.iloc[itrest]
                if ( (dftemp['EXTID'] == dfcomp['EXTID']) and (dftemp['RUNID'] == dfcomp['RUNID']) and ( np.abs(dftemp['centerx'] - dfcomp['centerx']) < delX) and ( np.abs(dftemp['centery'] - dfcomp['centery']) < delY) ):
                    #if ( (dftemp['EXTID'] == dfcomp['EXTID']) and (dftemp['RUNID'] == dfcomp['RUNID']) and ( np.abs(dftemp['centerx'] - dfcomp['centerx']) < 1) ):                    
#                    if (dftemp.sime== 0 or dfcomp.sime == 0):
                    dfallsplitted = dfallsplitted.append(dftemp)
                    dfallsplitted = dfallsplitted.append(dfcomp)
#                        deltaY = np.append(deltaY, np.abs(dftemp['centery'] - dfcomp['centery']) )


#                    print itori, ' ' , itrest
#                    print '-------------TEMP------------------ ', dftemp
#                    print '--------------COMP------------------', dfcomp
#    plt.hist(deltaY,bins=np.arange(0,40,1),histtype = 'step',log=True,label=r)
    print 'dfallsplitted = ' ,  len(dfallsplitted)
    dfallsplitted.to_pickle(outfolder  + 'splitted_dx'+str(delX) + '_dy'+str(delY)+'.pkl')  
    print len(dfallsplitted[dfallsplitted.sime==0])
    print len(dfallsplitted[ (dfallsplitted.sime==0) & (dfallsplitted.ll - dfallsplitted.llc < -25)])

plt.show()



