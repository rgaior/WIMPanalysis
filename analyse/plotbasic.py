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

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("folder", type=str, nargs='?',default='/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run1/cluster_sim/', help="root file folder")
args = parser.parse_args()

folder = args.folder
run = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
print 'rune = ', run
file = folder + '/pkl/' + 'simall.pkl'
#file = folder + '/processed/'+ 'rest_fake_splitted.pkl'
dfori = pd.read_pickle(file)
df = dfori[dfori.simx!=0]
#df = dfori

figp, arp= plt.subplots(figsize=(8,6))     
for ext in constant.extensionlist:
    dftemp= df[df.EXTID==ext]
    arp.plot(dftemp.sime, (dftemp.efit - dftemp.sime)/dftemp.sime,'.',label='ext.' + str(ext))

figprof, arprof= plt.subplots(figsize=(8,6))     
for ext in constant.extensionlist:
    dftemp= df[df.EXTID==ext]
    sns.regplot(x=dftemp.sime, y=(dftemp.efit - dftemp.sime)/dftemp.sime, x_bins=10, fit_reg=None,label='ext.' + str(ext))

figprof.suptitle(run,fontsize=15, fontweight='bold')
figp.suptitle(run,fontsize=15, fontweight='bold')
arp.set_xlabel('simulated E sime [keV]')
arp.set_ylabel('delta E: (efit -  sime)/sime')
arprof.legend()
arp.legend()


bins = 20
#### diff data - sim
figdE, ardE= plt.subplots(figsize=(6,6))
#figE.subplots_adjust(left=0.2)f
figdE.suptitle(run,fontsize=15, fontweight='bold')
ardE.hist((df.efit - df.sime)/df.sime,bins=bins,histtype='step',log=True,lw=2)
ardE.set_xlabel('delta E: (efit- sime)/sime')
print np.mean(df.efit - df.sime), ' rms = ', np.std( (df.efit - df.sime)/df.sime)
 
figdX, ardX= plt.subplots(figsize=(6,6))
figdX.suptitle(run,fontsize=15, fontweight='bold')
ardX.hist(df.centerx - df.simx,bins=bins,histtype='step',log=True,lw=2)
ardX.set_xlabel('delat X: centerx - simx')
print np.mean(df.centerx - df.simx), ' rms = ', np.std( df.centerx - df.simx)

figdY, ardY= plt.subplots(figsize=(6,6))
figdY.suptitle(run,fontsize=15, fontweight='bold')
ardY.hist(df.centery - df.simy,bins=bins,histtype='step',log=True,lw=2)
ardY.set_xlabel('delat Y: centery - simy')

#### simulated data
figsX, arsX= plt.subplots(figsize=(6,6))
figsX.suptitle(run,fontsize=15, fontweight='bold')
arsX.hist(df.simx,bins=bins,histtype='step',log=True,lw=2)
arsX.set_xlabel('simulated: simx')

figsY, arsY= plt.subplots(figsize=(6,6))
figsY.suptitle(run,fontsize=15, fontweight='bold')
arsY.hist(df.simy,bins=bins,histtype='step',log=True,lw=2)
arsY.set_xlabel('simulated: simy')

#### fitted data
figfX, arfX= plt.subplots(figsize=(6,6))
figfX.suptitle(run,fontsize=15, fontweight='bold')
arfX.hist(df.centerx,bins=bins,histtype='step',log=True,lw=2)
arfX.set_xlabel('fitted: centerx')

figfY, arfY= plt.subplots(figsize=(6,6))
figfY.suptitle(run,fontsize=15, fontweight='bold')
arfY.hist(df.centery,bins=bins,histtype='step',log=True,lw=2)
arfY.set_xlabel('fitted: centery')

figsigma, arsigma= plt.subplots(figsize=(6,6))
figsigma.suptitle(run,fontsize=15, fontweight='bold')
arsigma.plot(df.simz, df.sigma,'.')
arsigma.set_xlabel('simz')
arsigma.set_ylabel('sigma')


figdE.savefig(folder + '/plots/' + 'E_diff'+run+'.png')
figdX.savefig(folder + '/plots/' + 'X_diff'+run+'.png')
figdY.savefig(folder + '/plots/' + 'Y_diff'+run+'.png')
figsX.savefig(folder + '/plots/' + 'X_sim'+run+'.png')
figsY.savefig(folder + '/plots/' + 'Y_sim'+run+'.png')
figfX.savefig(folder + '/plots/' + 'X_fit'+run+'.png')
figfY.savefig(folder + '/plots/' + 'Y_fit'+run+'.png')



figEvsE, arEvsE= plt.subplots(figsize=(8,6))
#figE.subplots_adjust(left=0.2)f
figEvsE.suptitle(run,fontsize=15, fontweight='bold')
arEvsE.plot(df.sime, df.efit,'.')

arEvsE.set_ylabel('efit [keV]')
arEvsE.set_xlabel('sime [keV]')
#print np.mean(df.efit - df.sime), ' rms = ', np.std(df.efit - df.sime)


plt.show()
