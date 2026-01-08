import numpy as np
import matplotlib.pyplot as plt


Data=np.loadtxt("e.dat")

print (Data.shape)

t=Data[:,0]
E1=Data[:,2]
E2_lower=Data[:,3]
E2_upper=Data[:,4]
E3=Data[:,5]
t = t/42.0



plt.plot(t,E1,'b',label=r"$S_{0}^{'}$")
plt.plot(t,E2_lower,'r',label=r"$S_{1}^{'}$")
plt.plot(t,E2_upper,'g',label=r"$S_2^{'}$")
#plt.plot(t,E3,'k',label=r"$S_3^{'}$")
plt.legend()
plt.xlabel('Time (fs)')
plt.ylabel('Population')
plt.savefig('energy_traj.png', dpi=400, bbox_inches="tight")

