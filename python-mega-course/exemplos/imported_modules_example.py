import time
import os

#dir(os)

while True:
    if os.path.exists('files/vegetables.txt'):
        with open('files/vegetables.txt') as file:
            print(file.read())
    else:
        print('File does not exist.')
            
    time.sleep(10)

