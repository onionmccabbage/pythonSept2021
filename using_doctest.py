# doctest is a simple way to unit test a module
import doctest # part of python standard library

def cube(x):
    # mini-challenge - add a test for hte cube of -3
    '''
    This function returns the cube of a number
    >>> cube(3)
    27
    >>> cube(-3)
    -27
    '''
    return x*x*x

if __name__ == '__main__':
    # r = cube(27)
    # print(r)
    # we can invoke doctest here
    doctest.testmod(verbose=True)