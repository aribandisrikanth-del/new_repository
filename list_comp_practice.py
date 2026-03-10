inp=int(input("pick a number "))
list1=[]
for i in range(0,inp+1):
    list1=list1+[i]
list2=[x for x in list1 if x%2==1]
print(list2)

fruits=["orange","strawberry","banana"]
caps_fruits=[fruit.capitalize for fruit in fruits]
print(caps_fruits)