rows=int(input("Enter number of rows and eg(N=4)"))
Step=int(input("Enter step no:eg(step=1"))

for i in range(1,rows+1,step):
    for j in range (1,i+1,step):
        print(i*j,end="  ")
    print("\n")
