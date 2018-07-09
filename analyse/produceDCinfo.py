import numpy as np
import pandas as pd
import sys
import os
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)


import utils
import constant
#file = '/Users/gaior/DAMIC/data/DC/DC_vs_runID_fullCCD.txt'
name = 'DC_vs_runID_2473_3576'
file = '/Users/gaior/DAMIC/data/DC/' + name +'.txt'

f = open(file,'r')

a_image = np.array([])
a_ext = np.array([])
a_DC = np.array([])
a_DCerr = np.array([])
a_ADUDC = np.array([])
a_ADUDCerr = np.array([])

lines = f.readlines()
extsize = 7
extlen = np.ones(extsize)
extblocksize= 7
imblocksize= extblocksize*extsize + 1

columns = ['image','ext','DC','DCerr','ADUDC','ADUDCerr','exposuretime','runname']
df = pd.DataFrame(columns=columns)

for i in range(len(lines) - imblocksize + 5):
#    print 'i = ' , i 
    l = lines[i]
 #   print l
    if 'IMAGE' in l:
        imblock = lines[i:i+imblocksize+1]        
        imm = imblock[0].split(" ")[4].split(",")[0]
        im = int(imm)
        ext = 0
        DC = 0
        DCerr = 0
        ADUDC = 0
        ADUDCerr = 0
        imblock = imblock[2:]
        for j in range(extsize):
            extblock = imblock[j*7:j*7+extblocksize]
            for k in range(len(extblock)):
                currl = extblock[k]
                ls = currl.split()
                if 'EXTENSION' in currl:
                    ls = currl.split()
                    ext = int(ls[-1])
                if 'Dark Current' in currl:
                    ls = extblock[k+1].split()
                    DC = float(ls[0])
                    DCerr = ls[-2]
                    DCerr = float(DCerr.split(',')[0])
                if 'ADU' in currl:
                    ls = currl.split()
                    ADUDC = float(ls[6])
                    ADUDCerr = ls[-2]
                    ADUDCerr = float(ADUDCerr.split(',')[0])
            exposuretime = utils.getexpofromrunid(im)[1]
            runname = utils.getexpofromrunid(im)[0]
            dftemp = pd.DataFrame([[im,ext,DC,DCerr,ADUDC,ADUDCerr,exposuretime,runname]],columns=columns)
            df = df.append(dftemp,ignore_index=True)
        


outfolder = '/Users/gaior/DAMIC/data/DC/'
df.to_pickle(outfolder  + name+ '.pkl')

