class numbers:
    __PrivateVar=6
    def __privMeth(self):
        print("hello private message here you should not see")
    def hello(self):
        print(numbers.__PrivateVar)
obj=numbers()
obj.hello
obj.__privMeth