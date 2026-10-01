#1 Print numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)
#2 Print numbers from 10 to 1 using while loop
i = 10

while i >= 1:
    print(i)
    i -= 1

#3 Multiplication table
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

#4 Sum of numbers from 1 to n
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)

#5 Factorial of a number
number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)

#6 Print even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

#7 Reverse a number using a loop
number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse:", reverse)

#8 Count digits of a number
number = int(input("Enter a number: "))

number = abs(number)
count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10
        count += 1

print("Number of digits:", count)

#9 Check whether a number is prime
number = int(input("Enter a number: "))

if number <= 1:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

#10 Fibonacci series up to n terms
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

