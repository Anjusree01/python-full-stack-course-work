
#1.case conversion methods

"anjusree".upper()
'ANJUSREE'
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
10.isliteral()
SyntaxError: invalid syntax

#5.Replace & modify methods:

"anjusree".replace("sree","anju")
'anjuanju'
'anjusree'.translate(str.maketrans("a","x"))
'xnjusree'
'anjusree'.maketrans("anju","sree")
{97: 115, 110: 114, 106: 101, 117: 101}

#6.splitting & joining methods
"a,n,j,u".split(",")
['a', 'n', 'j', 'u']
"a,n,j,u".rsplit(",", 1)
['a,n,j', 'u']
"Anju\nSree".splitlines()
['Anju', 'Sree']
" ".join(["Hello", "world"])
'Hello world'
"anju-sree".partition("-")
('anju', '-', 'sree')
"anju-sree".rpartition("-")
('anju', '-', 'sree')

#7.whitespace & trimming methods
"  anju  ".strip()
'anju'
"--anju".lstrip()
'--anju'
"--anju".lstrip("-")
'anju'
"anju--".rstrip("-")
'anju'

#8.encoding & decoding:

"anju".encode("utf-8")
b'anju'
b"anju".decode("utf-8")
'anju'
