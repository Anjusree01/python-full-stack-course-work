'''#1.
for i in range(1,11):
    print(i)

#2.
for i in range(1,21):
    print(i)

#3.
for i in range(10,0,-1):
    print(i)

#4.
for i in range(2,21,2):
    print(i)

#5.
for i in range(1,20,2):
    print(i)

#6.
n = 5
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')

#7.
n = int(input("enter a num:"))
for i in range(1,11):
    print(f'{n}*{i} = {n*i}')

#8.
sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)

#9.
n = int(input("enter the number: "))
for i in range(1,n):
    n = n + i
print(n)

#10.
for i in range(1,11):
    print(i * i)

#11.
for i in range(1,11):
    print(i * i * i)'''

#12.
r = 0
for i in range(1,51):
    r = i % 5
    a = count(r)
    print(a)
        
