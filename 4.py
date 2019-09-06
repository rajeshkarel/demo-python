class Student:  # another way is - class Student(object):
    # the below block define attributr
    def __init__(self):
        self.name = "karel"
        self.age = 31
        self.masks = 900

    def talk(self):
        print(self)
        print(
            f"Hi all, My name is {self.name} , age is {self.age}, and my masks is {self.masks}"
        )


# print(self)
s = Student()
print(s)
s.talk()
print(s.talk())
