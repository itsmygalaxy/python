# Encoding and Decoding values
__author__ = "Venkat"
s="itsmygalaxy"
s = s.encode('base64','strict')
print(s)

s = s.decode('base64','strict')
print(s)
'''
===========Output============
#python encode_decode.py
aXRzbXlnYWxheHk=

itsmygalaxy
========End of Output========
'''
