flist=[]
slist=[]
sum1=0
sum2=0
len1=int(input("Enter the number of elements :"))
for i in range(0,len1):
    print("Enter the elements",i+1)
    inp=int(input())
    flist.append(inp)
len2=int(input("Enter the number of elements"))
for i in range(0,len2):
    print("Enter the elements",i+1)
    inp=int(input())
    slist.append(inp)
if(len(flist)==len(slist)):
    print("same elngth")
else:
    print("Not same")


for num in flist:
    sum1+=num
for num in slist:
    sum2+=num
if sum1==sum2:
    print("sum are same")
else:
    print("Sum are not same")
for num in flist:
    if num in slist:
        print(num,"found in both list")
    
    
