ar = [-2,-3,4,-1,2,1,5,-3]
i = 0; j= len(ar)-1
dir = {}
def cal(arr,i,j):
    temp =0
    while i<=j:
        temp +=arr[i]
        i +=1
    return temp
while i<=j:
    if ar[i] <0:
        i +=1
    if ar[j]<0:
        j -=1
    dir[f'{ar[i]} to {ar[j]}'] = cal(ar,i,j)
    i +=1

Keymax = max(dir, key=dir.get)
print(Keymax)