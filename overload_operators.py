class a():
    def __init__(self,value):
        self.value=value
    def __lt__(self,other):
        if self.value < other.value:
            return self.value,"is less than",other.value
        elif self.value > other.value:
            return self.value,"is greater than",other.value
    def __eq__(self,other):
        if self.value == other.value:
            return self.value,"is equal to",other.value

ob1=a(int(input("pick a number to check if it is greater than or equal to or less than ")))
ob2=a(int(input("pick a number to check if it is greater than or equal to or less than the other value ")))

print(ob1<ob2)

ob3=a(int(input("pick a number to check if it is equal to another number ")))
ob4=a(int(input("pick a number to check if it is equal to the other value before this ")))

print(ob3==ob4)