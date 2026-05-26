

import re

text = 'Python'
pattern = r'[A-Z]'

result = re.match(pattern,text) #given pattern matches with the starting of the text

print(result.group() if result else "No match found") #group prints whatever matches


import re

text = 'Python 98'
pattern = r'[0-9]'

result = re.search(pattern,text) #given pattern search for entire string/check with every element

print(result.group() if result else "No match found") #group prints whatever matches

import re

text = 'Python 98'
pattern = r'[0-9]{2}'

result = re.search(pattern,text) #given pattern search for entire string/check with every element

print(result.group() if result else "No match found") #group prints whatever matches


list of all the patterns

import re

text = 'Python 12567890 5678 890 version 1897653 windows 10 marks 85 programming'
pattern = r'[0-9]{2,}'

result = re.findall(pattern,text) #findall will give you list of all the patterns
print(result)

import re

text = 'Python 12567890 5678 890 version 1897653 windows 10 marks 85 programming'
pattern = r'[0-9]{2,}'

result = re.finditer(pattern,text) #index of that number where it is starting
for i in result:
    print(i.group(),i.start())

import re

text = '9876543210'
pattern = r'[0-9]{10}'

result = re.fullmatch(pattern,text)

print(result.group() if result else "no match found")

sub- replace function

import re
text = 'python programming'
pattern = r'[aeiouAEIOU]'
result = re.sub(pattern,'*',text) #sub- replace function
print(result)

import re
text = 'python,java;mysql)flask'
pattern = r'[,;)]'
result = re.split(pattern,text)
print(result)

import re
text = 'hat hot hit hut head heap heat hate'
pattern = r'h.t'
result = re.findall(pattern,text)
print(result)


import re
text = 'hat hot hit hut head heap heat hate'
pattern = r'^h' #starting use ^
result = re.findall(pattern,text)
print(result)

import re
text = 'hat hot hit hut head heap heat hate'
pattern = r'e$' #ending use $
result = re.findall(pattern,text)
print(result)

import re
text = 'hy h hhhhhht htttttt httttttttttttttttttt'
pattern = r'ht*' #0 or more occurence of t
result = re.findall(pattern,text)
print(result)

import re
text = 'hy h hhhhhht htttttt httttttttttttttttttt'
pattern = r'ht+' #1 or more occurence of t
result = re.findall(pattern,text)
print(result)


import re
text = 'hy h hhhhhht htttttt httttttttttttttttttt'
pattern = r'ht?' #if it is there give else leave 0 or 1
result = re.findall(pattern,text)
print(result)
'''
import re
text = 'Anjusree'
pattern = r'[A-Z]'

result = re.match(pattern,text)
print(result.group() if result else "not found")

import re
text = "Amalasree"
pattern = r'[A-Z]'
result = re.match(pattern,text)
print(result.group() if result else 

