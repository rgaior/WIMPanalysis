clusterfolder = '/Users/gaior/DAMIC/data/clusterfile/'
extensionlist = [1,2,3,4,6,11,12]
usedfolder = {'run100ks1':'/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run1/cluster_sim/','run100ks2':'/Users/gaior/DAMIC/data/damic1x100/cryoOFF_100000s-IntW800_OS_1x100_run2/cluster_sim/','run30ks1':'/Users/gaior/DAMIC/data/damic1x100/cryoOFF_30000s-IntW800_OS_1x100_run1/cluster_sim/'}

runid = {'run100ks1':[2473,2474,2475,2479,2480,2481,2482,2483,2484],'run100ks2':[2559,2560,2561,2562,2563,2564,2565,2566,2567,2568,2569,2570,2571,2572,2573,2577,2611,2612,2613,2614,2615,2616,2617,2618,2619],'run30ks1':[2623,2624,2625,2626,2627,2628,2629,2630,2631,2632,2633,2634,2635,2636,2637]}
runidind = {2473:1,2474:2,2475:3,2479:4,2480:5,2481:6,2482:7,2483:8,2484:9,2559:10,2560:11,2561:12,2562:13,2563:14,2564:15,2565:16,2566:17,2567:18,2568:19,2569:20,2570:21,2571:22,2572:23,2573:24,2577:25,2611:26,2612:27,2613:28,2614:29,2615:30,2616:31,2617:32,2618:33,2619:34}
#,'run30ks1':[2623,2624,2625,2626,2627,2628,2629,2630,2631,2632,2633,2634,2635,2636,2637]}
#runid = {'run100ks1':[2473,2474,2475,2479,2480,2481,2482,2483,2484],'run100ks2':[2559,2560,2561,2562,2563,2564,2565,2566,2567,2568,2569,2570,2571,2572,2573,2577,2611,2612,2613,2614,2615,2616,2617,2618,2619},'run30ks1':[2623,2624,2625,2626,2627,2628,2629,2630,2631,2632,2633,2634,2635,2636,2637]}

basefolder = '/Users/gaior/DAMIC/data/official/'
basefolder2 = '/Users/gaior/DAMIC/data/official2/'
basefolder4 = '/Users/gaior/DAMIC/data/official4/'
basefolderidm = '/Users/gaior/DAMIC/data/idm2018/'
basefolders = {1:'/Users/gaior/DAMIC/data/official/',2:'/Users/gaior/DAMIC/data/official2/',4:'/Users/gaior/DAMIC/data/official4/'} 
runname = {'run100ks1':'/cryoOFF_100000s-IntW800_OS_1x100_run1/','run100ks2':'/cryoOFF_100000s-IntW800_OS_1x100_run2/','run100ks3':'/cryoOFF_100000s-IntW800_OS_1x100_run3/','run30ks1':'/cryoOFF_30000s-IntW800_OS_1x100_run1/','run30ks2':'/cryoOFF_30000s-IntW800_OS_1x100_run2/','run30ks3':'/cryoOFF_30000s-IntW800_OS_1x100_run3/','run30ks4':'/cryoOFF_30000s-IntW800_OS_1x100_run4/','run30ks5':'/cryoOFF_30000s-IntW800_OS_1x100_run5/'}

#runinfo = {'run100ks1':(1e5,9),'run100ks2':(1e5,25),'run100ks3':(1e5,11),'run30ks1':(3e4,15), 'run30ks2':(3e4,102),'run30ks4':(3e4,33)}
runinfo = {'run100ks1':(1e5,9),'run100ks2':(1e5,25),'run100ks3':(1e5,11),'run30ks1':(3e4,15), 'run30ks2':(3e4,102), 'run30ks3':(3e4,150),'run30ks4':(3e4,88),'run30ks5':(3e4,40)}
badruns = {'run100ks1':[2482,2479],'run100ks2':[2577],'run100ks3':[],'run30ks1':[],'run30ks2':[2849,2927,2902],'run30ks3':[3003,3059,3112],'run30ks4':[3345.3346],'run30ks5':[]}

extid = [1,2,3,4,6,11,12]
#pklfolder = '/Users/gaior/DAMIC/data/damic1x100/'


outfolder = '/Users/gaior/DAMIC/code/data_analysis/out/'



#############################
## cuts definition ##########
#############################
positioncut = 'centery < 42 & centery > 2 & multirows == 0'
maskcut = 'is_masked == 0 & touchmask == 0 & success ==1'
llcut = 'll <100 & ll_14 < 90'
qmaxcut = 'qmax/(ene1*1000./3.77) > 0.2'
badimage = 'RUNID!=2482 &  RUNID!=2479 & RUNID!=2577 & RUNID!=2849 & RUNID!=2927 & RUNID!=2902 & RUNID !=3003 & RUNID!=3059 & RUNID!=3112 & RUNID!=3345 & RUNID!=3536'
basecuts = positioncut + ' & ' + maskcut + ' & ' +  llcut+ ' & ' +  qmaxcut + ' & ' +  badimage


