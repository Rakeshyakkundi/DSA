st = "abcadbabcde"
# m = {}
# left = 0
# right = 0
# ans = 0
# n = len(st)
# while left<n and right<n:
#     el = st[right]
#     if el in m:
#         left = max(left,m[el]+1)
#     m[el]=right
#     ans = max(ans,right-left+1)
#     right +=1
# print(m)

ls = []
for i in range(len(st)):
    temp = ''
    temp += st[i]
    for j in range(i+1,len(st)):
        temp +=st[j]
        if temp not in ls:
            ls.append(temp)

git = []
# print(ls)
for i in ls:
    dir = {}
    for j in i:
        if j in dir:
            dir[j] +=1
        else:
            dir[j] = 0
    le = 0
    for k in dir:
        if dir[k] >0:
            le = 1
    if le == 0:
        st = ''
        for i in dir:
            st +=i
        git.append(st)  
len_max = 0
string =''
for i in git:
    a = len(i)
    if a>len_max:
        string = i
        len_max =a
print(string,len(string))