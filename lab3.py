#1

for i in range (1499,2701):
    if i%5==0:
        print(i,"is a multiple of 5")
    elif i%7==0:
        print(i,"is a multiple of 7")    
    else:
        pass

#2

temp=float(input("Enter a temperature value in farenheit:"))

temp=((temp-32)/9)*5

print(temp)

temp=float(input("Enter a temperature value in celsius:"))

temp=temp/5*9+32

print(temp)




#3

num=int(input("enter a number between 1 to 9:"))

if(num>=1 and num<=9):
    print("Well guessed!")
else:
    while  not( num>=1 and num<=9):
        num=int(input("enter a number between 1 to 9:"))
    else:
        print("Well guessed!")    
         #4 pattern 

n =int (input("Enter a number:"))

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


for i in range(n - 1, 0, -1):

    print(' ' * (n - i) + '*' * i)




#write a program that takes a workd from user and reverse it

word=input("Enter a word:")

word=word[::-1]
print(word)

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
print("the number of odd",odd)

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
     


#write a program to print fibonacci series between 0 to 50 
# 0 1 1 2 3 5 8 13 21 ...

n1=0
n2=1

print(n1,n2,end=" ")

while (n1+n2<=50):
    temp=n2
    n2=n1+n2
    n1=temp
    print(n2,end=" ") 

#10
    for i in range(1, 51):
     if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
     elif i % 3 == 0:
        print("Fizz", end=" ")
     elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end="")



#Write a Python program that accepts a sequence of lines as input, where a blank line indicates the end of input. The program should then print the lines as output, converting all characters to lowercase.

str1=""
str2=input("Enter a line:")
while (str2!=""):
    str1=str1+str2
    str2=input("Enter a line:")

print(str1.lower())    






#Write a Python program which accepts a sequence of comma separated 4 digit 
#binary numbers as its input and print the numbers that are divisible by 5 in a 
#comma separated sequence.

#Sample Data : 0100,0011,1010,1001,1100,1001  
#Expected Output : 1010

binary_numbers = input("Enter comma-separated 4 digit binary numbers: ").split(",")

divisible_by_5=[]








# Write a Python program that accepts a string and calculate the number of digits and letters.
#Sample Data : Python 3.2 
#Expected Output :  
#Letters 6  
#Digits 2


#  Take user input
text = input("Enter a string: ")

# Initialize counters
letters = 0
digits = 0

#Loop through each character in the string
for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

# Step 4: Print the results
print("Letters:", letters)
print("Digits:",digits)


