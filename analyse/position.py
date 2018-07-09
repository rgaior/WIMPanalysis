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
from mpl_toolkits.axes_grid1 import make_axes_locatable


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
#runs = ['run100ks1','run100ks2','run100ks3','run30ks1','run30ks2','run30ks4']
runs = ['run30ks4']
dlllimit = 0
fname = 'data'
folder = constant.basefolders[4]
exemplepath = '/Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run2/pkl/data.pkl'
df = utils.initialize_dataframe(exemplepath)
df = utils.mergeruns(runs,folder,fname,df)
fidcut = 'sigma > 0.3 & sigma < 0.8'
dlllimits = [-23,-30,-40]
dlllimit = -30
pvcrashbefcut = 'RUNID < 3345'
pvcrashaftercut = 'RUNID  > 3345'
dllcut = ' ll - llc < ' + str(dlllimit) 

dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut )
#dfsel = df.query(constant.basecuts + ' & ' + dllcut + '&' + fidcut + ' & ' + pvcrashbefcut )
listofid = pd.unique(dfsel.RUNID)

xlow = 4000
xhigh = 9000
ylow = 1
yhigh = 44
xbinning = 100
ybinning = 1 
xedges = np.arange(xlow,xhigh,xbinning)
yedges = np.arange(ylow,yhigh,ybinning)
x = dfsel.centerx
y = dfsel.centery

H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
H = H.T


fig, ax2dhist = plt.subplots(figsize=(10, 8))

# the scatter plot:                                                             
#ax2dhist.scatter(x, y)
max = H.max()
print 'max = ', H
#the2dhist= ax2dhist.imshow(H,  cmap='RdBu_r',vmin=-max, vmax=max,interpolation='nearest', origin='low', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], aspect='auto')
the2dhist= ax2dhist.imshow(H,  cmap='Blues',vmin=0, vmax=max,interpolation='nearest', origin='low', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], aspect='auto')
# ax2dhist.set_aspect(1.)

# create new axes on the right and on the top of the current axes               
# The first argument of the new_vertical(new_horizontal) method is              
# the height (width) of the axes to be created in inches.                       
divider = make_axes_locatable(ax2dhist)
axHistx = divider.append_axes("top", 1.2, pad=0.1, sharex=ax2dhist)
axHisty = divider.append_axes("right", 1.2, pad=0.1, sharey=ax2dhist)

# make some labels invisible                                                                           
axHistx.xaxis.set_tick_params(labelbottom=False)
axHisty.yaxis.set_tick_params(labelleft=False)

# now determine nice limits by hand:                                                                   
binwidth = 1
#xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
#lim = (int(xymax/binwidth) + 1)*binwidth

xbins = np.arange(xlow,xhigh,xbinning)
ybins = np.arange(ylow,yhigh,ybinning)
axHistx.hist(x, bins=xbins,histtype='step',lw=1,color='k')
axHisty.hist(y, bins=ybins, histtype='step',lw=1,color='k', orientation='horizontal')

#ax2dhist.pcolormesh(x, y, Z, vmin=-1., vmax=1., cmap='RdBu_r')

# fig, axarr = plt.figure((2,2), figsize=(10, 10), )
# ax = fig.add_subplot(title='imshow: square bins')
# plt.imshow(
#fig.colorbar(, ax=ax)
ticks=np.linspace(0,max,max+1)
fig.colorbar(the2dhist, ax=ax2dhist,ticks=ticks)
ax2dhist.set_xlabel('X [re-binned per ' +str(xbinning) + ' pixels]' )
ax2dhist.set_ylabel('Y [pixel]')

plt.show()
