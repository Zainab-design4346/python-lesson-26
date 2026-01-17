class fun1:
    def __init__(self):
      self.str1=""
      
    def getString(self):
       self.str1=input("Enter a string: ")

    def printString(self):
       print("Result:",self.str1.upper())

s1=fun1()
s1.getString()
s1.printString()
    
