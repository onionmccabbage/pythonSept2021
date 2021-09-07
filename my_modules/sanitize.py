# a tuple (since we will not need to change this)
cat_t = ('users', 'posts', 'albums', 'photos')

def cleanup(**kwargs):
    '''
    clean up incoming data
    Expects 'category' and 'id' as keyword arguments
    'category' must be a string that matches values in cat_t
    'id' must be an integer 1-8 inclusive
    '''
    # check we have the expected arguments
    if 'category' in kwargs and kwargs['category'] in cat_t:
        category = kwargs['category'].lower() # force it to lower case
    else:
        category = 'users'
    if 'id' in kwargs: # check we have the expected keyword argument
        try: # catch exceptions when we try to cast the value as an integer
            # NB the input() statement ALWAYS returns a string
            id = int( float(kwargs['id']) ) # cannot just use int()
            if id not in range(1,9): # stop before 9
                id = 1 # set a sensible default
        except Exception as err:
            print(err) # we are not obliged to print anything
            id = 1 # set a sensible default
        finally: # we do not have to use finally - it can be left out
            pass # pass is useful if we need to have a block that does nothing
    else: # if no argument called 'id' was provided, use sensible defaults
        id = 1
    sanitized_data = {'category':category, 'id':id} # build a dictionary
    return sanitized_data

if __name__ == '__main__':
    # experiment = cleanup(id=3, category='posts')
    experiment = cleanup( category='teatime')
    print(experiment) # expect sensible defaults