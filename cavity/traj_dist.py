import numpy as np
import matplotlib.pyplot as plt


#Function to compute distance between two atoms
def distance(A, B):
    d = (A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2
    d = d**0.5
    return(d)


#Load data
A=np.loadtxt('coord.dat')
n_atoms = int(np.loadtxt('n_atoms'))


m,n=A.shape
print('coord data shape=',m ,'*', n)
n_frames=int(m/n_atoms)
print('n_frames in coord data =',n_frames)
l=int(np.loadtxt('n_steps'))
print('number of steps to be considered =', l)
n_frames=l


#Extract distances
data=np.zeros([n_frames,n_atoms,3])
dA=np.zeros(n_frames)
dB=np.zeros(n_frames)
t=np.zeros(n_frames)
for i in range(0,n_frames):
    data[i,:,:]=A[i*n_atoms:(i+1)*n_atoms,:]
#    print(data[i,:,:])
    dA[i]=distance(data[i,0,:],data[i,9,:])
    dB[i]=distance(data[i,1,:],data[i,9,:])
    t[i]=i*0.1
#    print(data[i,1,:],data[i,5,:])
#    print('dA=',dA[i])
#    print('dB=',dB[i])


#labels
label = ['O','N','C','C','C','HA','H','H','H','HB']


#save data
d = dB - dA
np.savetxt('d.dat',d)
np.savetxt('t.dat',t)


#Plot
plt.plot(t,dA,'r-',label='O-H')
plt.plot(t,dB,'k',label='N-H')
plt.xlabel("Time (fs)")
plt.ylabel(r"distance($A^0$")
plt.legend()
plt.savefig('distance.png',dpi=400,bbox_inches='tight')
