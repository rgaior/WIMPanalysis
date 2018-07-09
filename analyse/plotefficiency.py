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



#fignr, arnr = plt.subplots(figsize=(8,6))     
figsimE, arsimE = plt.subplots(figsize=(8,6))     
figeff, areff = plt.subplots(figsize=(8,6))     
colors = plt.rcParams['axes.prop_cycle']
for r,c in zip(['run100ks1','run100ks2','run30ks1'],colors):
#for r in ['run100ks1']:
#    c = c.values()
    folder = constant.usedfolder[r]
    run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    file = folder + '/pkl/' + 'simall.pkl'
    dfori = pd.read_pickle(file)
    df = dfori[dfori.simx != 0]
    files = glob.glob(folder + '/*.root') 
    print 'run = ', run
    if '30000' in run:
        nrofsimevent = 30
    if '100000' in run:
        nrofsimevent = 100
    totnrofevent = nrofsimevent*len(files)
    print 'totnrofevent = ' , totnrofevent
    binsize = 0.05 #eV
    detltaE = 1 # eV
    bins = np.arange(0,1,binsize)
    nrofeventperbin = totnrofevent/(detltaE/binsize)
    print 'nrofeventperbin  = ' , nrofeventperbin
    ################## the simulated spectrum
#    arsimE.hist(df.sime,bins = bins, histtype='step',label=r,lw=2,log=True)
#    arsimE.hist(df.efit, bins = bins, histtype='step',label=r,lw=2,log=True)
#    print ' colors = ' , c

    weight = 1/(np.ones(len(df.ene1))*nrofeventperbin)
    print weight
#    n, b,  patches  = arsimE.hist(df.ene1,weights=weight, bins = bins, color=c,histtype='step',label=r,lw=2,log=True)
#    n, b,  patches  = areff.hist(df.ene1,weights=weight, bins = bins, color=c,histtype='step',label=r,lw=2,log=True)
#    n, b,  patches  = areff.hist(df.sime,weights=weight, bins = bins, color=c,histtype='step',label=r,lw=2,log=True)
    n, b,  patches  = areff.hist(df.efit,weights=weight, bins = bins,histtype='step',label=r,lw=2)
    n, b,  patches  = areff.hist(df.sime,weights=weight, bins = bins,histtype='step',label='sim E',lw=2)
    print 'n = ' , n
    print 'average eff = ' , np.sum(n)/len(n)
#    print arsimE._get_lines.prop_cycler
#    wid = b[1:] - b[:-1] 
#    areff.bar(b[:-1],n, width=wid,color=c,fill=False,label=r,lw=2,log=True) 
#    areff.step(b[:-1],n,label=r,lw=2) 
#    plt.show() 
#plt.yscale('log')
    areff.set_xlabel('energy [keV]')
    areff.set_ylabel('efficiency')
    areff.legend(loc=4)
# a_eff = np.array([])
# a_err_eff = np.array([])
# prof_eff = np.array([])
# prof_ext = np.array([])

# figeffvsE, arreffvsE = plt.subplots(figsize=(8,6))
# for ext in constant.extensionlist:
#     files = glob.glob(folder + '/pkl/' + '*_'+str(ext)+ '.pkl')
#     print 'be careful to the number of files... there is simall.pkl !'
#     a_efftemp = np.array([])
#     a_reconEtemp = np.array([])
#     a_simEtemp = np.array([])
#     for f in files:        
#         df = pd.read_pickle(f)
#         df = df[df.simx!=0]
#         eff = float(df.shape[0])/nrofsimevent
#         a_efftemp = np.append(a_efftemp,eff)
#         prof_eff = np.append(prof_eff,eff)
#         prof_ext = np.append(prof_ext,ext)
#         a_reconEtemp = np.append(a_reconEtemp,df.efit)  
#     a_eff = np.append(a_eff,np.mean(a_efftemp))
# #    a_err_eff = np.append(a_err_eff,np.std(a_efftemp)/np.sqrt(len(files)))
#     a_err_eff = np.append(a_err_eff,np.std(a_efftemp))
#     arreffvsE.plot()
#     print len(files)

# #sns.regplot(x=prof_ext,y=prof_eff, x_bins=7, fit_reg=None,label='ext.' + str(ext))
# plt.suptitle(run,fontsize=15, fontweight='bold')
# plt.errorbar(constant.extensionlist,a_eff,yerr = a_err_eff,fmt='o',lw=2)
# plt.xlabel('extension')
# plt.ylabel('efficiency')
plt.show()








# ############################
# ##  argument parser       ##
# ############################
# parser = argparse.ArgumentParser()
# parser.add_argument("folder", type=str, nargs='?',default='/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run1/cluster_sim/', help="root file folder")
# args = parser.parse_args()

# folder = args.folder
# #nrofevent = {'30000':30,'100000':100}
# run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]





#    print 'efficiencu = ', eff

 #   print ' extension '  , ext
#    print files
                     


# figprof, arprof= plt.subplots(figsize=(6,6))     
# for ext in constant.extensionlist:
#     dftemp= df[df.EXTID==ext]
#     sns.regplot(x=dftemp.sime, y=(dftemp.efit - dftemp.sime)/dftemp.sime, x_bins=10, fit_reg=None,label='ext.' + str(ext))

# figprof.suptitle(run,fontsize=15, fontweight='bold')
# figp.suptitle(run,fontsize=15, fontweight='bold')
# arp.set_xlabel()
# arprof.legend()
# arp.legend()

#plt.xlabel('sime [keV]')
#plt.ylabel('(efit - sime)/sime')
# bins = 20
# #### diff data - sim
# figdE, ardE= plt.subplots(figsize=(6,6))
# #figE.subplots_adjust(left=0.2)f
# figdE.suptitle(run,fontsize=15, fontweight='bold')
# ardE.hist(df.efit - df.sime,bins=bins,histtype='step',log=True,lw=2)
# ardE.set_xlabel('delta E: efit- sime')
# print np.mean(df.efit - df.sime), ' rms = ', np.std(df.efit - df.sime)
 
# figdX, ardX= plt.subplots(figsize=(6,6))
# figdX.suptitle(run,fontsize=15, fontweight='bold')
# ardX.hist(df.centerx - df.simx,bins=bins,histtype='step',log=True,lw=2)
# ardX.set_xlabel('delat X: centerx - simx')

# figdY, ardY= plt.subplots(figsize=(6,6))
# figdY.suptitle(run,fontsize=15, fontweight='bold')
# ardY.hist(df.centery - df.simy,bins=bins,histtype='step',log=True,lw=2)
# ardY.set_xlabel('delat Y: centery - simy')

# #### simulated data
# figsX, arsX= plt.subplots(figsize=(6,6))
# figsX.suptitle(run,fontsize=15, fontweight='bold')
# arsX.hist(df.simx,bins=bins,histtype='step',log=True,lw=2)
# arsX.set_xlabel('simulated: simx')

# figsY, arsY= plt.subplots(figsize=(6,6))
# figsY.suptitle(run,fontsize=15, fontweight='bold')
# arsY.hist(df.simy,bins=bins,histtype='step',log=True,lw=2)
# arsY.set_xlabel('simulated: simy')

# #### fitted data
# figfX, arfX= plt.subplots(figsize=(6,6))
# figfX.suptitle(run,fontsize=15, fontweight='bold')
# arfX.hist(df.centerx,bins=bins,histtype='step',log=True,lw=2)
# arfX.set_xlabel('fitted: centerx')

# figfY, arfY= plt.subplots(figsize=(6,6))
# figfY.suptitle(run,fontsize=15, fontweight='bold')
# arfY.hist(df.centery,bins=bins,histtype='step',log=True,lw=2)
# arfY.set_xlabel('fitted: centery')

####

# figdE.savefig(folder + '/plots/' + 'E_diff'+run+'.png')
# figdX.savefig(folder + '/plots/' + 'X_diff'+run+'.png')
# figdY.savefig(folder + '/plots/' + 'Y_diff'+run+'.png')
# figsX.savefig(folder + '/plots/' + 'X_sim'+run+'.png')
# figsY.savefig(folder + '/plots/' + 'Y_sim'+run+'.png')
# figfX.savefig(folder + '/plots/' + 'X_fit'+run+'.png')
# figfY.savefig(folder + '/plots/' + 'Y_fit'+run+'.png')



# figEvsE, arEvsE= plt.subplots(figsize=(6,6))
# #figE.subplots_adjust(left=0.2)f
# figEvsE.suptitle(run,fontsize=15, fontweight='bold')
# arEvsE.plot(df.sime, df.efit,'.')

# arEvsE.set_ylabel('efit')
# arEvsE.set_xlabel('sime')
# #print np.mean(df.efit - df.sime), ' rms = ', np.std(df.efit - df.sime)


#plt.show()
