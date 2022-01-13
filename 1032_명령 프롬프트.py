import sys
N = int(sys.stdin.readline())
ans = [sys.stdin.readline().strip() for i in range(N)]

a = list(ans[0])
for i in range(1,N):
    b = list(ans[i])
    for j in range(len(a)):
        if a[j] != b[j]: 
            a[j] = "?"
        else:
            a[j] = a[j]
print(''.join(a))