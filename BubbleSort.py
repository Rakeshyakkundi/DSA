ls = [6,2,6,2,1,9,2,64,1,13,345]
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i]>ls[j]:
            temp = ls[i]
            ls[i]=ls[j]
            ls[j]=temp
print(ls)