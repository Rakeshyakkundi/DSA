test_case = int(input())

def output(S,K,N):
    good_well = 0
    for  i in range(int(len(S)/2)):
        s1 = i
        s2 = N-i+1
        if S[s1] != S[s2]:
            good_well += 1
    return good_well
        


while True:
    ls = []
    if test_case !=0:
        N = int(input())
        k = int(input())
        S = input()
        ls. append(output(S,k,N))
        break
    test_case = test_case -1

for i in range(len(ls)):
    print(f"case#{i+1}:",ls[i])
