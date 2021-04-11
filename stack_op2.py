ls = []
max = 3
while(1):
    n = int(input("Enter 1.input 2.pop 3.display 4.exit :\n"))
    if n ==1:
        if len(ls)<max:
            num = int(input("enter :"))
            ls.append(num)
        else:
            print(f"max is {max} num")
    elif n == 2:
        if len(ls)>0:
            ls.pop()
            print(ls)
        else:
            print("stack is empty")
    elif n == 3:
        if len(ls)<=0:
            print("stack is empty")
        else:
            print()
            for i in range(len(ls),0,-1):
                print(ls[i-1])
        break

# infix  a op b
#  eg : 1 + 2

# postfix a b op
#  eg : 1 2 +

#  a op1 b op2 c op3 d
#     +     *     +
#  BODMAS

