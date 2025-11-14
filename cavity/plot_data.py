import numpy as np 
import os


# Load path to trajectories
file = open('path_log')
path = file.readlines()
n = len(path)                 # No. of trajectories
l = 736                       # n_frames
file.close()


# initialize numpy arrays for storig data
Norm_01 = np.zeros([n,l])
Norm_02 = np.zeros([n,l])
Norm_03 = np.zeros([n,l])
Norm_12 = np.zeros([n,l])
Norm_13 = np.zeros([n,l])
Norm_23 = np.zeros([n,l])
P0 = np.zeros([n,l])
P1 = np.zeros([n,l])
P2 = np.zeros([n,l])
P3 = np.zeros([n,l])
# loop to read in excitation energies and oscillator sterngths
for i in range(0,n):
        print ("Trajectory ",i)
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm01.dat'))
        Norm_01[i,:] = data[0:l]
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm02.dat'))
        Norm_02[i,:] = data[0:l]
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm03.dat'))
        Norm_03[i,:] = data[0:l]
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm12.dat'))
        Norm_12[i,:] = data[0:l]
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm13.dat'))
        Norm_13[i,:] = data[0:l]
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm23.dat'))
        Norm_23[i,:] = data[0:l]
        p_data = np.loadtxt(os.path.join(path[i].strip(),f'p.dat'))
        P0[i,:] = p_data[:,2]
        P1[i,:] = p_data[:,3] 
        P2[i,:] = p_data[:,4]
        P3[i,:] = p_data[:,5]
        print(p_data.shape) 

# Time array
t=p_data[:,0]

# saving data to file
np.savetxt('Norm_01.dat', Norm_01, delimiter=',')
np.savetxt('Norm_02.dat', Norm_02, delimiter=',')
np.savetxt('Norm_03.dat', Norm_03, delimiter=',')
np.savetxt('Norm_12.dat', Norm_12, delimiter=',')
np.savetxt('Norm_13.dat', Norm_13, delimiter=',')
np.savetxt('Norm_23.dat', Norm_23, delimiter=',')
np.savetxt('P0.dat', P0, delimiter=',')
np.savetxt('P1.dat', P1, delimiter=',')
np.savetxt('P2.dat', P2, delimiter=',')
np.savetxt('P3.dat', P3, delimiter=',')
np.savetxt('time.dat',t)
