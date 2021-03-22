arr1 = [0,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,1,0,0,1,0]
arr2 = [0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,0,0]

sub_str1 = []
sub_str2 = []

str1 = '';str2 = ''
for i in range(len(arr1)):
    str1 = f'{arr1[i]}'
    str2 = f'{arr2[i]}'
    for j in range(i+1,len(arr1)):
        str1 += f'{arr1[j]}'
        str2 += f'{arr2[j]}'
        sub_str2.append(str2)
        sub_str1.append(str1)
        

dir = {}

for i in range(len(sub_str1)):
    if sub_str1[i] in sub_str2:
        dir[sub_str1[i]]= len(sub_str1[i])

max=0;str_max = ''
for i in dir:
    if dir[i] > max:
        max = dir[i]
        str_max = i
   
print(str_max,max)
for i in dir:
    print(i,":",dir[i],"\n")