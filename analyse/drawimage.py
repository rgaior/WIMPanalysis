import ROOT as R
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
import constant
import argparse

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("run", type=str, nargs='?',default='run100ks1', help="runs")
parser.add_argument("runid", type=int, nargs='?',default=2473, help="runid")
parser.add_argument("extid", type=int, nargs='?',default=1, help="runs")
parser.add_argument("centerx", type=int, nargs='?',default=6000, help="center x")
parser.add_argument("centery", type=int, nargs='?',default=20, help="center y")
parser.add_argument("--nelec", type=int, nargs='?',default=0, help="")
args = parser.parse_args()
run = args.run
runid = args.runid
extid = args.extid
centerx = args.centerx
centery = args.centery
nelec = args.nelec
#file = "/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run1/cluster_sim/sim100_0-1_004_11.root"
#file = "/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run1/blank/blank_d44_snolab_Int-800_Exp-100000_2481_1.root"

folder = constant.usedfolder[run]
if run == 'run100ks2':
    ind = str(constant.runid[run].index(runid) + 1 + 9)
else:
    ind = str(constant.runid[run].index(runid) + 1 )
print ind
filesec = '100' if ('100000' in constant.usedfolder[run]) else '30'
filename = 'sim'+ filesec + '_0-1_' + str(ind.zfill(3)) + '_' + str(int(extid))  + '.root'
file = constant.usedfolder[run] + filename
runname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
fileelec = '/Users/gaior/DAMIC/data/processed/processed/'+runname + '/roots/'  + filename

f = R.TFile(file)
im = f.Get("image")
centralbin_x = centerx
centralbin_y = centery
delta_x = 10
delta_y = 4
image = utils.getimagepart(im,centralbin_x,centralbin_y,delta_x,delta_y)
#print image[2]
if nelec == 0:
    f, axarr = plt.subplots()
    f.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid),fontsize=20)
    plt.imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
    axarr.set_xlabel('X [pixel]')
    axarr.set_ylabel('Y [pixel]')
    plt.colorbar()
else:    
    felec = R.TFile(fileelec)
    print fileelec
    imelec = felec.Get("sim/nelec")
#    imelec = felec.Get("sigma")
    print imelec
    f, axarr = plt.subplots(1,2, figsize=(14,6))
    f.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid),fontsize=20)
    imageelec = utils.getimagepart(imelec,centralbin_x,centralbin_y,delta_x,delta_y)
    adc = axarr[0].imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
    elec = axarr[1].imshow(imageelec[2],origin='lower',extent=[np.min(imageelec[0]),np.max(imageelec[0])+1,np.min(imageelec[1]),np.max(imageelec[1])+1],aspect='auto')
    f.colorbar(adc, ax=axarr[0])
    f.colorbar(elec, ax=axarr[1])
    axarr[0].set_xlabel('X [pixel]')
    axarr[0].set_ylabel('Y [pixel]')
    axarr[1].set_xlabel('X [pixel]')
    axarr[1].set_ylabel('Y [pixel]')
#    axarr[0].colorbar()
    




plt.show()
