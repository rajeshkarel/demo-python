# instance variable example
class Sample:
    # this is a constructor
    def __init__(self):
        self.x = 10

    # below is instance method
    def modify(self):
        self.x += 1


# create 2 instance

s1 = Sample()
s2 = Sample()

print("x in s1= ", s1.x)
print("x in s2= ", s2.x)

# modify x in s1

s1.modify()

print("x in s1= ", s1.x)
print("x in s2= ", s2.x)

# o/p as per below

# x in s1=  10
# x in s2=  10
# x in s1=  11
# x in s2=  10

