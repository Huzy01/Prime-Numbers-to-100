# Name of program - Prime Numbers

# Programmer - Huzaifah Hensrot

# Version 1.0

# Date- 17/06/2020


print('Welcome to Huzaifahs prime number program')
Name = input('Enter your name:')
# this is the welcome screen where the user will input their name.

print('Hello' + ' ' + Name)
# introduces the user
input('Press enter to continue')

print('A  prime  number is a number that can only be divided by 1 or itself')
# defintion of a prime number
input('Press enter to contine')

print('Type Fact if you want to see a fun fact about prime numbers or press enter to continue')
fact =input('>>')
if fact=='Fact':
    print('Did you know that 1 is not a prime number. This makes 2 the smallest prime number')
else:
    print('Okay we will move on')
input('Press enter to continue')

responce = input('Would you like to see the prime numbers from 1-100' + ' ' + 'Type Y(Yes) or N(No)')
# this is a question (decision making statement) where the program will ask the user if they want to see the prime numbers 1-100


if responce == 'Y':
    # what this says is that if your answer to the above question is yes, then the prime number function will executed.
 print('Here:')
 
 for num in range(2,100): # This is a range for the prime numbers within a for loop
   if num > 1:# the number  must be greater than 1, as 2 is the smallest prime number
       for i in range(2,num):
           if (num % i) == 0:
               break # terminates the for loop
       else:
           print(num)# outputs the prime numbers

elif responce == 'N':
    # if your answer is no to the above question, then the program will be ended. 
    print('Good bye' + ' ' + Name)
    # farewell message for the user
    exit()
    #this function will close the program

elif responce != 'Y' or 'N':
  print('You did not select Y or N but I will still display the prime numbers')
  #prime number function:
  for num in range(2,100):
      #This is a range for the prime numbers within a for loop
   if num > 1:
       # the number  must be greater than 1, as 2 is the smallest prime number
       for i in range(2,num):
           if (num % i) == 0:
               break
            #terminates the for loop
       else:
           print(num)
           #outputs the prime numbers
 input('Press enter to exit')
