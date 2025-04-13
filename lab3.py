# 1 find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 

for num in range(1500, 2701):

    if num % 7 == 0 and num % 5 == 0:
        print(num, end=" ")

# 2 celcius to f f to c 

cel_temp = float(input("enter the temperature"))
# convert into f
fa_temp = (cel_temp * 9/5 ) + 32

print( "temperature in farenheit" ,fa_temp)

# farenheit to c 
f_temp = float(input("enter the temperature"))
# convert into c
c_temp = (f_temp - 32 )* 5/9 

print( "temperature in farenheit" ,c_temp)

#3 guess no 1 and 9 

secret_number = 5

while True:
  
    user_guess = int(input("Enter a number between 1 to 9: "))
    
    if user_guess == secret_number:
        print("Well guessed!")
        break
    else:
        print("Try again!")

        #4 pattern 

n =int (input("Enter a number:"))

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


for i in range(n - 1, 0, -1):

    print(' ' * (n - i) + '*' * i)
    #  5 reverse 

    word = input("Please enter a word: ")

reversed_word = word[::-1]

print("Reversed word:", reversed_word)
# 6 even and odd numbers 

numbers=(1,2,3,4,5,6,7,8,9,)
even = 0
odd = 0

for num in numbers:
   if num % 2 == 0:
       even+=1
   else:
       odd+=1

print("the number of even are ",even)
print("the number of odd are ",odd)

# 7 type item

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]


for item in datalist:
   
    item_type = type(item)
    
   
    print('Item:', item, ', Type:', item_type)

    # 8 
    for i in range (7):
     if i == 3 or i == 6: 
         continue
     print(i, end="")
     
  #9 
first_no = 0
second_no = 1

while first_no < 50:
    print(first_no,end=" ")

    next_no = first_no + second_no
    first_no = second_no 
    second_no = next_no

    #10
    for i in range(1, 51):
     if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
     elif i % 3 == 0:
        print("Fizz", end=" ")
     elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

        #11
        lines = []
        print("enter lines of text ")
        while True:
           line= input()

           if line == "":
              break
           lines.append(line.lower())  
        for line in lines:
         print(line)

         #12
         binary_input = input("Enter 4-digit binary numbers ")
        divisible_by_5 = []
        for binary in binary_input.split(','):
            decimal = int(binary, 2)

    if decimal % 5 == 0:
        divisible_by_5.append(binary)
        print("Binary numbers divisible by 5:", ",".join(divisible_by_5))



         #13
        input_str = input("Enter a string: ")


letter_count = 0
digit_count = 0
for char in input_str:
    if char.isalpha(): 
        letter_count += 1
    elif char.isdigit():  
        digit_count += 1

print("Letters:", letter_count)
print("Digits:", digit_count)

#14

import re

def validate_password(password):
    if (len(password) < 6 or len(password) > 16):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

password = input("Enter your password: ")
if validate_password(password):
    print("Password is valid!")
else:
    print("Invalid password!")

           

  

   

