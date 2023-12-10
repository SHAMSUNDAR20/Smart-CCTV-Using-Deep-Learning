a=0
b=0
c=input("Enter any letter:")
for i in c:
    if i=='N':
        b+=2
    elif i=='E':
        a+=2
    elif i=='W':
        a-=2
    elif i=='S':
        b-=2

        print(a)
print(b)
if(a<0):
    print("-")
elif(a>=0):
    print("+")
if(b<0):
    print("-")
elif(b>=0):
    print("+")

