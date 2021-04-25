row = int(input("Enter no of rows"))
column = int(input("Enter no of column"))
ls = []
for i in range(row):
    a = []
    for j in range(column):
        num = int(input(f"Enter number for {i,j} :"))
        a.append(num)
    ls.append(a)
print(ls)