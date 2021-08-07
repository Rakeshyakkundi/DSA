# test_case = int(input())

# def output(S,K,N):
#     good_well = 0
#     for  i in range(int(len(S)/2)):
#         s1 = i
#         s2 = N-i+1
#         if S[s1] != S[s2]:
#             good_well += 1
#     return good_well
        


# while True:
#     ls = []
#     if test_case !=0:
#         N = int(input())
#         k = int(input())
#         S = input()
#         ls. append(output(S,k,N))
#         break
#     test_case = test_case -1

# for i in range(len(ls)):
#     print(f"case#{i+1}:",ls[i])



# ls = [8,4,6,12]
# ls.sort()
# part = []
# while True:
#     if len(ls) <=0:
#         break
#     print(ls)
#     try:
#         a1 = ls.pop(0)
#         a2 = ls.pop(0)
#         sum =a1+a2
#         part.append(sum)
#         ls.append(sum)
#         ls.sort()
#     except:
#         print(part)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    for i in range(d):
        first = a.pop(0)
        a.append(first)
    return a
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)
