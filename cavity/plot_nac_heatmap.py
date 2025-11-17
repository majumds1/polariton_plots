import numpy as np
import matplotlib.pyplot as plt

# Load the 2D NAC data
data = np.loadtxt('Norm_12.dat',delimiter=",")
t=np.loadtxt('time.dat', delimiter=',')
n_traj=np.arange(0,10,1)
t=t/42.0

# plot heatmap
plt.pcolor(t,n_traj,data,cmap='turbo')
plt.colorbar(label='||NAC|| (a.u.)')
plt.clim(0,100)    # fix colorbar
plt.xlabel('Time (fs)')
plt.ylabel('Trajectory')
plt.title('Nonadiabatic Coupling Heatmap')
plt.tight_layout()
plt.savefig('Norm_12.png',dpi=400,bbox_inches='tight')	
