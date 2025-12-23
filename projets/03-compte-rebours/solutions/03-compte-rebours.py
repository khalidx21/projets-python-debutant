import time

seconds = int(input('Number of seconds : '))

for i in range(seconds, -1, -1):
    print('End !' if i==0 else i)
    if i != 0 : time.sleep(1)
    pass
