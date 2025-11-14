# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 09:53:29 2025

@author: Sourav
"""

import numpy as np
import matplotlib.pyplot as plt


# No. of atoms 
n_atoms = 10


# Load trajectory NAC data
A = np.loadtxt('nac_extract.txt')
#A = np.transpose(A)
m, n = A.shape
n_frames=int(m/(n_atoms*3))


# Setup and store couplings between all possible states in a 3D numpy array
N = np.zeros([n_frames,n_atoms*3,3])
norm12=np.zeros(n_frames)
norm13=np.zeros(n_frames)
norm23=np.zeros(n_frames)
t=np.zeros(n_frames)
for i in range(0,n_frames):
     N[i,:,:] = A[i*n_atoms*3:(i+1)*n_atoms*3,:] 
     norm12[i]=np.linalg.norm(N[i,:,0])
#     print(N[i,:,2])
#     print('length=',len(N[i,:,2]))
     norm13[i]=np.linalg.norm(N[i,:,1])
     norm23[i]=np.linalg.norm(N[i,:,2])
     t[i]=i*0.1 
     

# Save data
np.savetxt('norm12.dat', norm12)
np.savetxt('norm13.dat', norm13)
np.savetxt('norm23.dat', norm23)
print('n_frames=',n_frames)
