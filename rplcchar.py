print("enter the string ")
a=input()
for i in range(1,len(a)):
    b = a[0]+a[1:].replace(a[0], '$')
print(b)
