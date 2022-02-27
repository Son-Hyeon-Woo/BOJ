import sys
x = int(sys.stdin.readline())

cnt = [0] + [0] * x

for i in range(2,x+1):
    cnt[i] = cnt[i-1] + 1
    
    if i % 3 == 0:
        cnt[i] = min(cnt[i//3]+1, cnt[i])
    
    if i % 2 == 0:
        cnt[i] = min(cnt[i//2]+1, cnt[i])

print(cnt[x])

