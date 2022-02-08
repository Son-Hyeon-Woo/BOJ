import sys
shape = list(map(int, sys.stdin.readline().split()))
num_list = []
for i in range(shape[0]):
    num_list.append(sys.stdin.readline().strip())
    
ans = 1
for i,j in enumerate(num_list):
    for a,b in enumerate(j):
        temp = b
        idx = 1
        for k in j[a+1:]:
            if (k == b) & (i+1 + idx <= shape[0]):
                if b == k == num_list[i+idx][a] == num_list[i+idx][a+idx]:
                    if ans < (idx+1)**2:
                        ans = (idx+1)**2
            idx += 1    
print(ans)
        

