def checkResume(file):
    try:
        a = open(file, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def readFile(file):
    try:
        a = open(file, 'r')
        a1 = a.readlines()
        for x in a1:
            print(x)
    except:
        print('Error when reading')

if __name__ == '__readResume__':
    readResume()