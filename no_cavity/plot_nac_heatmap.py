import numpy as np
import matplotlib.pyplot as plt

# Load the 2D NAC data
data = np.loadtxt('Norm_23.dat',delimiter=",")


# Plot heatmap
plt.imshow(
    data,
    cmap='turbo',
    aspect='auto',
    origin='lower',
    vmin=0.0,        
    vmax=100       
)
plt.imshow(data, cmap='turbo', aspect='auto',origin='lower')
plt.colorbar(label='||NAC|| (a.u.)')
plt.xlabel('Time (fs)')
plt.ylabel('Trajectory')
plt.title('Nonadiabatic Coupling Heatmap')
plt.tight_layout()
plt.savefig('Norm_23.png',dpi=400,bbox_inches='tight')	
