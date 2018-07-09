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
import glob 
import argparse

# ############################
# ##  argument parser       ##
# ############################
# parser = argparse.ArgumentParser()
# parser.add_argument("detname", type=str, nargs='?',default='EA7', choices=['EA7','EA61','GDC','GDL'], help="detector type")
# args = parser.parse_args()

# detname = args.detname
# #years = constant.years
# inputbkg = constant.cleanradio2 + '/bkg_' + detname + '*'
folder = '/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run1/cluster_sim/'
fname = 'sim100_0-1_001_1.root'
df = utils.readsimtree(folder+ fname)
plt.plot(df.centerx,df.centery)
plt.show()
#print df
