

#2 Accept two numbers and display their data types
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("First number:", num1)
print("Data type:", type(num1))

print("Second number:", num2)
print("Data type:", type(num2))

#3 Convert a string number into integer and float
number = "25"

integer_number = int(number)
float_number = float(number)

print("Integer:", integer_number)
print("Float:", float_number)

#4 Find the length of a string
text = input("Enter a string: ")

print("Length:", len(text))

#5 Create list, tuple, set, and dictionary
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)
my_set = {1, 2, 3, 4}
my_dictionary = {
    "name": "Yuvi",
    "age": 20
}

print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dictionary)
print("Type:", type(my_dictionary))


