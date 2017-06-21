#Making string values to upper_lower_max_min_replace
__author__ = "Venkat"
s="itsmygalaxy"

print ("Printing string UPPER:")
print s.upper()

print ("Printing string LOWER:")
print s.lower()

print("Max Character in the String:")
print max(s)

print("Min Character in the String:")
print min(s)

print ("Replacing the character 'a' with '--A--':")
print s.replace("a", "--A--")

'''
=============output===================
python lower_upper_replace_max_min.py
Printing string UPPER:
ITSMYGALAXY
Printing string LOWER:
itsmygalaxy
Max Character in the String:
y
Min Character in the String:
a
Replacing the character 'a' with '--A--':
itsmyg--A--l--A--xy
=============End of output============
'''
