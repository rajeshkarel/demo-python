# -------------------------------------------

# what will happends when the class variable is modified in the
#  instance namepace?, since every instace will have its own
#  namespace, if the class variable is modified in the one instance
# namespace, it will not affect the variable in the other instance namespace

# understanding instance name space

# accessing the class var in the s1 instance namespace


class Student:
    # this is a class var
    n = 10


s1 = Student()

print(s1.n)

s1.n += 1

print(s1.n)

# o/p will we as per below

# 10
# 11

# mofified class var in not seen in other instance

print("mofified class var in not seen in other instance ")

s2 = Student()

print(s2.n)

# o/p will be as per blow

# mofified class var in not seen in other instance
# 10

