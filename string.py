ls = "hello hi there"
ls = ls.split()
for i in range(len(ls)):
    temp = ls[i]
    for j in range(len(ls[i]),0,-1):
        print(temp[j-1],end="")
    print("\t",end="")
print()
