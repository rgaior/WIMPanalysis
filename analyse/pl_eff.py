import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


efficiencyfile ='/Users/gaior/DAMIC/data/efficiency/extracted.pkl'
eff = pd.read_pickle(efficiencyfile)

plt.plot(eff.e,eff.eff)
plt.ylabel('efficiency')
plt.xlabel('energy [keV]')
plt.show()

