# this utility retrieves all the contents of a text file and returns it

def getFileContents(whichFile):
    '''
    Read data back from a text file
    (name of text file is expected as an argument)
    '''
    resultString = ''
    try:
        fin = open(whichFile, 'rt') # read text
        resultString = fin.read()

    except Exception as e:
        resultString = 'There was a problem: {}'.format(e)
    finally:
        fin.close()
        return resultString

if __name__ == '__main__':
    r = getFileContents('test.txt')
    print(r)
    r = getFileContents('my_file.txt')
    print(r)