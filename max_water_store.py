ls = [1,8,6,2,5,4,8,3,7]
maxarea = 0 
l = 0
r = len(ls)-1

while(l<r):
    # print(ls[l],ls[r],r,l)
    maxarea = max(maxarea,min(ls[l],ls[r])*(r-l))
    if(ls[l]<ls[r]):
        l +=1
    else:
        r -=1

print(maxarea)

