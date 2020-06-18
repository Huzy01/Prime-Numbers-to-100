## By Huzaifah Hensrot


# Prime-Number-Program

## Python3 program to display the prime numbers

This program is written in **Python 3** which aims to aim **display the prime numbers from 1-100**. In addition to this, there are some *extra features* such as:

* Asks the user their name (Line 10 - 16):

`print('Welcome to Huzaifahs prime number program')
Name = input('Enter your name:')
#this is the welcome screen where the user will input their name.

print('Hello' + ' ' + Name)
#introduces the user
input('Press enter to continue')`

* Tells them the defintion of a prime number (Line 18 - 20 ):

`print('A  prime  number is a number that can only be divided by 1 or itself')
#defintion of a prime number`

* Asks them if they want to see a fun fact about prime numbers and then (Line 22 - 28 ):

`print('Type Fact if you want to see a fun fact about prime numbers or press enter to continue')
fact =input('>>')
if fact=='Fact':
    print('Did you know that 1 is not a prime number. This makes 2 the smallest prime number')
else:
    print('Okay we will move on')
input('Press enter to continue')`


* Asks the user if they want to see the prime numbers from 1-100. If they say yes then it would display the prime bumbers but if they say no the program will end (Line 30 - 66):

`if responce == 'Y':
    #what this says is that if your answer to the above question is yes, then the prime number function will executed.
 print('Here:')
 
 for num in range(2,100): # This is a range for the prime numbers within a for loop
   if num > 1:# the number  must be greater than 1, as 2 is the smallest prime number
       for i in range(2,num):
           if (num % i) == 0:
               break # terminates the for loop
       else:
           print(num)
           #outputs the prime numbers

elif responce == 'N':
    # if your answer is no to the above question, then the program will be ended. 
    print('Good bye' + ' ' + Name)
    # farewell message for the user
    exit()
    # this function will close the program

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
           #outputs the prime numbers`



## How to run the prime number program

For users who are new to visiting this repository, this is a step by step guide to running my program:

1. Stay on the current repository (Prime-Number-Program) and click and open on the file that says "PrimeNumberHuzaifah.py"

2. Next, copy the whole code and paste into any Python IDLE (I would recommend using the IDE from Python.org).
Click on the link to download Python3.8.3 https://www.python.org/downloads/ or you can use an online Python IDE by clicking on this link https://repl.it/languages/python3 and pasting my code on to the main.py file. 

3. Once downloaded and installed, click on IDLE(Python3.8 32-bit).

4. Once open, click on the edit tab and open a blank file. Thereafter paste the code and save it (**save the file as     (WhateverNameYouWant .py).

5. When you have saved the file, you can run the code by pressing F5 or clicking on the 'Run button' in the Run tab.

**Any problems just email me on: huzaifahhensrot@gmail.com 
