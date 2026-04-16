'''
#EXCEPTIONAL HANDLINGS:(two types of errors-complier error,runtime error)

#single expection
try:
    a = int(input("enter the integer:"))
except:
    print("please enter the integer")
else:
    print("a=",a)
finally:
    print("end of the program")

#multiple exception


try:
    l = [2,3]
    #print(l[5])
    d = {1:3,2:7,4:9}
    print(d[5])
    print(10/0)
    a = int(input("enter the integer:"))
    print(a+'10')
except TypeError:
    print("enter the correct datatype")
except IndexError:
    print("list is out of range")
except KeyError:
    print("Key is not present")
except ZeroDivisionError:
    print("a num can't be divide by zero")
except ValueError:
    print("please enter the integer")
else:
    print("a=",a)
finally:
    print("end of the program")


try:
    l = [2,3]
    #print(l[5])
    d = {1:3,2:7,4:9}
    #print(d[8])
    print(10/0)
    a = int(input("enter the integer:"))
    print(a+'10')
except (TypeError,IndexError,KeyError,ZeroDivisionError,ValueError) as e:
    print("Error occured",e)

else:
    print("a=",a)
finally:
    print("end of the program")


try:
    l = [2,3]
    #print(l[5])
    d = {1:3,2:7,4:9}
    #print(d[8])
    print(10/0)
    a = int(input("enter the integer:"))
    print(a+'10')
except Exception as e:
    print("Error occured",e)

else:
    print("a=",a)
finally:
    print("end of the program")

try:
    balance = 1000
    amount =-10
    if amount<0:
        raise Exception('Amount needs to be positive')
    balance += amount

except Exception as e:
    print("Error occured:",e)

else:
    print("Current Balance:",balance)

finally:
    print("End of the program")
'''

#open |read,write,append | close

file = open('namess.txt','r') #create a notepad file consist of student names
print(file.read())
file.seek(0)
print(file.readline())
file.seek(10)
print(file.readlines())
file.close
'''
try:
    
    file = open('namess.txt','r')
except FileNotFoundError:
    print("File not found")
else:
    
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(10)
    print(file.readlines())
    file.close()
    
'''
