import requests
from my_modules.sanitize import cleanup
from my_modules.write_to_file import appendFileContents
from my_modules.read_from_file import getFileContents

def get_data(category, id):
    '''
    Get data from an end-point API for a given cateory and id
    Permitted categories are: users, posts, albums and photos
    id is restricted to 1-8
    '''
    url = 'https://jsonplaceholder.typicode.com'
    full_path = '{}/{}/{}'.format(url, category, id)
    j = {'message':'no data'} # we need a dict
    try:
        res = requests.get(full_path)
        j = res.json() # we just want the json data
    except Exception as err:
        print('Something went wrong. ', err)
    finally:
        return j # return the data as a dict

def main():
    '''
    the main module of this project. Calls other methods
    '''
    # ask the user for a category and an id
    which_cat = input('which category? ')
    which_id  = input('which id (1-8)? (0 to read data from file) ')
    # zero means retreive data from a text file
    if which_id == '0':
        r = getFileContents('report.txt')
        print(r)
        quit # all done - stop the program
    # use our sanitize module to clean up the user-entered data
    cleaned = cleanup(category=which_cat, id = which_id)
    # make a request and return the json
    data = get_data(category = cleaned['category'], id = cleaned['id'])
    # build a string containing the returned data
    r = 'Category {} member {} gives the following:'.format(cleaned['category'], cleaned['id'])
    print(r)
    appendFileContents('report.txt', r) # store it in a file
    s = ''
    for k, v in data.items(): # iterate over the data members
        s += '\t{}: {}'.format(k, v) # assemble a string
    print(s)
    appendFileContents('report.txt', s)
    # if category is 'users' then also retrieve all the posts from the API
    if cleaned['category'] == 'users':
        print('Posts for user {}:'.format(cleaned['id']))
        posts = get_data(category='posts', id='')
        for item in posts: # posts is a list
            if item['userId']==cleaned['id']:
                print('Post {}: title: {} body:{}\n'.format(item['id'], item['title'], item['body']))

if __name__ == '__main__':
    main()