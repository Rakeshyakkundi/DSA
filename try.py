
# one
st = 10;ed = 30

def check(num):
    prime = 'y'
    for  i in range(2,num):
        if num%i == 0:
            prime = 'n'
            break
    if prime == 'y':
        return num

def prime(st,ed):
    count = []
    for i in range(st,ed+1):
        accept = check(i)
        if accept != None:
            count.append(accept)
    # print(count)
    print(len(count))

prime(st,ed)

# two
st = 'privin'
dir = {}
for i in range(len(st)):
    if st[i] not in dir:
        dir[st[i]] = 0
    else:
        dir[st[i]] +=1
count = []
for i in dir:
    if dir[i]==0:
        count.append(i)
# print(count)
print(len(count))


