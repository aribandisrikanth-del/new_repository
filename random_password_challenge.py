import random
x=""
def letter():
    y=random.randint(1,26)
    alphabet=[chr(i) for i in range(97,123)]
    alphabet1=[chr(i) for i in range(65,91)]
    if random.randint(0,1)%2!=0:
        return alphabet[y]
    else:
        return alphabet1[y]

for i in range(random.randint(10,20)):
    x+=letter()
print(x)