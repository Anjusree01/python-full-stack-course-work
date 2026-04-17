'''
#FILE OPERATIONS
#open |read,write,append | close

file = open('names.txt','r') #create a notepad file consist of student names
print(file.read())
file.seek(0)
print(file.readline())
file.seek(10)
print(file.readlines())
file.close

#
try:
    
    file = open('names.txt','r')
except FileNotFoundError:
    print("File not found")
else:
    
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(10)
    print(file.readlines())
    file.close()
    
with open('names.txt','r') as file: #if we use this then we need not to close the file coz it automatically does
    print(file.read()) 
    file.seek(0) 
    print(file.readline())
    file.seek(6)
    print(file.readlines()) 

with open('names.txt','a') as file: #to add something at the end of the file we use append ('a')
    file.write('\nHimabindhu')
    file.write('\nBunny')

with open('names.txt','w') as file: #clear the before information and rewrites the file
    file.write('\nHimabindhu')
    file.write('\nBunny')

    
with open('names.txt','w+') as file: #we can write and also read 
    file.write('\nHimabindhu')
    file.write('\nBunny')
    file.seek(0)
    print(file.read())


with open('names.txt','r+') as file: #we can read and write
    print(file.read())
    file.write('\nSunny')
    file.write('\nBhagya')

with open('names.txt','a+') as file: #we can append and read
    file.write('\nHimabindhu')
    file.write('\nBunny')
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())


file = open('names.text','r')
print(file.read())
file.seek()
print(file.readline())
file.seek()
print(file.readlines())
file.close

try:
    file = open('names.txt''r')

except FileNotFoundError:
    print("file not found in your system")

else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek()
    print(file.readlines())
    file.close()

with open("names.txt",'r') as File:
    print(file.read())
    file.seek()
    print(file.readline())
    file.seek()
    print(file.readlines())



file = open('keerthi.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())


with open('keerthi.txt','w+') as file:
    file.write("\nphone")
    file.write("\ncharger")
    file.seek(0)
    print(file.read())


'''






with open('keerthi.txt','r+') as file:
    print(file.read())
    file.write("\nchair")
    file.write("\ntable")
    file.seek(0)
    print(file.read())

with open('keerthi.txt','a') as file:
    file.write("\nbag")
    file.write("\nwatch")

  










































    
