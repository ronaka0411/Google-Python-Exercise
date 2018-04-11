# unicode string object of python
# use of encode and decode method of string class of python
import sys

ustring = u'A unicode \xf2 string \xf1' #ustring contains unicode string
print(ustring)
s = ustring.encode('utf8') #s contains bytes of utf8 encoding
print(s)
t = s.decode('utf8')
print(t == ustring)

# Output
'''
A unicode ò string ñ
b'A unicode \xc3\xb2 string \xc3\xb1'
True
'''

