
# 'ab' is short for 'a'ddress'b'ook

ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }
print("Swaroop address is",ab['Swaroop'])
ab['Guido'] = 'guido@python.org'
print(ab)
for name, address in ab.items():
    print ('Contact %s at %s'% (name, address))

if 'Guido' in ab: # OR ab.has_key('Guido')
    print ("\nGuido's address is %s" % ab['Guido'])