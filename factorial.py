def fact(num):
    f=1
    if num<0:
        print("Factorial of 0 is not possible")
    elif num==0:
        print("Factrorial is:",f)
    else:
        for i in range (1,num+1):
            f=f*i
        print("Factorial is:",f)
num=int(input("Enter the number"))
fact(num)
