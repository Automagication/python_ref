"""
class
"""
class Employee:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

john = Employee('John')
print(john) # John


print('****************************************************')
# Dog class
class Dog:
  # Method of the class
  def bark(self):
    print("Ham-Ham")

# Create a new instance
charlie = Dog()

# Call the method
charlie.bark()
# This will output "Ham-Ham"

print('****************************************************')
#instantiate
class Car:
  "This is an empty class"
  pass

# Class Instantiation
ferrari = Car()
print('****************************************************')

class my_class:
  class_variable = "I am a Class Variable!"
  
x = my_class()
y = my_class()

print(x.class_variable) #I am a Class Variable!
print(y.class_variable) #I am a Class Variable!
print(my_class.class_variable)
print('****************************************************')



