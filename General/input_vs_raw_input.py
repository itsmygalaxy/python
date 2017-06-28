__Author__ = "Venkat"
name = raw_input("what is your name:\n")
age = raw_input("what is your age:\n")
print'======================================='
print'The below is the output of raw_input():'
print'======================================'
print 'Welcome '+ name
print'Glad you crossed '+age
print 'type of age is: ', type(age)

print('=======================================')
print('The below is the output of input(): ')
print('=======================================')
bmonth = input('Enter the birth month(numeric) you were born: ')
print name+",Brilliants are born on this month: ",bmonth
print 'type of month is: ', type(bmonth)


'''
#############Output#####################
what is your name:
Jason
what is your age:
30
=======================================
The below is the output of raw_input():
======================================
Welcome Jason
Glad you crossed 30
type of age is:  <type 'str'>                   --> Make a note its string.
=======================================
The below is the output of input():
=======================================
Enter the birth month(numeric) you were born: 8
Jason,Brilliants are born on this month:  8
type of month is:  <type 'int'>                    --> Make a note its Integer.
##########End of Output##################
'''
