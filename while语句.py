num=23
i=10
while(i!=0):
    i=i-1
    guess=int(input('You guess the number is'))
    if guess==num:
        print("Congratuation you guessed it")
    elif guess>num:
        print('it\'s a little less than you think' )
    else :
        print('it\'s a bit bigger than you think')
    print('You still can try',i,'time')
else :
    print('the while loop is over')
print('Done')