# all generators comprehensively iterate over a collection (in memory or generated on demand)
# we can write custom generators, by using the 'yield' keyword

# suppose we need MULTIPLES from start to stop by step
def my_gen(start=1, stop_before=10, step=2): # sensible default values
    '''
    We can generate increasing multiples of a range of numbers
    '''
    number = start
    while number < stop_before:
        yield number # the 'yield' keyword makes this into a custom generator
        number *= step # increment number by multiples

def app():
    x = my_gen() # uses the defaults
    y = my_gen(3, 64, 4) # overrides the defaults
    # x and y are now instances of our custom generator - so we can iterate over them
    l = []
    for item in x: # populate a list from all the values in generator 'x'
        l.append(item)
    print(l)
    print(type(y)) # it is a generator
    print(*y) # make use of unpacking syntax *
    print(*y) # no output - the generator is exhausted!!
    # we need a fresh generator if we want the values again!!

if __name__ == '__main__':
    app()