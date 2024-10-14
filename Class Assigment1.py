# WHAT IS OOP
#
# Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
# For example, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.
# Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees or students and teachers. OOP models real-world entities as software objects that have some data associated with them and can perform certain operations.
# The key takeaway is that objects are at the center of object-oriented programming in Python. In other programming paradigms, objects only represent the data. In OOP, they additionally inform the overall structure of the program.
# Key Concepts of OOP


#  Encapsulation
# Encapsulation means restricting direct access to the internal variables and methods of an object to ensure better control.

class Person:
  def __init__(self, name):
    self.__name = name

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class animal:
  def sound(self):
      print("Animal makes a sound.")

class Dog(animal):
  pass




dog = Dog()
dog.sound()


# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# An example of a Python function that can be used on different objects is the len() function.

x = "Hello World!"

print(len(x))

# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages.

# 1. Class and Object
# Class: A blueprint for creating objects.
# Object: An instance of a class.
class student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

st1 = student("Mashal", 28)

print(st1.name)
print(st1.age)


# Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.
# default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
# parameterized constructor: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

class Employee:
  def __init__(self, name, id):
    self.id = id
    self.name = name

  def display(self):
    print("ID: %d \nName: %s" % (self.id, self.name))


# String concatenation means add strings together.
#
# Use the + character to add a variable to another variable:

x = "Python is "
y = "awesome"
z =  x + y
print(z)


# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

class student:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Hello, my name is {self.name}.")


student1 = student("Alice")




# Python supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options,
# to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated
# or lengthy, like other concepts of Python, this concept here is also easy and short.

# 1. Writing to a file (creates the file if it doesn't exist)
with open('example.txt', 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("Data written to 'example.txt'.")

# 2. Reading from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("\nReading from 'example.txt':")
    print(content)

# 3. Appending data to the existing file
with open('example.txt', 'a') as file:
    file.write("This is a new line added at the end.\n")

print("\nData appended to 'example.txt'.")

# 4. Reading the updated content
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print("\nReading updated content from 'example.txt':")
    print(updated_content)
#What Is NumPay
# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
# NumPy stands for Numerical Python.

# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important.


# NOTE:VARIETY OF THIS ASSIGNMENT IS FROM INTERNET AND CHATGPT 🙂




