import numpy as np
import matplotlib.pyplot as plt
import math
import argparse


# User arguments
parser = argparse.ArgumentParser(description="Compute and plot absorption spectrum.")
parser.add_argument('-w', "--linewidth", type=float,default=0.05, help="linewidth en eV")
parser.add_argument('-s', "--shift", type=float,default=0.0, help="red (-ve) or blue (+ve) shift in eV")
args = parser.parse_args()


# Load options
sigma = args.linewidth   # in eV
#ls = args.lineshape
shift=args.shift




# shift  
def apply_shift(A, shift):
    l = len(A)
    B = np.zeros(l)
    B = A + shift
    return (B)


# Create energy grid
def expand(Energy, Intensity,a,b):
    l = len(Energy)
    E = np.linspace(a, b, 100)
    length = len(E)
    I = np.zeros(length)
    for i in range(0, l):
        d = Energy[i] - E[0]
        index = 0
        for j in range(0, length):
            if (d > np.abs(Energy[i] - E[j])):
                index = j
                d = np.abs(Energy[i] - E[j])
#               print("*")
#        E[index] = Energy[i]
        I[index] = I[index] + Intensity[i]
        print(i)
    return (E, I)


# Load data
energy=np.loadtxt('e.dat')
osc=np.loadtxt('osc.dat')
l=len(energy)



# Lineshape function 
# everything in eV
E , I = expand(energy, osc,np.min(energy),np.max(energy))    # Energy grid
#sigma = sigma*0.0367     # eV to a.u.
Length = len(E)
G = np.zeros(Length)
E_grid = E
for i in range(0, Length):
        G  = G + I[i]*(1/(2*np.pi*sigma**2)**0.5)*np.exp(((-1)*(E_grid-E[i])**2)/(2*sigma**2))


# Final lineshape function
# convert energy to eV
#E = E*27.2114
# apply shift
E = apply_shift(E, shift)
G = G/(np.max(G))

#Plot
plt.xlim(np.min(E), np.max(E))
plt.ylim(0, 1.1*np.max(G))
plt.xlabel('Energy (eV)', fontsize=12.5)
plt.ylabel('Relative Intensity', fontsize=12.5)
plt.plot(E, G, 'purple', label="Absorption spectrum")
plt.legend()
plt.savefig('absorption_spectrum.png',dpi=400,bbox_inches='tight')
np.savetxt('energy_grid',E)
np.savetxt('intensity_grid',I)
