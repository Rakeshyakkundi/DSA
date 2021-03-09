string = 'abc'
for i in range(len(string)):
    temp =f'{string[i]}'
    print(string[i])
    for j in range(i+1,len(string)):
        temp += f'{string[j]}'
        print(temp)