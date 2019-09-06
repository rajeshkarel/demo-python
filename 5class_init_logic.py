# instance vars and instance method - v2.0
class Student:
    def __init__(self, n='', m=0):
        self.name = n
        self.masks = m
    # this is an instance method
    def display(self):
        print('hi', self.name)
        print('your masks: ' , self.masks)
    
# constructor called with out args 
s = Student()
s.display()
print('------------')

# constructor called with args

s1 = Student('raj', 1234)
s1.display()

print('----------')

# o/p will be

# hi 
# your masks:  0
# ------------
# hi raj
# your masks:  1234
# ----------

#  we have to understand that a constractor not create an instance
# duty of constractor is to inilialize the values to the instance variable

