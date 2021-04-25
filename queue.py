# reverse queue
qu = [1,2,3,4,5]
end = len(qu)
for i in range(len(qu)):
    temp = qu[0]
    qu[0] = None
    for j in range(end-1):
        qu[j]=qu[j+1]
    qu[end-1] = temp
    end -=1
print(qu)




#  1    2   3   4   5
#  temp = 1
#       2    3    4   5
#  2    3    4    5  
#  2    3    4    5   1
# temp = 2
#       3    4    5   1
#  3    4    5        1
#  3    4    5    2   1
# temp = 3
#       4    5    2   1
#  4    5         2   1
#  4    5    3    2   1
# temp = 4
#       5    3    2   1
#  5         3    2   1
#  5    4    3    2   1
# temp = 5
#       4    3    2   1
#       4    3    2   1
#  5    4    3    2   1
