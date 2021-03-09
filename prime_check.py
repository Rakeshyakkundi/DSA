def fun_c(a):
    r = True
    for i in range(2,a):
        if a%i==0:
            r = False
            pass
    if r == True:
        print('Prime',a)

for j in range(2,100):
    fun_c(j)