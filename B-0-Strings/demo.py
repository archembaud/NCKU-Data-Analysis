# This is a simple demonstration of simple strings in Python
firstName = "Matthew"
lastName = "Smith"

# Use an f-string to create a new string using the first and last name
wholeName = f"{firstName} {lastName}"

# Use "type" to inspect the type of variable (hint: these are strings)
print(f"firstName has type {type(firstName)}")
print(f"My name is {firstName} {lastName}")

# Use the split method, which produces a list of strings
result = wholeName.split(" ")
print(f"Split result = {result}")
print(f"result has type {type(result)}") # This will give you a list