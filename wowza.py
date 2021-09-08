def wow():
    pass

def other():
    pass


wow.someProp = 'oops'
wow.o = other


print(wow.someProp, wow.o)

wow.o()