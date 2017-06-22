#simple sample of Arguments passed and displaying it using the code.
__author__ = "Venkat"
import sys
print ("Number of arguments:", len(sys.argv),"arguments.")
print("Argument List",str(sys.argv))

'''
############Output##########
$ python arguments.py py1, py2, py3
Number of arguments: 4 arguments.
Argument List ['Arguments.py', 'py1,', 'py2,', 'py3']
===
$ python Arguments.py py1,py2,py3
Number of arguments: 2 arguments.
Argument List ['Arguments.py', 'py1,py2,py3']
############End of Output##########
'''
