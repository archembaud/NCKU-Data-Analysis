# Simple FOR loop demo

N = 10
# The for loop will repeat itself 10 times
# starting from 0 and finishing at 9.
for i in range(N):
    print(f"This is step {i} out of {N-1}")

# We can also iterate over items in a list
names = ['Bruce Wayne', 'Clark Kent', 'Barry Allen']
for name in names:
    print(f"Looking at name = {name}")

# We can use the enumerate tool to provide an index as well
for index, name in enumerate(names):
    print(f"Looking at name = {name} with index = {index}")