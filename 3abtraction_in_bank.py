class Bank:
    def __init__(self):
        self.accout = 10
        self.name = "karel"
        self.balance = 1200000
        self.__loan = 1330

    def display_to_clerk(self):
        print(self.accout)
        print(self.name)
        print(self.balance)
        print(self.__loan)


b = Bank()
b.display_to_clerk()
