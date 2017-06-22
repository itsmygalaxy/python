#simple sample of Arguments passed and displaying it using the code.
__author__ = "Venkat"
import sys
print ("Number of arguments:", len(sys.argv),"arguments.")
print("Argument List",str(sys.argv))

# OR you can wrige as below
#print ("Number of arguments:",len(sys.argv[1:]),"arguments.")
#print ('Argument List',str(sys.argv[1:]))

'''
############Output##########
$ python arguments.py py1, py2, py3
Number of arguments: 4 arguments.
Argument List ['arguments.py', 'py1,', 'py2,', 'py3']
===
$ python arguments.py py1,py2,py3
Number of arguments: 2 arguments.
Argument List ['arguments.py', 'py1,py2,py3']
===
#output for the commented section: as argv starts from [0], so it prints arguments.py, to skip that you can give as stated above.
$ python arguments.py py1, py2, py3
Number of arguments: 3 arguments.
Argument List ['py1,', 'py2,', 'py3']

############End of Output##########
'''
