ar = [0,2,0,254,23,0]

def one():
    for i in range(len(ar)):
        temp = ar[i]
        if temp == 0:
            ar.pop(i)
            ar.append(temp)

    print(ar)

def two():
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if ar[i]==0:
                temp=ar[i]
                ar[i] = ar[j]
                ar[j]=temp

    print(ar)

if __name__ == '__main__':
    one()