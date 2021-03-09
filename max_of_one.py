ls = [
    [0,1,0,1],
    [1,1,0,0],
    [0,0,0,1],
    [1,1,1,1]
]
dir={}
for i in range(len(ls)):
    one = 0
    for j in ls[i]:
        if j==1:
            one +=1
    dir[i]=one

print(max(dir))