a = [7,5,2,3,4];j=0;store=0;r=True
le = len(a)
mid = int(le/2)
left = max(a[0:mid])
right = max(a[mid:len(a)])
print('left right',left,right)
for i in range(len(a)):
    j +=1
    if a[i]==left:
        while(j):
            print(a[j])
            temp = left - a[j]
            if temp >0:
                store = store + temp
            try:
                r = False
                if a[j+1]==right:
                    print('water can be store is  :',store)
                    exit(0)
            except:
                if r==True:
                    print('water can be store is :',store)
                exit(0)
            j = j+1
