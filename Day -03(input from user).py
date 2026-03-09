name=input('enter the name:') #input for the string,
                              #default input type is string
age=int(input('enter your age:')) #input for the integer
marks=float(input('enter your marks:')) #input for the float
names =input('enter your names:(space separated)').split() #input for the list
names =input('enter your names:(comma separated)').split(',')
numbers=list(map(int,input('enter your numbers:').split())) #input of integers for the list
numbers=list(map(float,input('enter your numbers:').split())) #input of float for the list
numbers=list(input('enter your names:').split()) #input of strings for the list
numbers=tuple(input('enter your names:').split()) #input of strings for the tuple
numbers=tuple(map(int,input('enter your nums:').split())) #input of integers for the tuple
numbers=tuple(map(float,input('enter your nums:').split())) #input of float for the tuple
numbers=set(input('enter your nums:').split()) #input of string for the set
numbers=set(map(int,input('enter your nums:').split())) #input of integers for the set
numbers=set(map(float,input('enter your nums:').split())) #input of float for the set
d = eval(input('enter the input:')) #input for the dictionary              
# enter the input:{1:1,2:4,3:9}              
# {1: 1, 2: 4, 3: 9}
d = eval(input('enter the input:'))             
# enter the input:(1,2,3,4)            
#(1, 2, 3, 4)
