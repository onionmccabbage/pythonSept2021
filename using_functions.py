# we can encapsulate logic in a reuseable function

def doStuff(some_value):
    print(some_value**2)

x=0

while x<5: # CAREFUL - we need a way to stop the while loop!!!
    # break # this will ALWAYS stop teh while loop
    x += 1
    doStuff(x)


# find the hypotenuse of a right-angled triangle
def pythag(x=3, y=4): # optional defaults for the arguments
    '''
    This is a docstring - explain the purpose of this function
    Arguments received for x and y
    return hypotenuse (root of sum of squares)
    '''
    r = (x*x + y*y)**0.5
    return r

# here we use our function NB there is no overloading function in python
print(pythag()) # 5
print(pythag(3)) # 5 uses default value of y
print(pythag(y=4)) # 5 uses default value of x
print(pythag(30, 40)) # 50

