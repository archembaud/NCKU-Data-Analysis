# Create a simple dict
# This looks a lot like a JSON
superhero = {
    'firstName': 'Bruce',
    'lastName': 'Wayne',
    'superheroName': '',
    'age': 41
}

# Use an f-string to show what is in this object
print(f"The contents of superhero are: {superhero}")

# Now to use the dict as intended - using its keys
# Let's modify the superheroName
superhero['superheroName'] = 'Batman'
# And let's update the age
superhero['age'] = 42

# Show the updated contents using an f-string
print(f"Updated contents of superhero are: {superhero}")

# Add a new key-value pair
superhero['power'] = 'money'

# And use these keys for reading
print(f"{superhero['firstName']} {superhero['lastName']} is actually {superhero['superheroName']}, and their superpower is {superhero['power']}")