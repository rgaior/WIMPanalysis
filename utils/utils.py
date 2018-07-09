import numpy as np
import ROOT as R
import pandas as pd
import glob 
import constant
def readsimtree(simname, exposuretime, typeofdata=None):
    f = R.TFile(simname)
    t = f.Get("clusters")
#    v= f.Get("v")
#    print 'v = ' , v[1] 
#fout << "RUNID:EXTID:efact:nvalidpix:cid:centerx:centery:linlength:is_masked:qguess:sguess:oguessg:oguessc:llg:llc:success:ll:meanx:meanx_err:sigma:sigma_err:efit:qbase:npix:npix4:\
#ene1:ene_integ:chi2g:chi2c:touchmask:sime:simz:simx:simy:simsigma" << std::endl;

    columns = ['RUNID','EXTID','efact','nvalidpix','cid','centerx','centery','linlength','is_masked','qguess','sguess','oguessg','oguessc','llg','llc','success','ll','meanx','meanx_err','sigma','sigma_err','efit','qbase','npix','npix4','ene1','ene_integ','chi2g','chi2c','touchmask','sime','simz','simx','simy','simn','simdistx','simdisty','multirows','type','status','ll_enlarg','llc_enlarg','ll_14','llc_14','gchi2','cchi2','qmax','qdelta_dx','qdelta_sx','is_premasked','exposuretime']        
    df = pd.DataFrame(columns=columns)
    for event in t:
        RUNID =  event.RUNID
        EXTID =  event.EXTID
        efact = event.efact
        nvalidpix = event.nvalidpix
        cid = event.cid
        centerx = event.centerx
        centery = event.centery
        linlength = event.linlength
        is_masked = event.is_masked
        qguess = event.qguess
        sguess = event.sguess
        oguessg = event.oguessg
        oguessc = event.oguessc
        llg = event.llg
        llc = event.llc
        touchmask = event.touchmask
        sime = event.sime
        simz = event.simz
        simy = event.simy
        simx = event.simx
        success = event.success
        ll = event.ll
        meanx = event.meanx
        meanx_err = event.meanx_err
        sigma = event.sigma
        sigma_err = event.sigma_err
        efit = event.efit
        qbase = event.qbase
        npix = event.npix
        npix4 = event.npix4
        ene1 = event.ene1
        ene_integ = event.ene_integ
        chi2g = event.chi2g
        chi2c = event.chi2c
        simn = event.simn
#        simp0 = event.simp0
#        simmeanx = event.simmeanx
        simdistx = event.simdistx
        simdisty = event.simdisty
        multirows = event.multirows
        type = typeofdata
        status = event.status
        ll_enlarg = event.ll_enlarg
        llc_enlarg = event.llc_enlarg
        ll_14 = event.ll_14
        llc_14 = event.llc_14
        gchi2 = event.gchi2
        cchi2 = event.cchi2
        qmax = event.qmax
        qdelta_dx = event.qdelta_dx
        qdelta_sx = event.qdelta_sx
        is_premasked = event.is_premasked
        exposuretime=exposuretime
#    columns = ['RUNID','EXTID','efact','nvalidpix','cid','centerx','centery','linlength','is_masked','qguess','sguess','oguessg','oguessc','llg','llc','success','ll','meanx','meanx_err','sigma','sigma_err','efit','qbase','npix','npix4','ene1','ene_integ','chi2g','chi2c','touchmask','sime','simz','simx','simy','simsigma','simp0','simmeanx','type']        

        dftemp = pd.DataFrame([[RUNID,EXTID,efact,nvalidpix,cid,centerx,centery,linlength,is_masked,qguess,sguess,oguessg,oguessc,llg,llc,success,ll,meanx,meanx_err,sigma,sigma_err,efit,qbase,npix,npix4,ene1,ene_integ,chi2g,chi2c,touchmask,sime,simz,simx,simy,simn,simdistx,simdisty,multirows,type,status,ll_enlarg,llc_enlarg,ll_14,llc_14,gchi2,cchi2,qmax,qdelta_dx,qdelta_sx,is_premasked,exposuretime]], columns=columns)
        df = df.append(dftemp,ignore_index=True)

    return df


def readsimclustertree(simname, exposuretime, typeofdata=None):
    f = R.TFile(simname)
    t = f.Get("simclusters")
#    v= f.Get("v")
#    print 'v = ' , v[1] 
#fout << "RUNID:EXTID:efact:nvalidpix:cid:centerx:centery:linlength:is_masked:qguess:sguess:oguessg:oguessc:llg:llc:success:ll:meanx:meanx_err:sigma:sigma_err:efit:qbase:npix:npix4:\
#ene1:ene_integ:chi2g:chi2c:touchmask:sime:simz:simx:simy:simsigma" << std::endl;
#  sime            = 0.356232
#  simx            = 7881.81
#  simy            = 0.485228
#  simz            = 0.0389468
#  simn            = 42
#  assigned        = -2
#  meanxp          = 7881.96
#  efit            = 0.329152
#  ene1            = 0.35407
#  sigma           = 0.570782
#  qbase           = 0.00557316
#  success         = 1
#  is_masked       = 1
#  ll              = 29.2468
#  llc             = 349.697
#  RUNID           = 2473
#  EXTID           = 1
#  touchmask       = 0
#  simdist         = 2572.45

    columns = ['RUNID','EXTID','is_masked','llc','success','ll','meanxp','sigma','efit','qbase','ene1','touchmask','sime','simz','simx','simy','simn','simdistx','simdisty','assigned','type','exposuretime']        
    df = pd.DataFrame(columns=columns)
    for event in t:
        RUNID =  event.RUNID
        EXTID =  event.EXTID
        is_masked = event.is_masked
        llc = event.llc
        touchmask = event.touchmask
        sime = event.sime
        simz = event.simz
        simy = event.simy
        simx = event.simx
        simn = event.simn
        success = event.success
        ll = event.ll
        meanxp = event.meanxp
        sigma = event.sigma
        qbase = event.qbase
        ene1 = event.ene1
        efit = event.efit
        assigned = event.assigned
        simdistx = event.simdistx
        simdisty = event.simdisty
        type = typeofdata
        exposuretime = exposuretime
#    columns = ['RUNID','EXTID','efact','nvalidpix','cid','centerx','centery','linlength','is_masked','qguess','sguess','oguessg','oguessc','llg','llc','success','ll','meanx','meanx_err','sigma','sigma_err','efit','qbase','npix','npix4','ene1','ene_integ','chi2g','chi2c','touchmask','sime','simz','simx','simy','simsigma','simp0','simmeanx','type']        

        dftemp = pd.DataFrame([[RUNID,EXTID,is_masked,llc,success,ll,meanxp,sigma,efit,qbase,ene1,touchmask,sime,simz,simx,simy,simn,simdistx,simdisty,assigned,type,exposuretime]], columns=columns)
        df = df.append(dftemp,ignore_index=True)

    return df


def readsimtreeori(simname, typeofdata=None):
    f = R.TFile(simname)
    t = f.Get("clusters")
#    v= f.Get("v")
#    print 'v = ' , v[1] 
#fout << "RUNID:EXTID:efact:nvalidpix:cid:centerx:centery:linlength:is_masked:qguess:sguess:oguessg:oguessc:llg:llc:success:ll:meanx:meanx_err:sigma:sigma_err:efit:qbase:npix:npix4:\
#ene1:ene_integ:chi2g:chi2c:touchmask:sime:simz:simx:simy:simsigma" << std::endl;

    columns = ['RUNID','EXTID','efact','nvalidpix','cid','centerx','centery','linlength','is_masked','qguess','sguess','oguessg','oguessc','llg','llc','success','ll','meanx','meanx_err','sigma','sigma_err','efit','qbase','npix','npix4','ene1','ene_integ','chi2g','chi2c','touchmask','sime','simz','simx','simy','type']        
    df = pd.DataFrame(columns=columns)
    for event in t:
        RUNID =  event.RUNID
        EXTID =  event.EXTID
        efact = event.efact
        nvalidpix = event.nvalidpix
        cid = event.cid
        centerx = event.centerx
        centery = event.centery
        linlength = event.linlength
        is_masked = event.is_masked
        qguess = event.qguess
        sguess = event.sguess
        oguessg = event.oguessg
        oguessc = event.oguessc
        llg = event.llg
        llc = event.llc
        touchmask = event.touchmask
        sime = event.sime
        simz = event.simz
        simy = event.simy
        simx = event.simx
        success = event.success
        ll = event.ll
        meanx = event.meanx
        meanx_err = event.meanx_err
        sigma = event.sigma
        sigma_err = event.sigma_err
        efit = event.efit
        qbase = event.qbase
        npix = event.npix
        npix4 = event.npix4
        ene1 = event.ene1
        ene_integ = event.ene_integ
        chi2g = event.chi2g
        chi2c = event.chi2c
        type = typeofdata

#    columns = ['RUNID','EXTID','efact','nvalidpix','cid','centerx','centery','linlength','is_masked','qguess','sguess','oguessg','oguessc','llg','llc','success','ll','meanx','meanx_err','sigma','sigma_err','efit','qbase','npix','npix4','ene1','ene_integ','chi2g','chi2c','touchmask','sime','simz','simx','simy','simsigma','simp0','simmeanx','type']        

        dftemp = pd.DataFrame([[RUNID,EXTID,efact,nvalidpix,cid,centerx,centery,linlength,is_masked,qguess,sguess,oguessg,oguessc,llg,llc,success,ll,meanx,meanx_err,sigma,sigma_err,efit,qbase,npix,npix4,ene1,ene_integ,chi2g,chi2c,touchmask,sime,simz,simx,simy,type]], columns=columns)
        df = df.append(dftemp,ignore_index=True)

    return df




def readsimtreeP(simname, typeofdata=None):
    f = R.TFile(simname)
    t = f.Get("clusters")
#    v= f.Get("v")
#    print 'v = ' , v[1] 
#fout << "RUNID:EXTID:efact:nvalidpix:cid:centerx:centery:linlength:is_masked:qguess:sguess:oguessg:oguessc:llg:llc:success:ll:meanx:meanx_err:sigma:sigma_err:efit:qbase:npix:npix4:\
#ene1:ene_integ:chi2g:chi2c:touchmask:sime:simz:simx:simy:simsigma" << std::endl;

    columns = ['RUNID','EXTID','EXPSTART','EXPTIME','efact','nvalidpix','cid','centerx','centery','linlength','success','status','llc','llc','ll','ll_enlarg','llc_enlarg','ll_14','llc_14','meanx','meanx_err','sigma','sigma_err','efit','qbase','npix','npix4','gchi2','cchi2','ene1','ene_integ','chi2g','chi2c','qmax','qdelta_dx','qdelta_sx','touchmask','is_premasked','sime','simz','simx','simy','simn','simdistx','simdisty','type']        
    df = pd.DataFrame(columns=columns)
    for event in t:
        RUNID =  event.RUNID
        EXTID =  event.EXTID
        EXPSTART =  event.EXPSTART
        EXPTIME =  event.EXPTIME
        efact = event.efact
        nvalidpix = event.nvalidpix
        cid = event.cid
        centerx = event.centerx
        centery = event.centery
        linlength = event.linlength
        success = event.success
        status = event.status
        #to be mod llc -->llg
        llc = event.llc
        llc = event.llc
        ll = event.ll
        ll_enlarg = event.ll_enlarg
        llc_enlarg = event.llc_enlarg
        ll_14 = event.ll_14
        llc_14 = event.llc_14
        meanx = event.meanx
        meanx_err = event.meanx_err
        sigma = event.sigma
        sigma_err = event.sigma_err
        efit = event.efit
        qbase = event.qbase
        npix = event.npix
        npix4 = event.npix4
        gchi2 = event.gchi2
        cchi2 = event.cchi2
        ene1 = event.ene1
        ene_integ = event.ene_integ
        chi2g = event.chi2g
        chi2c = event.chi2c
        qmax = event.qmax
        qdelta_dx = event.qdelta_dx
        qdelta_sx = event.qdelta_sx
        touchmask = event.touchmask
        is_premasked = event.is_premasked
        sime = event.sime
        simz = event.simz
        simy = event.simy
        simx = event.simx
        simn = event.simn
        simdistx = event.simdistx
        simdisty = event.simdisty
        type = typeofdata

#    columns = ['RUNID','EXTID','efact','nvalidpix','cid','centerx','centery','linlength','is_masked','qguess','sguess','oguessg','oguessc','llg','llc','success','ll','meanx','meanx_err','sigma','sigma_err','efit','qbase','npix','npix4','ene1','ene_integ','chi2g','chi2c','touchmask','sime','simz','simx','simy','simsigma','simp0','simmeanx','type']        

        dftemp = pd.DataFrame([[RUNID,EXTID,EXPSTART,EXPTIME,efact,nvalidpix,cid,centerx,centery,linlength,success,status,llc,llc,ll,ll_enlarg,llc_enlarg,ll_14,llc_14,meanx,meanx_err,sigma,sigma_err,efit,qbase,npix,npix4,gchi2,cchi2,ene1,ene_integ,chi2g,chi2c,qmax,qdelta_dx,qdelta_sx,touchmask,is_premasked,sime,simz,simx,simy,simn,simdistx,simdisty,type]], columns=columns)
        df = df.append(dftemp,ignore_index=True)

    return df



def getimagepart(image,centralbin_x,centralbin_y,delta_x,delta_y):
    array_x = range(centralbin_x - delta_x, centralbin_x + delta_x + 1)
    array_y = range(centralbin_y - delta_y, centralbin_y + delta_y + 1)
#    print array_y
    imtoshow = np.ndarray(shape=(len(array_x),len(array_y)))
    count = 0
    for x in array_x:
        imarray = np.array([])
        for y in array_y:
            imarray = np.append(imarray,image.GetBinContent(x + 1 ,y + 1))
        imtoshow[count] = imarray
        count+=1
    return [array_x,array_y,imtoshow.T]

def getimage(image):
    array_x = range(0,4200)
    array_y = range(1,43)
    imtoshow = np.ndarray(shape=(len(array_x),len(array_y)))
    count = 0
    for x in array_x:
        imarray = np.array([])
        for y in array_y:
            imarray = np.append(imarray,image.GetBinContent(x + 1 ,y + 1))
        imtoshow[count] = imarray
        count+=1
    return [array_x,array_y,imtoshow.T]


# compares df1 with df2 according a criteria given as a string.
# if no criterion is given a position criterion is applied: diff in centerx  == 0 & diff in centery == 0
# returns two dataframes
def compareDF(df1, df2, listofrun, criteria=None):
    dfcomm = pd.DataFrame(columns=df1.columns)
    dfremainder = pd.DataFrame(columns=df1.columns)
#    for rid in constant.runid[run]:
    extids = [1,2,3,4,6,11,12]
    for rid in listofrun:
        for eid in extids:
            df1test = df1[ (df1.RUNID==rid) & (df1.EXTID == eid) ]
            df2test = df2[ (df2.RUNID==rid) & (df2.EXTID == eid) ]            

            df1size = df1test.shape[0]
            df2size = df2test.shape[0]
            for idf1 in range(df1size):
                df1temp = df1test.iloc[idf1]
                com = False
                for idf2 in range(df2size):
                    df2temp = df2test.iloc[idf2]
                    if criteria == None:
                        if (df1temp.centerx == df2temp.centerx) and (df1temp.centery == df2temp.centery) :                
#                    print 'found common frame ' , df1temp.centerx,  ' ', df2temp.centerx, df1temp.centery,  ' ', df2temp.centery 
                            com = True
                    else:
                        for c in criteria:                        
                            if (df1temp[c] == df2temp[c]):
                                com = com&True                        
                            else:
                                # if one of the criterion is not fulfilled
                                com = com&False                                            
                if com == True:
            #                print ' len(df1temp) = ' , df1temp
                    dfcomm = dfcomm.append(df1temp)                
                elif com==False:       
                    dfremainder = dfremainder.append(df1temp)                
#    print 'len(dfcomm) = ', len(dfcomm)
#    print 'len(dfremainder) ' , len(dfremainder)
    return [dfcomm, dfremainder]



def checksplit(dfref):
    # loop over the DF
    allsize = dfref.shape[0]
    a_multir = np.zeros(allsize)
    for iref in range(allsize):
        dftemp = dfref.iloc[iref]
    # loop over the remainder of the DF
        yref = dftemp['centery']
        for iremainder in range(iref+1, allsize):
            dfcomp = dfref.iloc[iremainder]
            ycomp = dfcomp['centery']
            if np.abs(ycomp - yref) > 3:
                break
#            print 'iref = ' , iref , 'iremainder = ' , iremainder, ' ycomp = ' , ycomp , ' yref = ' , yref 
            if ( (dftemp['EXTID'] == dfcomp['EXTID']) and (dftemp['RUNID'] == dfcomp['RUNID']) and ( np.abs(dftemp['meanx'] - dfcomp['meanx']) < 3) and ( np.abs(dftemp['centery'] - dfcomp['centery']) < 1.3) ):
#            if ( (dftemp['EXTID'] == dfcomp['EXTID']) and (dftemp['RUNID'] == dfcomp['RUNID']) and ( np.abs(dftemp['centerx'] - dfcomp['centerx']) < 3) and ( np.abs(dftemp['centery'] - dfcomp['centery']) < 2) ):
#                print ' dftemp[centerx]  = ' , dftemp['centerx'] , ' dfcom[centerx]  = ' , dfcomp['centerx'] , ' dftemp[centery]  = ' , dftemp['centery'] , ' dfcom[centery]  = ' , dfcomp['centery'] 
                a_multir[iref] = 1
                a_multir[iremainder] = 1
#    print 'nr of multir = ' , np.count_nonzero(a_multir) 
    dfnew = dfref.copy()
    dfnew = dfnew.assign(multir=pd.Series(a_multir).values)
    return dfnew




                

def getlistofimage(path):
    listoffile = glob.glob(path+ '*_11.root')
    listofim = []
    for f in listoffile:
        im = f[ f[:f.rfind('_')].rfind('_')+1:f.rfind('_')]
        print listofim.append(int(im))                
    return listofim


def mergeruns(listofrun,folder,fname,dfall):
    for r in listofrun:
        folder2 = folder + constant.runname[r] + '/pkl/'
        print folder2
        df = pd.read_pickle(folder2 + fname + '.pkl')
        dfall = dfall.append(df)
    return dfall

        
def initialize_dataframe(path):
    dfex = pd.read_pickle(path)
    return pd.DataFrame(columns=dfex.columns)



#def fitDLL(dlldata,function,)

#def get


def writebrowsercommand(df, outname, run, iteration):
    fout = open(outname,'w')
    exptime = '30000' if ('30' in run) else '100000'
    for index, row in df.iterrows():
        path = constant.basefolders[iteration] + constant.runname[run] + 'rootc/d44_snolab_Int-800_Exp-' +  exptime + '_' + str(int(row['RUNID'])) + '_' + str(int(row['EXTID'])) + '.root'
#EventBrowser /Users/gaior/DAMIC/data/official4/cryoOFF_100000s-IntW800_OS_1x100_run1/rootc/d44_snolab_Int-800_Exp-100000_2475_6.root
        fout.write('EventBrowser' + ' -c ' + str(int(row['cid'])) + ' ' + path + '\n')

 
def produceimagecut(dfdc,dclimvalue):
    imcuts = []
    count = 0
    for index, row in dfdc.iterrows():
        if row.ADUDC > dclimvalue:
            if count ==0:
                imcut = ''
                imcut += ' ( RUNID != '+ str(row.image) + ' | EXTID != ' +str(row.ext) + ') ' 
            else:
                imcut += ' & ( RUNID != '+ str(row.image) + ' | EXTID != ' +str(row.ext) + ') ' 
            count +=1            
            if count==20:
                imcuts.append(imcut)
                count=0
                
    return imcuts


def getexpofromfilename(f):
    f = f[f.rfind('/'):]
    f = f[f.rfind('Exp-')+4:]
    exp = f[:f.find('_')]
    return int(exp)
    
def getexpofromrunid(runid):
    run = ''
    if ( (runid >= 2473) & (runid <= 2484) ):
        run = 'run100ks1'
    if ( (runid >= 2559)  & (runid <= 2619)):
        run = 'run100ks2'
    if ( (runid >= 2829) & (runid <= 2839)):
        run = 'run100ks3'
    if ( (runid >= 2623) & (runid <= 2637)):
        run = 'run30ks1'
    if ( (runid >= 2843) & (runid <= 2951)):
        run = 'run30ks2'
    if ( (runid >= 3003) & (runid <= 3162)):
        run = 'run30ks3'
    if ( (runid >= 3203) & (runid <= 3487)):
        run = 'run30ks4'
    if ( (runid >= 3536) & (runid <= 3576)):
        run = 'run30ks5'
    print 'runid = ' , runid, 'run = ', run
    expo = constant.runinfo[run][0]
    print 'exop = ',  expo
    return [run,expo]


def getrunexposure(runname,extnr):
    expo = constant.runinfo[runname][0]
    totnrofruns = constant.runinfo[runname][1]
    nrofbadruns = len(constant.badruns[runname])
    
    runexpo = (totnrofruns - nrofbadruns)*extnr*expo
    return runexpo


def removedexpofromDC(runname,dfdc, dclimvalue):
    removedexpo = 0
    for index, row in dfdc.iterrows():
        if row.runname != runname:
            continue
        if row.ADUDC > dclimvalue:
            removedexpo += row.exposuretime
    print ' runname = ' , runname , ' exporempove ', removedexpo
    return removedexpo

def removedexpofromDCperext(runname,dfdc, dclimvalue):
    removedexpo = 0
    removedexpoperext = {1:0, 2:0, 3:0, 4:0, 6:0, 11:0, 12:0}
    for index, row in dfdc.iterrows():
        if row.runname != runname:
            continue
        if row.ADUDC > dclimvalue:
            removedexpoperext[row.ext] += row.exposuretime
    print ' runname = ' , runname , ' exporempove ', removedexpoperext
    return removedexpoperext


    
    
#return the error of the 
def gethisterror(values, weights, bins):
    a_error = np.array([])
    binsindex = np.digitize(values,bins)

    # access elements for first bin                                                                                                       
    for index in range(1,len(bins)):
        bin_ws = weights[np.where(binsindex==index)[0]]
    # error of fist bin                                                                                                               
        error = np.sqrt(np.sum(bin_ws**2.))
#        print error
        a_error =np.append(a_error,error)
        
    return a_error
