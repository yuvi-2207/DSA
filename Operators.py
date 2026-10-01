#1 Addition, subtraction, multiplication, and division
a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#2 Find remainder and quotient
a = 17
b = 5

print("Remainder:", a % b)
print("Quotient:", a // b)

#3 Check even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#4 Compare two numbers
a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#5 Demonstrate logical operators
a = 10
b = 20

print("AND:", a < 20 and b > 10)
print("OR:", a > 20 or b > 10)
print("NOT:", not(a > b))

#6 Demonstrate assignment operators
x = 10

print("Initial:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)


#7 Find the largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both are equal")













