#Write a program to create a class with following variables and methods 
# 1. Private variable named privateVar that contains an integer value 
# 2. Create a private function privMeth that prints a message 
# 3. Create a function hello that prints the value of privateVar 
# 4. Create an object for the class and call all the functions.

class Private:
    def __init__(self, privateVar):
        self.__privateVar = privateVar
    def __privMeth(self):
        print("Hello, world!")
    def hello(self):
        self.__privMeth()
        print(self.__privateVar)
code = Private(12)
#code.__privMeth()
code.hello()

