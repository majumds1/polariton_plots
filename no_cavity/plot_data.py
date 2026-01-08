import numpy as np 
import os


# Load path to trajectories
file = open('path_log')
path = file.readlines()
n = len(path)                 # No. of trajectories
#l = 736                       # n_frames
l = int(np.loadtxt('n_steps'))
file.close()


# initialize numpy arrays for storig data
Norm_12 = np.zeros([n,l])
Norm_13 = np.zeros([n,l])
Norm_23 = np.zeros([n,l])
P1 = np.zeros([n,l])
P2 = np.zeros([n,l])
P3 = np.zeros([n,l])
d_grid = np.loadtxt("d_grid.dat")
Density_total = np.zeros([l,len(d_grid)])
#density_traj = np.zeros([l,len(d_grid)])
# loop to read in excitation energies and oscillator sterngths
for i in range(0,n):
        print ("Trajectory ",i)
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm12.dat'))
        Norm_12[i,:] = data[0:l]
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm13.dat'))
        Norm_13[i,:] = data[0:l]
        data = np.loadtxt(os.path.join(path[i].strip(),f'norm23.dat'))
        Norm_23[i,:] = data[0:l]
####################################################################################### 
        p_data = np.loadtxt(os.path.join(path[i].strip(),f'p.dat'))
        P1[i,:] = p_data[:,2][0:l] 
        P2[i,:] = p_data[:,3][0:l]
        P3[i,:] = p_data[:,4][0:l]
        print(p_data.shape) 
######################################################################################
        density_traj = np.loadtxt(os.path.join(path[i].strip(),f'density.dat'))
        Density_total = Density_total + density_traj


# Time array
t = p_data[:,0]




#Normalize density
for i in range(0,l):
    Density_total[i,:] = Density_total[i,:]/n
    print (np.sum(Density_total[i,:]))



# saving data to file
np.savetxt('Norm_12.dat', Norm_12, delimiter=',')
np.savetxt('Norm_13.dat', Norm_13, delimiter=',')
np.savetxt('Norm_23.dat', Norm_23, delimiter=',')
np.savetxt('P1.dat', P1, delimiter=',')
np.savetxt('P2.dat', P2, delimiter=',')
np.savetxt('P3.dat', P3, delimiter=',')
np.savetxt('time.dat',t)
np.savetxt('Density_data.dat', Density_total, delimiter=',')
