# we can make calls to external API end-points
import requests # we may need to add the requests library to Python
import json # json is part of the standard python library
# we can import our utility module
import my_modules.util

def main(n=1): # no need for *args or **kwargs
    result = requests.get('https://jsonplaceholder.typicode.com/photos/{}'.format(n))
    result_d = result.json() # convert the retrieved data to a dictionary
    # the returned data will always have a 'title' member
    print(result_d['title'])

if __name__ == '__main__':
    # ask user for a number
    n = input('which number? ')
    # we should make sure it is a number
    n = my_modules.util.checkInt(n)
    # call the 'main' function
    main(n)