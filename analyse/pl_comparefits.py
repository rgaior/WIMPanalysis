import numpy as np
import matplotlib.pyplot as plt

def expo(x,a,b,c):
    return a*(np.exp((x - b)/c))

folder = '/Users/gaior/DAMIC/code/data_analysis/out/dllfits/'
moriondruns = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2']
lastrun = ['run30ks4']
firstbin = -20
step =0.2
lastbin = 0
bins = np.arange(firstbin, lastbin, step)
cols = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
for lv,c in zip([-10,-8,-6],cols):
    fname = ''
    fname2 = ''
    for r in moriondruns:
        fname += r
    fname += str(lv)
    fname += '_'+str(firstbin)
    fit  = np.load(folder+fname +'.npy')
    for r in lastrun:
        fname2 += r
    fname2 += str(lv)
    fname2 += '_'+str(firstbin)
    fit2  = np.load(folder+fname2 +'.npy')
    plt.plot(bins,expo(bins,fit[0],fit[1],fit[2]),ls='--',c=c,label='moriond, fit range [' + str(firstbin)+';' +str(lv)+']')
    plt.plot(bins,expo(bins,fit2[0],fit2[1],fit2[2]),c=c, label='run30ks4, fit range [' + str(firstbin)+';' +str(lv)+']')
plt.legend()
plt.yscale('log')
plt.show()
