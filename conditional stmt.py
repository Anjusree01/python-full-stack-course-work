print('----------------------------- simple if examples----------------------------------')

'''min_bal = 5000
current_bal =2000
if current_bal < min_bal:
    print('send mesg and cut some money')'''


print('-------------------------- if and else -----------------------------')
'''data = ('user@gmail.com','user@123')
mail = input('enter the email: ')
password = input('enter the password: ')
if data == (mail,password):
        print('Login Successful')
else:
    print('invalid login')'''


'''fruits = ['mango','apple','papaya','pine apple']
search_item = input('search here: ')
if search_item in fruits :
    print(f'{search_item} found! Buy Now')
else:
    print(f'{search_item} is out of stock, we will notify you once it is available')'''


'''print('--------------------elif--------------------------')
time = int(input('enter the hour: '))
print('Avaliable buses are: ')
if 0 <= time <=6 :
    print('bus5\nbus7\bus8\bus9')
elif 7 <= time <= 12:
    print('bus1\nbus2\nbus3')
elif 13 <= time <= 18:
    print('bus45\nbus46\nbus48\nbus49')
elif 19 <= time <= 24:
    print('bus56','bus57','bus58',sep = '\n')'''

'''print('welcome to uber, book your ride')
print('1.bike')
print('2.auto')
print('3.cab')
choice = int(input('choose the option: '))
if choice == 1:
             print('booked bike successfully')
elif choice ==2:
    print('booked auto successfully')
elif choice ==3:
    print('booked cab successfully')'''


print('---------------------------nested if------------------------------------------')
login_status = False
premium_accout = True
if login_status:
    print('welcome to the hotstar')
    if premium_account:
        print('play the viedo without ads')
    else:
        print('play the viedo with ads')
else:
    print('Invalid Login')
