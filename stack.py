ls = []
rev = []
max = 5
while True:
    num = int(input("1.insert 2.pop 3.display 4.exit 5 reverse\n"))
    if num ==1 and len(ls)<max:
        n = int(input("Data :"))
        ls.append(n)
        continue
    if num == 2 and len(ls)>0:
        ls.pop()
        continue
    if num == 3:
        print("Stack Top-Down :")
        for i in range(len(ls)-1,-1,-1):
            print(ls[i])
        continue
    if num == 4:
        print("bye")
        exit()
    if num == 5:
        for i in range(len(ls)):
            rev.append(ls.pop())
        ls = rev
        print("Stack Top-Down :")
        for i in range(len(ls)-1,-1,-1):
            print(ls[i])