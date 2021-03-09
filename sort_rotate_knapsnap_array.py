from typing import ItemsView


arr = [30,24, 14, 53, 466,600,234]
arr1 = [10,20,30,40,50,60]
max= 500
print("array is :",arr)
# Sort array
for i in  range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Sorted array :",arr)

# reverse array
if len(arr)%2 ==0:
    for i,j in zip(  range(0, int(len(arr)/2)  ),range(  int(len(arr)-1),int(len(arr)/2-1),-1)   ):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    print('Reversed array :',arr)
if len(arr)%2==1:
    start = 0
    mid1 =int(len(arr)/2)
    mid2 = mid1+1
    end = len(arr)
    for i,j in zip(range(start,mid1),range(end-1,mid2-1,-1)):
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    print('Reversed array :',arr)

original = set(arr.copy())
[600,466,234,53,30,24, 14]
k = 900;sum = 0;remanins = []
for i in range(len(arr)):
    if sum <k:
        sum += arr[i]
        if sum>k:
            sum -= arr[i]
            remanins.append(arr[i])
    else:
        remanins.append(arr[i])
remanins = set(remanins)
print("k is :",k)
print("sum added in total :",sum,"\nRemaining in list :",remanins,"\nIdems add in sum :",original.difference(remanins))

