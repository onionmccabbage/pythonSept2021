# this is a useful utility module
# we need a function which checks that a value is a number

def checkInt(i):
    '''
    This utility checks a value is an integer
    It will return 1 if not an integer
    '''
    # check if it is already an integer
    if type(i) == int:
        return i # all good - just return the integer
    else:
        # we can use exceptipn handling
        try:
            i = int(float(i)) # take the value and convert it first to a float then to an int
        except Exception as e:
            # we really ought to do something if there is an exception!!!
            print('There was an exception: {0}'.format(e))
            i=1 # set it to a sensible default
        finally: # not required, but will always run
            pass # we would normally tidy up here
    return i

if __name__ == '__main__':
    # exercise this module to check it works as intended
    print(checkInt(3))
    print(checkInt('oops')) # should return 1, with an exception