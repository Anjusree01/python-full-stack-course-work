Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#1.case conversion methods

"anjusree".upper()
'ANJUSREE'
'ANJUSREE.lower()
SyntaxError: unterminated string literal (detected at line 1)
'ANJUSREE'.lower()
'anjusree'
'anju'.capitalize()
'Anju'
'Anju sree'.title()
'Anju Sree'
'AnjuSree'.swapcase()
'aNJUsREE'
'anjusree'.casefold()
'anjusree'
'ANJUSREE'.casefold()
'anjusree'
'Anjusree'.casefold()
'anjusree'

#2.Alignment & Formatting

'anju'.center(4,"*")
'anju'
'anju'.center(8,"*")
'**anju**'
'anju'.ljust(6,'&')
'anju&&'
'anju'.rjust(6,'&')
'&&anju'
'anju'.zfill(5)
'0anju'

#3.search & find methods

'anju'.find("1")
-1
'anju'.find("1")
-1
'anju'.find("a")
0
'anju'.rfind("j")
2
'anju'.rfind("n")
1

'anju'.index("a")
0
'anju'.index('s')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'anju'.index('s')
ValueError: substring not found
'anju'.rindex("u")
3

'anjusree'.count("e")
2

#4.string testing methods
'anjusree'.startswith('anj')
True
'anjusree'.endswith('ree')
True
'anju'.isalpha()
True
'anju1'.isalnum()
True
"anju".islower()
True
'ANJU'.isupper()
True
" ".isspace()
True
"Anju Sree".istitle()
True
"var1".isidentifier()
True
"10".isliteral()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    "10".isliteral()
AttributeError: 'str' object has no attribute 'isliteral'
10.isliteral()
SyntaxError: invalid syntax

#5.Replace & modify methods:

"anjusree".replace("sree","anju")
'anjuanju'
'anjusree.translate9str.maketrans("a","x"))
SyntaxError: unterminated string literal (detected at line 1)
'anjusree'.translate(str.maketrans("a","x"))
'xnjusree'
>>> 'anjusree'.maketrans("anju","sree")
{97: 115, 110: 114, 106: 101, 117: 101}
>>> 
>>> 
>>> #6.splitting & joining methods
>>> 
>>> "a,n,j,u".split(",")
['a', 'n', 'j', 'u']
>>> "a,n,j,u".rsplit(",", 1)
['a,n,j', 'u']
>>> "Anju\nSree".splitlines()
['Anju', 'Sree']
>>> " ".join(["Hello", "world"])
'Hello world'
>>> "anju-sree".partition("-")
('anju', '-', 'sree')
>>> "anju-sree".rpartition("-")
('anju', '-', 'sree')
>>> 
>>> #7.whitespace & trimming methods
>>> "  anju  ".strip()
'anju'
>>> "--anju".lstrip()
'--anju'
>>> "--anju".lstrip("-")
'anju'
>>> "anju--".rstrip("-")
'anju'
>>> 
>>> #8.encoding & decoding:
>>> 
>>> "anju".encode("utf-8")
b'anju'
>>> "anju".encode("utf-9")
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    "anju".encode("utf-9")
LookupError: unknown encoding: utf-9
>>> "anju".decode("utf-8")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    "anju".decode("utf-8")
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b"anju".decode("utf-8")
'anju'
