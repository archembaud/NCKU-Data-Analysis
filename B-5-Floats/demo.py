# Demonstration of simple floats
a = '1.5'
b = float(a)
print(f'Value of a and b is {a}, {b}')
print(f"The type of a is {type(a)} and type of b is {type(b)}")

# Demonstration of round
c = round(b)   # round(a) results in an error!
print(f"The rounded value of a is {c}")