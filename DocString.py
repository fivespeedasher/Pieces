def PrintMaximum(a,b):
    """compare a and b

    print the bigger one"""
    a=int(a)
    b=int(b)
    if a<b:
        print(b)
    else :
        print(a)
PrintMaximum(5,10)
print (PrintMaximum.__doc__)