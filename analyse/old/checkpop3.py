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

delX = 2
delY = 2
plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20180116/'

fignr, arnr = plt.subplots(figsize=(8,6))     
produce = True
#for r in ['run100ks1','run100ks2','run30ks1']:
#for r in ['run100ks2']:
for r in ['run30ks1']:
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    print 'run = ', run
    file = folder + '/pkl/' + 'simall.pkl'
    dfori = pd.read_pickle(file)
    df = dfori[ (np.absolute((dfori.sime - dfori.efit)) > 0.13 ) & (dfori.sime!=0)]    
#    df = dfori[ (np.absolute((dfori.sime - dfori.efit)) > 0.13 ) ]    
    folder = folder[:folder.rfind('cluster_sim')] 
    splittedfile = folder + '/processed/' + 'splitted_dx'+str(delX) + '_dy'+str(delY)+'.pkl'
    dfsplitted = pd.read_pickle(splittedfile)
    if produce == True:
        dfcomm = pd.DataFrame(columns=df.columns)
        dfrest = pd.DataFrame(columns=df.columns)
        fakesize = df.shape[0]
        splittedsize = dfsplitted.shape[0]
        for ifake in range(fakesize):
            dfaketemp = df.iloc[ifake]
            com = False
            for isplitted in range(splittedsize):
                dsplittedtemp = dfsplitted.iloc[isplitted]
                if ( (dsplittedtemp.RUNID == dfaketemp.RUNID) and (dsplittedtemp.EXTID == dfaketemp.EXTID) and dsplittedtemp.centerx == dfaketemp.centerx) and (dsplittedtemp.centery == dfaketemp.centery):                
                    print 'dsplittedtemp.ext' , dsplittedtemp.EXTID, 'dfaketemp.ext' , dfaketemp.EXTID , ' dfaketemp.efit ', dfaketemp.efit ,' dfaketemp.sime ', dfaketemp.sime   
                    com = True
            if com == True:
                dfcomm = dfcomm.append(dfaketemp)                
            else:
                dfrest = dfrest.append(dfaketemp)                
#    df = dfori[dfori.simx == 0]
        dfcomm.to_pickle(folder + '/processed/' + 'comm_fake_splitted.pkl')
        dfrest.to_pickle(folder + '/processed/' + 'rest_fake_splitted.pkl')

    else:
        dfcomm = pd.read_pickle(folder  + '/processed/' + 'comm_fake_splitted.pkl')
        dfrest = pd.read_pickle(folder + '/processed/' + 'rest_fake_splitted.pkl')


#    dfcomm = dfcomm[(dfcomm.ll - dfcomm.llc < dllcut)]
#    dfrest= dfrest[(dfrest.ll - dfrest.llc < dllcut)]
    print 'len rest = ' , len(dfrest)
    count = 0 
    print len(dfrest)
    print len(dfcomm)
    for index, row in dfrest.iterrows():
        if count == 50:
            break
        count+=1
        fig = plt.figure()

        filesec = '100' if ('100000' in constant.usedfolder[r]) else '30'
        
#        filesec = '100' if ('10000' in  'skjdnf1000') else  '30'
        print 'filesec = ' , filesec
#sim30_0-1_012_12.root
        runid = row['RUNID']
        extid = row['EXTID']
        if r == 'run100ks2':
            ind = str(constant.runid[r].index(runid) + 1 + 9)
        else:
            ind = str(constant.runid[r].index(runid) + 1 )
        print 'runid = ' , runid
        print 'ind = ' , ind
        imfile = constant.usedfolder[r] + 'sim'+ filesec + '_0-1_' + str(ind.zfill(3)) + '_' + str(int(extid))  + '.root'

        f = R.TFile(imfile)
        im = f.Get("image")
        fig.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid))
        delta_x = 15
        delta_y = 4
        centralbin_x = int(row['centerx'])
        centralbin_y = int(row['centery'])
#        print 'centralbin_x = ',centralbin_x,'centralbin_y = ',centralbin_y
        image = utils.getimagepart(im,centralbin_x,centralbin_y,delta_x,delta_y)
#        print ' ' , np.min(image[0]), ' ' , np.max(image[0]), ' ' , np.min(image[1]), ' ', np.max(image[1])        
        plt.imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
        plt.xlabel("X [pixel]")
        plt.ylabel("Y [pixel]")
        plt.colorbar()
        fig.savefig(plotfolder + 'pop3_ev_r_'+r+'_run_'+str(runid) + '_ext_'+str(extid) + '_'+str(count)+ '.png')
plt.show()
        
# ### nr of fake vs extension:
#     a_nroffake = np.array([])
#     a_ext = np.array([])
#     for ext in constant.extensionlist:
#         dftemp= df[df.EXTID==ext]
#         dforitemp = dfori[dfori.EXTID==ext]
#         a_nroffake = np.append(a_nroffake, float(dftemp.shape[0])/dforitemp.shape[0])
#         a_ext = np.append(a_ext,ext)
#     arnr.plot(a_ext,a_nroffake,'o',label=r)

# ### Energy of fake and energy of all:
#     figE, arE = plt.subplots(figsize=(8,6))     
#     figE.suptitle(run,fontsize=15,fontweight='bold')
#     bins = np.arange(0,2,0.05)
#     arE.hist(dfori.efit,bins=bins,histtype='step',lw=2,label='all',log=True)
#     arE.hist(df.efit,bins=bins,histtype='step',lw=2,label='non simulated only',log=True)
#     arE.set_xlabel('energy [keV]')

# ### depth of fake and depth of all:
#     figSigma, arSigma = plt.subplots(figsize=(8,6))     
#     figSigma.suptitle(run,fontsize=15,fontweight='bold')
#     bins = np.arange(-500,0,5)
#     arSigma.hist(dfori.ll - dfori.llc,bins=bins,histtype='step',lw=2,label='all',log=True)
#     arSigma.hist(df.ll - df.llc,bins=bins,histtype='step',lw=2,label='non simulated only',log=True)
#     arSigma.set_xlabel('ll - llc')

# ### depth of fake and depth of all:
#     figLL_E, arLL_E = plt.subplots(figsize=(8,6))     
#     figLL_E.subplots_adjust(left=0.170)
#     figLL_E.suptitle(run,fontsize=15,fontweight='bold')
#     bins = np.arange(-50,0,1)
#     arLL_E.plot(dfori.efit, dfori.ll - dfori.llc,'.',label='all')
#     arLL_E.plot(df.efit, df.ll - df.llc, 'o', label='non simulated only')
#     arLL_E.set_xlabel('reconstructed E [keV]')
#     arLL_E.set_ylabel('ll - llc')

# ### depth of fake and depth of all:
#     figXY, arXY = plt.subplots(figsize=(8,6))     
#     figXY.suptitle(run,fontsize=15,fontweight='bold')
#     arXY.plot(df.centerx, df.centery,'s')
#     arXY.set_xlabel('X')
#     arXY.set_ylabel('Y')


# ###delta E vs Esim
#     figp, arp= plt.subplots(figsize=(8,6))     
#     figp.suptitle(run,fontsize=15,fontweight='bold')
# #for ext in constant.extensionlist:
#     dftemp= df[df.EXTID==ext]
#     arp.plot(dfori.sime, (dfori.efit - dfori.sime)/dfori.sime,'.',label='all')
#     arp.plot(df.sime, (df.efit - df.sime)/df.sime,'.',label='pop. 3')
#     arp.set_xlabel('simulated E sime [keV]')
#     arp.set_ylabel('delta E: (efit -  sime)/sime')

#     arnr.legend()
#     arLL_E.legend()
#     arE.legend()

#     arSigma.legend()

# #     plotfolder = '/Users/gaior/DAMIC/code/data_analysis/plots/20171219/'
# #     fignr.savefig(plotfolder + '/CheckPop3' + run + '_nr.png' )
# #     figE.savefig(plotfolder + '/CheckPop3' +run + '_E.png' )
# #     figSigma.savefig(plotfolder + '/CheckPop3' + run + '_LL.png' )
# #     figXY.savefig(plotfolder + '/CheckPop3' + run + '_XY.png' )
# #     figLL_E.savefig(plotfolder + '/CheckPop3' + run + '_LLE.png' )
# #     figp.savefig(plotfolder + '/CheckPop3' + run + '_deltaE.png' )



# #plt.show()




# # for r in ['run100ks1','run100ks2','run30ks1']:
# # #for r in ['run100ks1']:
# #     fignr, arnr = plt.subplots(figsize=(8,6))     
# #     folder = constant.usedfolder[r]
# #     run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
# #     print 'run = ', run
# #     file = folder + '/pkl/' + 'simall.pkl'
# #     dfori = pd.read_pickle(file)
# #     df = dfori[dfori.simx != 0]
# #     dfout = df[np.absolute((df.sime - df.efit)) > 0.13]    
# # #    plt.plot(df.sime,df.efit,'ob')
# # #    plt.plot(dfout.sime,dfout.efit,'or')

# # ### Energy of fake and energy of all:
# #     figE, arE = plt.subplots(figsize=(8,6))     
# #     figE.suptitle(run,fontsize=15,fontweight='bold')
# #     bins = np.arange(0,2,0.05)
# #     arE.hist(dfout.efit,bins=bins,histtype='step',lw=2,label='all',log=True)
# #     arE.set_xlabel('energy [keV]')

    

# # # ### nr of fake vs extension:
# # #     a_nroffake = np.array([])
# # #     a_ext = np.array([])
# # #     for ext in constant.extensionlist:
# # #         dftemp= df[df.EXTID==ext]
# # #         dforitemp = dfori[dfori.EXTID==ext]
# # #         a_nroffake = np.append(a_nroffake, float(dftemp.shape[0])/dforitemp.shape[0])
# # #         a_ext = np.append(a_ext,ext)
# # #     arnr.plot(a_ext,a_nroffake,'o',label=r)


# # # ### depth of fake and depth of all:
# # #     figSigma, arSigma = plt.subplots(figsize=(8,6))     
# # #     figSigma.suptitle(run,fontsize=15,fontweight='bold')
# # #     bins = np.arange(0,50,10)
# # #     arSigma.hist(dfori.llc - dfori.ll,bins=bins,histtype='step',lw=2,label='all',log=True)
# # #     arSigma.hist(df.llc - df.ll,bins=bins,histtype='step',lw=2,label='non simulated only',log=True)
# # #     arSigma.set_xlabel('sigma')


# # # arnr.legend()
# # # arE.legend()

# # # arSigma.legend()
# # # arSigma.legend()


# # plt.show()
