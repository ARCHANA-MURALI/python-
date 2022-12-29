list=[]
a=[]
n=int(input("Enter the limit of list"))
print("Enter the list elments\n")
for i in range (0,n):
      print("Enter the element no:-{}",format(i+1))
      elem=int(input())
      list.append(elem)
print(" the entered list is:",list)
for i in list:
      if i>100:
            a.append(i)
else:
    print("over")
print("the value greater than 100",a)    
