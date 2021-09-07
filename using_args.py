# arguments (args) and key-word arguments (kwargs) can be passed in to functions

def myfn( *args ): # args is always a tuple of the positional arguments
    print(args) # we may not know how many arguments to expect
    for item in args:
        print(item, type(args))

def mykw( **kwargs ): # kwargs is always a dictionary of the key-word arguments
    print(kwargs) # we may not know beforehand how many positional args may be provided

# mini-challenge - add up all the positional arguments (zero or more)
def sumNumbers(*args): 
    total = 0
    for item in args:
        if type(item) == float or type(item) == int: # we should make sure all the values are numbers!!
            total += item
    return total

# build a function which takes key-word arguments for a use, returning as a dict
def makeUser(**kwargs):
    # the kwargs are already a dict so just return it!!
    return kwargs

# we should get used to using proper modular syntax
if __name__ == '__main__': # if this is the main module, run the following code
    # here we can exercise the current module
    result = sumNumbers(1,2,3, 'weeblywoo',4,5) # expect 15
    print(result)
    user_1 = makeUser(name='Ada', pwd='secret',age=42, favepet='donkey')
    print(user_1)
    
    myfn(42, 'Freda')
    t = ('coffee', True, 42)
    myfn(*t) # we can pass in a tuple, but we must unpack it

    mykw(x=1, y=2, z=True, wibble='wobble')
    d = {'f':'Timnit', 'l':'Gebru'}
    mykw(**d) # we can pass in a dict, but we must un-pack it !!!