import numpy as np
import matplotlib.pyplot as plt

# Create distance grid
def expand(distance):
    l = len(distance)
    d_grid = np.linspace(-3 ,3, 300)
    length = len(d_grid)
    P = np.zeros([l,length])
    for i in range(0, l):
        d = distance[i] - d_grid[0]
        index = 0
        for j in range(0, length):
            if (d > np.abs(distance[i] - d_grid[j])):
                index = j
                d = np.abs(distance[i] - d_grid[j])
#               print("*")
#        E[index] = Energy[i]
        P[i,index] = P[i,index] + 1
#        print(i)
    # Normalize
#    P_norm=P/l
#    print('Norm=',np.sum(P_norm))
#    print('size=',P.shape)
    return (d_grid, P)


dist=np.loadtxt('d.dat')
d1,P1=expand(dist)
#print(P1)
np.savetxt('d_grid.dat',d1)
np.savetxt('density.dat',P1)


# plot heatmap
t=np.loadtxt("t.dat")
plt.pcolor(d1,t,P1,cmap='viridis')
plt.colorbar(label='||Norm|| (a.u.)')
plt.clim(0,1)    # fix colorbar
plt.ylabel('Time (fs)')
plt.ylabel('DH-AH')
plt.title('Density Heatmap')
plt.tight_layout()
plt.savefig('density_heatmap.png',dpi=400,bbox_inches='tight')	
