# understanding public and private variable
class Myclass:
    # this is constractor.
    def __init__(self):
        self.x = 1  # public
        self.__y = 2  # private

    # instance method to acces variables
    def display(self):
        print(self.x)  # x is available directly
        print(self._Myclass__y)  # name mangling required


print("accessing variable through method:")
m = Myclass()
m.display()

print("accessing through instance")
print(m.x)
print(m._Myclass__y)

