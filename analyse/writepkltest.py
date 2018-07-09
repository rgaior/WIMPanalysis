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

############################
##  argument parser       ##
############################
parser = argparse.ArgumentParser()
parser.add_argument("folder", type=str, nargs='?',default='', help="root file folder")
parser.add_argument("datatype", type=str, nargs='?',choices=['sim', 'data', 'blank'] ,help="type of data tag")
parser.add_argument("code", type=str, nargs='?',choices=['a', 'p', 'k'] ,help="for alvaro, pitam, karthik")
args = parser.parse_args()
datatype = args.datatype
folder = args.folder
code = args.code

infolders = {'sim':folder + '/rootsc/','blank':folder + '/rootbc/','data':folder + '/rootc/'}
fbase = '*.root*'

files = glob.glob(infolders[datatype] + fbase)    
first = True
outfolder = folder + '/pkl/'
outname = datatype
for f in files:
    exposure = utils.getexpofromfilename(f)

#     print 'input  = ' , f 
#     print ' outname = ' , outname 
#     print 'output = ', outfolder  + outname
#     if first == True:
#         #        dfall = utils.readsimtreeori(f,type)
#         if code == 'a':
#             dfall = utils.readsimtree(f,type,exposure)
#         elif code == 'p':
#             dfall = utils.readsimtreeP(f,type,exposure)

# #        dfall = utils.checksplit(dfall)

# #########################
#         #        df = utils.readsimtreeori(f,type)
# #        df = utils.readsimtree(f,type)
# #        df = utils.checksplit(df)
# #        df.to_pickle(outfolder  + outname)
# #############################

#         # simcluster trees
#         dfsimall = utils.readsimclustertree(f,type,exposure)
# #        dfsim = utils.readsimclustertree(f,type)
# #        dfsim.to_pickle(outfolder  + '/simc_' + outname[1:])
#         first = False
#     else:
#         #        df = utils.readsimtreeori(f,type)
#         if code == 'a':
#             df = utils.readsimtree(f,type,exposure)
#         elif code == 'p':
#             df = utils.readsimtreeP(f,type,exposure)

# #a#        df = utils.checksplit(df)


# #        df.to_pickle(outfolder  + outname)
#         dfall = dfall.append(df)
#         #        sim clusters
#         dfsim = utils.readsimclustertree(f,type)
#         dfsimall = dfsimall.append(dfsim)
# #        dfsimname =  outfolder  + '/simc_' + outname[1:]
# #        dfsim.to_pickle(dfsimname)
#         # write a dfall with some basic conditions:
#         # multir == 0 & is_masked == 0 & touchmask  == 0 &  centery < 44 & sime !=0
        


# if code == 'a':
#     dfgood = dfall[(dfall.multir==0) & (dfall.touchmask == 0) & (dfall.centery < 44 )]       
# elif code == 'p':
#     dfgood = dfall[(dfall.multir==0) & (dfall.touchmask == 0) & (dfall.centery < 44 )]       
# dfall.to_pickle(outfolder + outname +'.pkl')                                                                                          
# dfgood.to_pickle(outfolder + outname +'sel.pkl')                                                                                      

# dfsimgood = dfsimall[(dfsimall.touchmask == 0)] 
# dfsimall.to_pickle(outfolder + outname +'_s.pkl')                                                                                     
# dfsimgood.to_pickle(outfolder + outname + 'sel_s.pkl')   

# # dfgood = dfall[(dfall.multir==0) & (dfall.is_masked == 0) & (dfall.touchmask == 0) & (dfall.centery < 44 ) & (dfall.sime != 0)]
# # dfall.to_pickle(outfolder + './simall.pkl')
# # dfgood.to_pickle(outfolder + './simgood.pkl')

# # dfsimgood = dfsimall[(dfsimall.is_masked == 0) & (dfsimall.touchmask == 0)]
# # dfsimall.to_pickle(outfolder + './simc_simall.pkl')
# # dfsimgood.to_pickle(outfolder + './simc_simgood.pkl')


# #print df
