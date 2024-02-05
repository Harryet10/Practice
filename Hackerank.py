# 1. Hello World
print("Hello, World!")

# 2. Variables and Data Types
name = "John"
age = 25
height = 1.75
is_student = True

# 3. User Input
user_input = input("Enter something: ")
print("You entered:", user_input)

# 4. Conditional Statements
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 5. Loops
for i in range(5):
    print(i, end=" ")

while i > 0:
    print(i, end=" ")
    i -= 1

# 6. Lists
fruits = ["apple", "banana", "orange"]
print("List:", fruits)

# 7. Functions
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# 8. Dictionaries
person = {"name": "Bob", "age": 30, "city": "New York"}
print("Person:", person)

# 9. File Handling
with open("example.txt", "w") as file:
    file.write("This is an example.")

with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# 10. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 11. Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()

# 12. Lambda Functions
square = lambda x: x ** 2
print("Square of 5:", square(5))

# 13. List Comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print("Squares:", squares)

# 14. Random Module
import random
random_number = random.randint(1, 10)
print("Random number:", random_number)

# 15. Web Scraping (using BeautifulSoup)
from bs4 import BeautifulSoup
import requests

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string
print("Page Title:", title)

# 16. List Slicing
subset = numbers[1:4]
print("Subset:", subset)

# 17. String Formatting
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# 18. Tuples
coordinates = (3, 4)
x, y = coordinates
print("X:", x, "Y:", y)

# 19. Sets
fruits_set = {"apple", "banana", "orange"}
fruits_set.add("grape")
print("Fruits Set:", fruits_set)

# 20. File Handling (Appending)
with open("example.txt", "a") as file:
    file.write("\nAppending more text.")

with open("example.txt", "r") as file:
    content = file.read()
    print("Updated File Content:", content)

# 21. Decorators
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# 22. Map Function
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers:", squared_numbers)

# 23. Enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 24. List Sorting
sorted_numbers = sorted(numbers)
print("Sorted Numbers:", sorted_numbers)

# 25. Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print("Factorial of 5:", result)
