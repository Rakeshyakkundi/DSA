ls = [1,5,6,13,19,21,25]
#     0 1 2 3  4  5  6
target = 34 #only two numbers
n = len(ls)
m = {}
for i in range(0,n):
    goal = target - ls[i]
    print('goal',goal)
    if goal in m:
        print(m[goal],i)
        break
    m[ls[i]]=i

print(m)
