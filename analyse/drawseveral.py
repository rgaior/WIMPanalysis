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
parser.add_argument("infile", type=str, nargs='?',default=0, help="pickle file with the cluster you want to draw")
parser.add_argument("--nelec", action='store_true', help="display the nelec map")
parser.add_argument("--sigma", action='store_true', help="display the sigma map")
args = parser.parse_args()
# input file
infile = args.infile
# condition for the nelec and sigma maps
nelec = args.nelec
sigma = args.sigma

#condition for displaying the cluster
delta_x = 10
delta_y = 3

# build the image file name:
df = pd.read_pickle(infile)
# add a condition:
df = df[df.ll - df.llc < -15]


for index, row in df.iterrows():    
    runid = row.RUNID
    extid = row.EXTID
#    if runid !=2481:
#        continue
    for rname, ids in constant.runid.iteritems():
        if runid in ids:
            runname = rname
    if runname == 'run100ks2':
        ind = str(constant.runid[runname].index(runid) + 1 + 9)
    else:
        ind = str(constant.runid[runname].index(runid) + 1 )


    filesec = '100' if ('100000' in constant.usedfolder[runname]) else '30'
    filename = 'sim'+ filesec + '_0-1_' + str(ind.zfill(3)) + '_' + str(int(extid))  + '.root'
    folder = constant.usedfolder[runname] 
    file = folder + filename
    runpathname = folder[folder.find('damic1x100')+len('damic1x100')+1:folder.find('/cluster_sim')]
    fileelec = '/Users/gaior/DAMIC/data/processed/processed/'+runpathname + '/roots/'  + filename

    f = R.TFile(file)
    im = f.Get("image")
#    centralbin_x = int(row.centerx)
    centralbin_x = int(row.meanx)
    centralbin_y = int(row.centery)
    starx = row.meanx
    stary = row.centery

    image = utils.getimagepart(im,centralbin_x,centralbin_y,delta_x,delta_y)
#print image[2]
    if nelec == False and sigma == False:
        print 'here nelec = false'
        f, axarr = plt.subplots()
        f.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid),fontsize=20)
        plt.imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
#        plt.plot(np.array([row.centerx]),np.array([row.centery]),'*r',markersize=10)
        plt.plot(np.array([starx]),np.array([stary]),'*r',markersize=10)
#        plt.plot(np.array([centralbin_x]),np.array([centralbin_y]),'*r',markersize=10)
        axarr.set_xlabel('X [pixel]')
        axarr.set_ylabel('Y [pixel]')
        plt.colorbar()
    elif nelec ==True and sigma == False:    
        print ' here nelec = trye  sigma  = false'
        felec = R.TFile(fileelec)
        imelec = felec.Get("sim/nelec")
        #    imelec = felec.Get("sigma")
        print imelec
        f, axarr = plt.subplots(1,2, figsize=(14,6))
        f.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid),fontsize=20)
        imageelec = utils.getimagepart(imelec,centralbin_x,centralbin_y,delta_x,delta_y)
        adc = axarr[0].imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
        elec = axarr[1].imshow(imageelec[2],origin='lower',extent=[np.min(imageelec[0]),np.max(imageelec[0])+1,np.min(imageelec[1]),np.max(imageelec[1])+1],aspect='auto')
        axarr[0].plot(np.array([starx]),np.array([stary]),'*r',markersize=10)
        axarr[1].plot(np.array([starx]),np.array([stary]),'*r',markersize=10)
        f.colorbar(adc, ax=axarr[0])
        f.colorbar(elec, ax=axarr[1])
        axarr[0].set_xlabel('X [pixel]')
        axarr[0].set_ylabel('Y [pixel]')
        axarr[1].set_xlabel('X [pixel]')
        axarr[1].set_ylabel('Y [pixel]')

    elif nelec == True and sigma == True:
        print ' here nelec = trye  sigma  = true'
        felec = R.TFile(fileelec)
        imelec = felec.Get("sim/nelec")
        imsigma = felec.Get("sigma")
        f, axarr = plt.subplots(1,3, figsize=(14,6), sharey=True)
        f.suptitle('cluster on RUNID: '+ str(runid) + ' ext: '+ str(extid),fontsize=20)
        imageelec = utils.getimagepart(imelec,centralbin_x,centralbin_y,delta_x,delta_y)
        imagesigma = utils.getimagepart(imsigma,centralbin_x,centralbin_y,delta_x,delta_y)
        adc = axarr[0].imshow(image[2],origin='lower',extent=[np.min(image[0]),np.max(image[0])+1,np.min(image[1]),np.max(image[1])+1],aspect='auto')
        elec = axarr[1].imshow(imageelec[2],origin='lower',extent=[np.min(imageelec[0]),np.max(imageelec[0])+1,np.min(imageelec[1]),np.max(imageelec[1])+1],aspect='auto')
        sig = axarr[2].imshow(imagesigma[2],origin='lower',extent=[np.min(imagesigma[0]),np.max(imagesigma[0])+1,np.min(imagesigma[1]),np.max(imagesigma[1])+1],aspect='auto')
        axarr[0].plot(np.array([starx]),np.array([stary]),'*r',markersize=10)
        axarr[1].plot(np.array([starx]),np.array([stary]),'*r',markersize=10)
        axarr[2].plot(np.array([starx]),np.array([stary]),'*r',markersize=10)
        f.colorbar(adc, ax=axarr[0])
        f.colorbar(elec, ax=axarr[1])
        f.colorbar(sig, ax=axarr[2])
        axarr[0].set_xlabel('X [pixel]')
        axarr[0].set_ylabel('Y [pixel]')
        axarr[0].title.set_text('ADU')
        axarr[1].set_xlabel('X [pixel]')
        axarr[1].set_ylabel('Y [pixel]')
        axarr[1].title.set_text('Nelec')
        axarr[2].set_xlabel('X [pixel]')
        axarr[2].set_ylabel('Y [pixel]')
        axarr[2].title.set_text('sigma')
        f.tight_layout()
# top=0.888,
# bottom=0.13,
# left=0.061,
# right=0.967,
# hspace=0.2,
# wspace=0.195

#    axarr[0].colorbar()
    




plt.show()
