import sys
import math
N = int(sys.stdin.readline())
li = []
for i in range(N):
    li.append(sys.stdin.readline().split())
for i in li:
    L,R = int(i[0]),int(i[1])
    ans = math.factorial(int(i[1])) / (math.factorial(int(i[1]) - int(i[0])) * math.factorial(int(i[0])))
    ans = int(ans)
    print(ans)
