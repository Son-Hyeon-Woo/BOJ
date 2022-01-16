import sys
N,M = map(int, sys.stdin.readline().split())
numLi = []
for i in range(N):
    numLi.append(sys.stdin.readline().split())
a,b = N,M

for i in numLi:
    if 'X' in i[0]:
        a -= 1
    
for i in range(M):
    for j in range(N):
        # print(numLi[j][0][i])
        if numLi[j][0][i] == 'X':
            b-=1
            break
        
if a > b:
    print(a)
else :
    print(b)