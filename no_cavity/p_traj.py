import numpy as np
import matplotlib.pyplot as plt


Data=np.loadtxt("p.dat")

print (Data.shape)

t=Data[:,0]
P1=Data[:,2]
P2=Data[:,3]
P3=Data[:,4]


plt.plot(t,P1,'r',label=r"$S_{1}$")
plt.plot(t,P2,'g',label=r"$S_2$")
plt.plot(t,P3,'k',label=r"$S_3$")
plt.legend()
plt.xlabel('Time (fs)')
plt.ylabel('Population')
plt.savefig('population_traj.png', dpi=400)
