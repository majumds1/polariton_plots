import numpy as np
import matplotlib.pyplot as plt


N01=np.loadtxt("norm01.dat")
N12=np.loadtxt("norm12.dat")
N23=np.loadtxt("norm23.dat")
t=np.loadtxt("time.dat")
t=t/42.0




#print('max_23=',np.max(N23))
#print('arg max=',np.argmax(N23))
plt.plot(t, N01, 'b', label="$S_1^{'} - S_2^{'}$")
plt.plot(t, N12, 'r',label="$S_2^{'} - S_2^{''}$")
#plt.plot(t, N23, 'g',label="$S_2^{''} -  S_3^{'}$")
plt.xlabel('Time (fs)')
plt.ylabel('||NAC|| (a.u.)')
plt.legend()
plt.savefig('nac_compare.png',dpi=400,bbox_inches="tight")
