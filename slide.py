def one():
    ls = [2,3,4,1,-1,2,0]
    dir= []

    def fun(ls,k):
        for i in range(len(ls)):
            try:
                dir.append(max([ls[i] for i in range(k)]))
                ls.pop(0)
            except:
                break
    fun(ls,4)
    print(dir)
def two():
    ls = [3,4,56,1,0]
    for i in range(len(ls)-2):
        ls[i] = ls[i]+ls[i+1]+ls[i+2]
    for i in range(len(ls)-2,len(ls)):
        ls.pop()
    print(ls)

if __name__ =='__main__':
    print("One :")
    one()
    print("Two :")
    two()