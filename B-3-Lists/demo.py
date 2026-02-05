# Create a simple list of names - start with an empty list
names = []

# Add a name to it
names.append('Bruce Wayne')
# Add another name to it
names.append('Clark Kent')

# Print the list
print(f"The names variable has type = {type(names)} and contains {names}")

# Now let's create another list and set it equal to this one
# Add this point, the names list contains both Bruce Wayne and Clark Kent
backup_names = names

# See how many items are in the list
print(f"The list contains {len(names)} names")

# Remove Clark Kent
names.remove('Clark Kent')

# Show the new list
print(f"The names list now contains {names}")

# Print the backup list - does it contain the values you expect?
print(f"The backup list contains {backup_names}")