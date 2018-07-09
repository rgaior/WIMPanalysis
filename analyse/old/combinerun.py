import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import pandas as pd
from scipy.optimize import curve_fit

cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
import constant
import glob 
import argparse

def lognorm(x,alpha,mu,sigma,norm):
    return norm*(np.exp(-(np.log(x - alpha) - mu)**2 / (2 * sigma**2)) / ( (x-alpha)  * sigma * np.sqrt(2 * np.pi)))
def expo(x,a,b,c):
    return a*(np.exp((x - b)/c))



# ############################
# ##  argument parser       ##
# ############################
# parser = argparse.ArgumentParser()
# parser.add_argument("datatype", type=str, nargs='?',choices=['sim', 'data', 'blank'] ,help="type of data tag")
# args = parser.parse_args()
# datatype = args.datatype
iteration = 4
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
runs = ['run30ks4']
dlllimit = -20
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
# get the format of the dataframe
dfall = utils.initialize_dataframe(exemplepath)
# merge the runs
dfall = utils.mergeruns(runs,folder,fname,dfall)
#define the cut related to the DLL 
dllcut = ' ll - llc < ' + str(dlllimit) 
# perform cuts
#dfsel = dfall.query(constant.basecuts + ' & ' + dllcut)
dfsel = dfall.query(constant.basecuts + )
firstbin = -50
step = 0.2
lastbin = 0
bins = np.arange(firstbin, lastbin, step)
rangehigh = [-12,-8,-6]
cols = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
for lv,c in zip(rangehigh,cols):
    n,b,p = plt.hist(dfsel['ll']-dfsel['llc'],bins,lw=0,histtype='step')
    cbins = b[:-1] + float(step)/2
    #integral = step*sum(n)
    integral = 1
    err = np.sqrt(n)
    for i in range(len(n)):
        if n[i] == 0:
            n[i] = 0
            err[i] = 1

    plt.errorbar(cbins,n/integral,yerr=err/integral,color='black', fmt='o',fillstyle = 'none')
    newcbins = cbins[cbins<lv]
    newn = n[cbins<lv]
    newerr = err[cbins<lv]
    popt, pcov = curve_fit(expo, newcbins, newn/integral, sigma=newerr/integral)
    print popt
    print pcov
    plt.plot(newcbins,expo(newcbins,popt[0],popt[1],popt[2]),lw=2,c=c,label='right edge = '+str(lv))
    outfolder = '/Users/gaior/DAMIC/code/data_analysis/out/dllfits/'
    fname = ''
    for r in runs:
        fname += r
    fname += str(lv)
    fname += '_'+str(firstbin)
#    np.save(outfolder+fname,popt)

plt.yscale('log')

#print dfsel.shape[0], ' ', dfall.shape[0]
#plt.hist(dfall.ene1)
plt.xlabel('DLL')
plt.legend()
plt.ylim(0.01,np.max(n))
plt.show()

# dlllimit =  -100
# entriesperrun = np.array([])
# rate = np.array([])
# e_rate = np.array([])
# #bins = np.arange(2,100,0.5)
# bins = np.arange(-20,-6,0.2)
# #bins = np.arange(0,15,0.2)
# #bins = np.arange(4000,9000,10)
# #bins = np.arange(0,150,1)
# #    folder = '/Users/gaior/DAMIC/data/20180412/' + constant.runname[r] + '/pkl/'

#     print 'name of file = ', folder + fname + '.pkl'
#     df = pd.read_pickle(folder + fname + '.pkl')
#     dfall = dfall.append(df)





#     print dfall.shape[0]

# dfsel = dfall[(dfall.is_masked == 0) & 
#               (dfall.touchmask == 0) & 
#               (dfall.centery < 42 )  & 
#               (dfall.success ==1)    & 
#               (dfall.centery > 2)  & 
#               (dfall.multirows == 0)    &
# #              (dfall.ll < 100)       &
#               (dfall.RUNID!=2482) &  (dfall.RUNID!=2479) & (dfall.RUNID!=2577)& (dfall.RUNID!=2849) & (dfall.RUNID!=2902) & (dfall.RUNID!=2927) & (dfall.RUNID!=3003) & (dfall.RUNID!=3059) & (dfall.RUNID!=3112) 
# #              (dfall.llc - dfall.ll > 2.5)
              
#               #              (dfall.sigma > 0.3) & (dfall.sigma < 0.8) 
#               #              (dfall.ll - dfall.llc < dlllimit)
#                ]
# n, outbins, patches  = plt.hist(dfsel.ll - dfsel.llc,bins=bins,histtype='step',lw=0,label=r)
# n1, outbins1, patches1  = plt.hist(dfsel.ll - dfsel.llc,bins=bins,histtype='step',lw=1,density=True,label=r)
# delbin = outbins[1] - outbins[0]
# integral = delbin*sum(n)
# err = np.sqrt(n)
# for i in range(len(n)):
#     if n[i] == 0:
#         n[i] = 0
#         err[i] = 1

# #n, outbins, patches  = plt.hist(dfsel.llc - dfsel.ll,bins=bins,histtype='step',lw=1,label=r)
# cbins = outbins[:-1] + delbin/2
# plt.errorbar(cbins,n/integral,yerr=err/integral, fmt='o')

# #for ext in [1,2,3,4,6,11,12]:
# #for ext in [4,6,11,12]:
# #for ext in [1,2,3]:
# #    dftemp = dfsel[dfsel.EXTID==ext]
# #    plt.hist(dftemp.ene1,bins=bins,histtype='step',lw=1,label='ext:'+str(ext))


# #x = np.arange(1,50,0.1) 
# print cbins
# #popt, pcov = curve_fit(lognorm, cbins, n)
# popt, pcov = curve_fit(expo, cbins, n/integral, sigma=err/integral)
# #print np.sqrt(n)

# print popt
# print pcov
# plt.plot(cbins,expo(cbins,popt[0],popt[1],popt[2]),lw=2)

# #plt.yscale('log')
# # mu =1
# # alpha = 3
# # for mu in np.arange(0,2,0.5):
# #     for sigma in np.arange(0.4,0.7,0.2):
# #         lognorm = 1000*(np.exp(-(np.log(x - alpha) - mu)**2 / (2 * sigma**2)) / ( (x-alpha)  * sigma * np.sqrt(2 * np.pi)))
# #         plt.plot(x,lognorm,label = 'simga= ' + str(sigma) + ' mu= ' +str(mu))
        
# plt.ylim(0,2)
# # plt.legend(loc=2)
# plt.show()







