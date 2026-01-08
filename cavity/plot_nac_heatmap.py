import numpy as np
import matplotlib.pyplot as plt

# Load the 2D NAC data
data = np.loadtxt('Norm_12.dat',delimiter=",")
t=np.loadtxt('time.dat', delimiter=',')
file = open('path_log')
path=file.readlines()
n=len(path)
l=int(np.loadtxt('n_steps'))
file.close()

t=t/42.0
n_traj=np.arange(0,n,1)

# plot heatmap
t=t[0:l]
plt.pcolor(t,n_traj,data,cmap='turbo')
plt.colorbar(label='||NAC|| (a.u.)')
plt.clim(0,100)    # fix colorbar
plt.xlabel('Time (fs)')
plt.ylabel('Trajectory')
plt.title('Nonadiabatic Coupling Heatmap')
plt.tight_layout()
plt.savefig('Norm_12.png',dpi=400,bbox_inches='tight')	
