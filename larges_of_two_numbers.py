'''
num1 = 5
num2 = 6
if num1 > num2:
    print("First number is largest")
    print("BYE")
else:
    print("Second number is largest")
'''

'''
# Printing 5 natural number using print function
print(1)
print(2)
print(3)
print(4)
print(5)


# Printing 5 natural numbers using while loop :
print("\n\nUsing while loop ")
i = 0
while i < 6:
    print(i)
    i +=1

'''


'''
# Printing string letters using for loop
for letter in 'PYTHON':
    print(letter)
'''


'''
# Printing list using for loop

count = [20, 30, 40 ,50]

for num in count:
    print(num)
'''

'''
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num%2 == 0:
        print(num," is an even number")
'''


'''
# To print factor of a whole number using while loop

num = int(input("Enter a number to find its factor :"))
print(1, end=' ')

factor = 2
while factor <= num /2:
    if num % factor == 0:
        print(factor , end=' ')
    factor += 1
print(num, end='')
'''


'''
# Sum of all positive numbers

entry = 0
sum1 = 0

print("Enter numbers to find their sum of positive number ends with the loop : ")

while True:
    entry = int(input())
    if entry < 0:
        break
    sum1 += entry
    print("Sum = ", sum1)

'''


'''
# To check input number is prime or not

flag = 0
num = int(input("Enter the number to be checked : "))

if num > 1:
    for i in range(2 , int(num/2)):
        if num %i == 0 :
            flag = 1
            break
    if flag == 1:
        print(num, 'is not a prime number')
    else :
        print(num , 'is a prime number')
else:
    print("Entered number is <= 1, excute again !")

'''



'''
# To demostrate nested for loop

for var1 in range(3):
    print("Iteration" + str(var1 + 1) + 'of outer loop')
    for var2 in range(2):
        print(var2 + 1)
        print("out  of inner loop")
print("out of outer loop")
'''

'''
# Printing pattern

num = int(input("Enter a number to generate its pattern = "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

'''



#Prime numbers between 2 to 50

num = 2
for i in range(2, 10):
    j = 2
    while j <= (i/2):
        if i%j == 0:
            break
        j += 1
    if j > i/j:
            print(i, 'is a prime number')
print("BYE , BYE")



'''
# Calculate factorial of given numbers
fact = 1
num = int(input("Enter a number : "))
if num < 0:
    print("Sorry, factorial does not exist for negative number ")
elif num == 0 :
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact * i
        print("Factorial of ", num , 'is : ', fact)
'''



'''
# differnt type od data types

a = 10
print("Data type of a is : ", type(a))

b = 10.5
print("Data type of b is : ", type(b))

c = '10'
print("Data type of c is : ", type(c))

d = True
print("Data type of d is : ", type(d))

e = None
print("Data type of e is : ", type(e))
'''


'''
# To Demostrate list methods

a = [1,2,3,4,'Hello,']
print(a)

#insert
a.insert(3, 20)
print(a)

#remove
a.remove(3)
print(a)

#Append
a.append("World")
print(a)

#len
print(len(a))


#pop
a.pop()
print(a)

#clear
a.clear()
print(a)
'''

































































