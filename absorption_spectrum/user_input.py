# Get user input
n_state = input("Enter number of excited states : ")


n_state = n_state.strip()


file = open("n_state", "w")
file.write(str(n_state) + "\n")
file.close()


print(f"Saved number of excited states: {n_state} in file 'n_state'")
