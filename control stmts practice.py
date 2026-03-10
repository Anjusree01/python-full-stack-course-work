'''seats = (1,2,3,4,5)
for i in range(46):
    needed_seats = int(input("enter the no.of seats needed: "))
    if needed_seats == seats:
        print("your seat booking is conformed")
        break
    else:
        print("you can book maximum of 5 seats only")
else:
    print("seats are fulled")'''

'''Write a program that asks the user to guess a secret number (7).
Give the user 5 attempts.
If the guess is correct, print “You guessed correctly!”
Otherwise, after all attempts print “Better luck next time.”

secret_number = 7
for i in range(5):
    user_guess = int(input('enter your guess no.:'))
    if user_guess == secret_number:
        print("You guessed correctly!")
        break
    else:
        print("wrong guess")
else:
    print("Better luck next time")
        
Write a program where the user must enter a correct OTP (4321) within
3 attempts. If the OTP is correct, print “Verification successful.” 

otp = 4321
for i in range(3):
    user_input = int(input("enter the otp number:"))
    if user_input == otp:
        print("verification successful")
        break
    else:
        print("try again")
else:
    print("your attempts are compeleted")
    
Write a program that asks the user to enter a number greater than 50.
Give 4 attempts. If the user enters a correct number, print “Valid number.” '''

number <= 50
for i in range(4):
    user_number = int(input("enter the number:"))
    if user_number == number:
        print('valid number')
        break
    else:
        print('invalid number')
else:
    print('attempts are completed')
        
