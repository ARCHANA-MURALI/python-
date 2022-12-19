rows=int(input("Enter number of rows and eg(N=4)"))

for i in range(1,rows+1):
    for j in range (1,i+1):
        print(i*j,end="  ")
    print("\n")