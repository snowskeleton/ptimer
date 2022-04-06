import sys
from datetime import datetime
from time import sleep

from ptimer import convert, pdate


print("How long, in minutes?")
for line in sys.stdin:
    delta = convert(line)

    target = datetime.now() + delta
    print('Start: ', pdate(datetime.now()))
    print('Finish:', pdate(target))
    print('Total: ', pdate(delta))
    print("––––––––––––––––")
    while a != '00:00.00':
        a = pdate((target - datetime.now()))
        print('Left:  ', a, end='\r' )
        sleep(1)

    print('\nHow long, in minutes?')
if __name__ == '__main__':
    pass
