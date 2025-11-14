import numpy as np
import matplotlib.pyplot as plt


#Load data
P0 = np.loadtxt('P0.dat',delimiter=",")
P1 = np.loadtxt('P1.dat',delimiter=",")
P2 = np.loadtxt('P2.dat',delimiter=",")
P3 = np.loadtxt('P3.dat',delimiter=",")
t = np.loadtxt('time.dat', delimiter=",")
t=t/42

#no. of traj and length of each traj
n,l=P1.shape


#calculate population
P0_total = np.zeros(l)
P1_total = np.zeros(l)
P2_total = np.zeros(l)
P3_total = np.zeros(l)
for j in range(0,l):
     P0_total[j] = np.sum(P0[:,j])/n
     P1_total[j] = np.sum(P1[:,j])/n
     P2_total[j] = np.sum(P2[:,j])/n
     P3_total[j] = np.sum(P3[:,j])/n


#Plot
plt.title('Population Analysis')
plt.plot(t,P0_total,'purple',label=r"$S_{0}^{'}$")
plt.plot(t,P1_total,'r',label=r"$S_{1}^{'}$")
plt.plot(t,P2_total,'g',label=r"$S_{2}^{'}$")
plt.plot(t,P3_total,'k',label=r"$S_{3}^{'}$")
plt.xlabel('Time (fs)')
plt.ylabel('Population')
plt.ylim(0,1.1)
plt.legend()
plt.savefig('population.png', dpi=400, bbox_inches='tight')
