#if the "else" state,ent is used with a "for" loop, the else statement is executed when the loop has exhausted iterating the list.

__Author__ = "Venkat"
n=15
while n != 0:
        while n % 2 == 0:
                print n,
                print ' is an even number'
                n -= 1
        else:
                print '---------------------'
                n -= 1

'''
############Output#################
---------------------
14  is an even number
---------------------
12  is an even number
---------------------
10  is an even number
---------------------
8  is an even number
---------------------
6  is an even number
---------------------
4  is an even number
---------------------
2  is an even number
---------------------
##############End of Output###########
'''
