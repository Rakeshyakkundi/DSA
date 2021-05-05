ls = [1,4,5,6,11,11,11,11,21,26,28,29]
# start = 0;buz =1
# end = 0
# for i in range(len(ls)):
#     if ls[i]==11 and buz == 1:
#         start =i
#         buz = 0
#     elif ls[i-1]==11 and ls[i] != 11:
#         end = i-1

# print(start,end)

left = 0
right =len(ls)-1
while(left<=right):
    if ls[left] != 11:
        left +=1
    elif ls[right]!=11:
        right -=1
    else:
        break 

print(left,right)

