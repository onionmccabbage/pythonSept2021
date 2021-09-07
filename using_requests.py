# we can make calls to external API end-points
import requests # we may need to add the requests library to Python
import json # json is part of the standard python library

def main(n=1): # no need for *args or **kwargs
    result = requests.get('https://jsonplaceholder.typicode.com/photos')
    result_d = result.json() # convert the retrieved data to a dictionary
    print(result_d)

if __name__ == '__main__':
    # ask user for a number
    n = input('which number? ')
    # call the 'main' function
    main(n)