import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import colors as mcolors
colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
extensionlist = [1,2,3,4,6,11,12]

f = '/Users/gaior/DAMIC/data/DC/DC.pkl'
fmoriond = '/Users/gaior/DAMIC/data/DC/DCMoriond.pkl'
f = '/Users/gaior/DAMIC/data/DC/DC_vs_runID_2473_3576.pkl'

dcmoriond = pd.read_pickle(fmoriond)
dc = pd.read_pickle(f)

#plt.plot(dcmoriond.image,dcmoriond.ADUDC,'o')
#plt.plot(dc.image,dc.ADUDC,'o')
cols= ['r','b','k','g',colors['skyblue'],colors['rosybrown'],colors['olive']] 
for ext,c in zip(extensionlist,cols):
    dct= dc[dc.ext==ext]
    plt.plot(dct.image,dct.ADUDC,'o',markerfacecolor='None',c=c,label='ext: '+str(ext))

plt.legend()
plt.yscale('log')
plt.show()
