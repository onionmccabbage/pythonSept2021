# we can always check the data type

s = 'almost done'

if isinstance(s, str): # check the data type
    print('it is a string')

num = 1.2

if isinstance(num, (int, float)): # check data type against a tuple of possibilities
    print('it is a number')

print(type(s))