#Simple Pattern Generator
n = input("Enter the number of rows:")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="") #or print(i,end="") if you want 1, 22, 333 .... type pattern
    print()

#similar can be used to generate triangles out of stars, slash, etc, hollow triangles as well.