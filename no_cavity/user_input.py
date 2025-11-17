# Get user input
n_atoms = input("Enter number of atoms in the molecule : ")
n_steps= input("Enter number of time steps you wish to consider : ")


n_atoms = n_atoms.strip()

n_steps = n_steps.strip()


file = open("n_atoms", "w")
file.write(str(n_atoms) + "\n")
file.close()


file = open("n_steps","w")
file.write(str(n_steps) + "\n")
file.close()



print(f"Saved number of atoms: {n_atoms} in file 'n_atoms'")
print(f"saved length of trajectory: {n_steps} in file 'n_steps'")
