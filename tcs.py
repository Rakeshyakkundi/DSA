n=int(input())
arr = []
for i in range(n):
    z = int(input())
    arr.append(z)
k = int(input())
go = []
for i in range(k):
    a = arr.pop(0)
    arr.append(a)
print(arr)