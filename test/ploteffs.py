import numpy as np
import matplotlib.pyplot as plt

folder = '/Users/gaior/DAMIC/code/data_analysis/out/'
f1 = folder + 'out1_1.npz'
eff1 = np.load(f1)
f2 = folder + 'out2_1.npz'
eff2 = np.load(f2)
f3 = folder + 'out3_1.npz'
eff3 = np.load(f3)
f4 = folder + 'out1_2.npz'
eff4 = np.load(f4)
f5 = folder + 'out2_2.npz'
eff5 = np.load(f5)
f6 = folder + 'out3_2.npz'
eff6 = np.load(f6)
f7 = folder + 'out1_3.npz'
eff7 = np.load(f7)
f8 = folder + 'out2_3.npz'
eff8 = np.load(f8)
f9 = folder + 'out3_3.npz'
eff9 = np.load(f9)


plt.errorbar(eff3['e'],eff3['eff'],yerr=eff3['err'],fmt='o',label='old touchmask')
plt.errorbar(eff6['e'],eff6['eff'],yerr=eff6['err'],fmt='s',label='new touchmask')
plt.errorbar(eff9['e'],eff9['eff'],yerr=eff9['err'],fmt='v',label='new touchmask + simdisty < 2')
plt.grid()
plt.legend()
plt.xlabel('energy [keV]')
plt.ylabel('efficiency')
plt.show()
