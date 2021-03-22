ls = [2,3,4,1,-1,2,0]
dir= []

def fun(ls,k):
    for i in range(len(ls)):
        try:
            dir.append(max([ls[i] for i in range(k)]))
            ls.pop(0)
        except:
            break
fun(ls,2)
print(dir)
