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
import ROOT as R
produce = False
dllcut = -15
plotname = 'cut_' + str(dllcut)
fignr, arnr = plt.subplots(figsize=(8,6))     

#for r in ['run30ks1','run100ks1','run100ks2']:
for r in ['run100ks1']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    file = folder + '/pkl/' + 'simall.pkl'
    dfori = pd.read_pickle(file)
    count = 0
    for index, row in dfori.iterrows():
        if (row['efit'] > 0.8) or (row['efit'] < 0.7):
            continue
        if count > 10:
            break
        count+=1
        fig = plt.figure()
        filesec = '100' if ('100000' in constant.usedfolder[r]) else '30'
        runid = row['RUNID']
        extid = row['EXTID']
        ind = str(constant.runid[r].index(runid)+1)
        imfile = constant.usedfolder[r] + 'sim'+ filesec + '_0-1_' + str(ind.zfill(3)) + '_' + str(int(extid))  + '.root'

        f = R.TFile(imfile)
        im = f.Get("image")
        fig.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid))
        delta_x = 15
        delta_y = 4
        centralbin_x = int(row['centerx'])
        centralbin_y = int(row['centery'])
        image = utils.getimagepart(im,centralbin_x,centralbin_y,delta_x,delta_y)
        print 'centralbin_x = ',centralbin_x,'centralbin_y = ',centralbin_y
        print ' ' , np.min(image[0]), ' ' , np.max(image[0]), ' ' , np.min(image[1]), ' ', np.max(image[1])
        plt.imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
        plt.gca().annotate('E = ' +str(row['efit']),xy=(0,1),xytext=(0,1), xycoords ='axes fraction', fontsize=20)
        plt.gca().annotate('LL = ' +str(row['ll']),xy=(1,1),xytext=(1,1), xycoords ='axes fraction', fontsize=20)
        plt.gca().annotate('LLC = ' +str(row['llc']),xy=(1,0.9),xytext=(1,0.9), xycoords ='axes fraction', fontsize=20)
        
        plt.colorbar()
plt.show()
#        print row['meanx']
