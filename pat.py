x=int(input("enter the number:"))
for i in range(0,x):
    for j in range(0,x-i):
        print("\t",end="")
    for k in range(0,i+i):
        print("*\t",end="")
    print()
