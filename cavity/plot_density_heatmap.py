import numpy as np
import matplotlib.pyplot as plt


# Load the 2D density data
data = np.loadtxt('Density_data.dat',delimiter=",")
t=np.loadtxt('time.dat', delimiter=',')
l=int(np.loadtxt('n_steps'))
t=t/42.0
d_grid=np.loadtxt('d_grid.dat')


#Plot
t=t[0:l]
plt.xlim(-1.6,1.6)
plt.pcolor(d_grid,t,data,cmap='terrain')
cbar=plt.colorbar()
cbar.set_label('Probability density', fontsize=14)
plt.clim(0,0.3)    # fix colorbar
plt.xlabel(r"DH - AH ($A^0$)",fontsize=15)
plt.ylabel('Time (fs)',fontsize=15)
#plt.title('Distance density heatmap')
plt.tight_layout()
plt.savefig('density_heatmap_proposal.png',dpi=400,bbox_inches='tight')
