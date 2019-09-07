# a name space represents a memory block where names are
# mapped or linked to objects

# understanding class namespace


class Student:
    # this is a class namespace
    n = 10


# accessing the class var in the class namespace

print(Student.n)  # display 10
Student.n += 1
print(Student.n)  # dispaly 11

# o/p will be

# 10
# 11


# we know that a single copy of class variable is shared by all instance
# so, if the class variable is modified in the class namespace, since
# same copy of the variable is modified, the modified copy is avaible to
# all instance

# modified class var is seen in all instance

print("modified class var is seen in all instance")

s1 = Student()
print(s1.n)
s2 = Student()
print(s2.n)

# o/p will be as per below

# modified class var is seen in all instance
# 11
# 11

