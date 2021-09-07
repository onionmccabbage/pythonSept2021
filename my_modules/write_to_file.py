# this utility takes a string as input and appends it to a text file

def appendFileContents(whichFile, whatToWrite):
    '''
    Write text to a persistent text file
    '''
    try:
        fout = open(whichFile, 'at') # append text
        fout.write(whatToWrite+'\n') # add a new-line character at the end
    except Exception as e:
        print('there was a problem: {}'.format(e))
    finally:
        fout.close()

if __name__ == '__main__':
    appendFileContents('test.txt', 'some content')