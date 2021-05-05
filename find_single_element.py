ls = [1,1,5,2,3,3,2,5,6]
# dir = {}
# for i in range(len(ls)):
#     if ls[i] in dir:
#         dir[ls[i]] +=1
#     else:
#         dir[ls[i]] = 0
# for i in dir:
#     if dir[i]==0:
#         print(i)

sum = sum(ls)
set1 = set(ls)
setsum =0
for i in set1:
    setsum +=i
setsum = setsum*2
ans = setsum-sum
print(ans)