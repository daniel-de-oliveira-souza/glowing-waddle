from library.interface import *
from time import sleep
from library.files import *

header('WELCOME TO MY PORTFOLIO')

while True:
    answer = menu(['About', 'Resume', 'Contact Info', 'Exit'])
    if answer == 1:
        header('ABOUT')
        file = 'about.txt'
        readFile(file)
    elif answer == 2:
        header('RESUME')
        file = 'resume.txt'
        readFile(file)
    elif answer == 3:
        header('CONTACT INFO')
        file = 'contact.txt'
        readFile(file)
    elif answer == 4:
        print('Exiting portfolio. Have a nice day!')
        break
    else:
        print('\033[31mERROR! Please enter a valid option!\033[m')
    sleep(2)