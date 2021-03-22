ls = [1,2,3,4,5,6,7,8,9,10,11,2,14, 5,  16,17,18,20,21,2,24,  25,26,27,5];missing = [];a=1
#     0 1 2 3 4 5 6 7 8 9  10 11 12 13  14 15 16 17 18 19 20  21 22 23 24
for i in range(1,ls[len(ls)-1]):
    if i not in ls:
        missing.append(i)

print("missing values in array :",missing) 

x = 2;y = 5;dir={}
for i in range(len(ls)):
    if ls[i]==x:
        mini = 0
        for j in range(i,len(ls)):
            mini += 1
            if ls[j]==y:
                print("mini distance is :",mini-1)
                dir[f'{i}-{j}'] = mini-1

                break
print(dir)