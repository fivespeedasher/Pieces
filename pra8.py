import time
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%%d='%i%j,i*j,sep='',end='    ')
    print(time.strftime('%Y-%m-%d-%a %H:%M:%S', time.localtime(time.time())))

    time.sleep(1)
    print('\n')


# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)



