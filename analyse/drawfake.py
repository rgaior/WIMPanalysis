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
#for r in ['run30ks1']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    file = folder + '/pkl/' + 'simall.pkl'
    folderblank = folder[:folder.rfind('cluster_sim')] + '/blank/'
    print 'folder blank = ', folderblank
    fileblank = folderblank + '/pkl/simall.pkl'
    dfori = pd.read_pickle(file)
    df = dfori[dfori.simx == 0]
    dfblank = pd.read_pickle(fileblank)
    outfolder = folder[:folder.rfind('cluster_sim')] + '/processed/'
    if produce == True:
        dfcomm = pd.DataFrame(columns=df.columns)
        dffake = pd.DataFrame(columns=df.columns)
        blanksize = dfblank.shape[0]
        simsize = df.shape[0]
        for dsim in range(simsize):
            dsimtemp = df.iloc[dsim]
            com = False
            for d in range(blanksize):
                dtemp = dfblank.iloc[d]
                if (dsimtemp.centerx == dtemp.centerx) and (dsimtemp.centery == dtemp.centery):                
#                print 'dtemp.centerx = ' , dtemp.centerx , ' dsimtemp.centerx = ' , dsimtemp.centerx
#                print 'dtemp.centery = ' , dtemp.centery , ' dsimtemp.centery = ' , dsimtemp.centery
                    com = True
            if com == True:
                dfcomm = dfcomm.append(dsimtemp)                
            else:
                dffake = dffake.append(dsimtemp)                
#    df = dfori[dfori.simx == 0]
        dfcomm.to_pickle(outfolder  + 'common.pkl')
        dffake.to_pickle(outfolder  + 'fake.pkl')

    else:
        dfcomm = pd.read_pickle(outfolder  + 'common.pkl')
        dffake = pd.read_pickle(outfolder  + 'fake.pkl')


    dfcomm = dfcomm[(dfcomm.ll - dfcomm.llc > dllcut)]
    dffake= dffake[(dffake.ll - dffake.llc > dllcut)]
    
    for index, row in dffake.iterrows():
        fig = plt.figure()

        filesec = '100' if ('100000' in constant.usedfolder[r]) else '30'
        
#        filesec = '100' if ('10000' in  'skjdnf1000') else  '30'
        print 'filesec = ' , filesec
#sim30_0-1_012_12.root
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
        print 'centralbin_x = ',centralbin_x,'centralbin_y = ',centralbin_y
        image = utils.getimagepart(im,centralbin_x,centralbin_y,delta_x,delta_y)
        print ' ' , np.min(image[0]), ' ' , np.max(image[0]), ' ' , np.min(image[1]), ' ', np.max(image[1])
        plt.imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1])-1,np.max(image[1])],aspect='auto')
        plt.colorbar()
plt.show()
#        print row['meanx']
