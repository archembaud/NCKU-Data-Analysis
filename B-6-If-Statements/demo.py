# Demonstration of if statements
a = 1.5

# Simple if / else
if (a < 1.2):
    print("a is less than 1.2")
else:
    print("a is more than (or equal to) 1.2")


# Demonstrate boolean use in if statements
test = (a == 1.5)
if test:
    print("a is equal to (or very close to) 1.5")
else:
    print("a is not equal to 1.5")

# Using multiple if statements
if (a < 1.0):
    print('a is less than 1.0')
elif (a < 1.5):
    print('a is less than 1.5')
elif (a < 2.0):
    print('a is less than 2.0')
else:
    print("Made it to the else part")