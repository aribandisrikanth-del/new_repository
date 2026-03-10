s1=[1,2,3,4]
s2=["a","b","c","d"]
s3=list(zip(s1,s2))
print(s3)

for x,y in zip(s1,s2[::-1]):
    print(x,y)

dict1={s2 for s1, s2 in zip(s1,s2)}

print(dict1)