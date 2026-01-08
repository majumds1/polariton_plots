import numpy as np
import matplotlib.pyplot as plt


#Load data
P1 = np.loadtxt('P1.dat',delimiter=",")
P2 = np.loadtxt('P2.dat',delimiter=",")
P3 = np.loadtxt('P3.dat',delimiter=",")
t = np.loadtxt('time.dat', delimiter=",")
t=t/42

#no. of traj and length of each traj
#n,l=P1.shape
file = open('path_log')
path=file.readlines()
n=len(path)
l=int(np.loadtxt('n_steps'))
file.close()


#calculate population
P1_total = np.zeros(l)
P2_total = np.zeros(l)
P3_total = np.zeros(l)
P1_std = np.zeros(l)
P2_std = np.zeros(l)
P3_std = np.zeros(l)
for j in range(0,l):
     P1_total[j] = np.sum(P1[:,j])/n
     P2_total[j] = np.sum(P2[:,j])/n
     P3_total[j] = np.sum(P3[:,j])/n
     P1_std[j] = np.std(P1[:, j])
     P2_std[j] = np.std(P2[:, j])
     P3_std[j] = np.std(P3[:, j])



#Plot
t=t[0:l]
#plt.title('Population Analysis')
plt.plot(t,P1_total,'r',label=r"$S_{1}$")
plt.fill_between(t, P1_total - P1_std/np.sqrt(n), P1_total + P1_std/np.sqrt(n), color='r', alpha=0.15)
plt.plot(t,P2_total,'g',label=r"$S_2$")
plt.fill_between(t, P2_total - P2_std/np.sqrt(n), P2_total + P2_std/np.sqrt(n), color='g', alpha=0.15)
plt.plot(t,P3_total,'k',label=r"$S_3$")
plt.fill_between(t, P3_total - P3_std/np.sqrt(n), P3_total + P3_std/np.sqrt(n), color='k', alpha=0.15)
plt.xlabel('Time (fs)',fontsize=15)
plt.ylabel('Population',fontsize=15)
plt.ylim(-0.1,1.1)
plt.legend(fontsize=14)
plt.savefig('population_proposal.png', dpi=400, bbox_inches='tight')
