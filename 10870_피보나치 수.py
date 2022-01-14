import sys
N = int(sys.stdin.readline())

def pivo(N):
    if N == 0:
        ans = 0
    elif N == 1:
        ans = 1
    else:
        ans = pivo(N-1) + pivo(N-2)
        
    return(ans)

print(pivo(N))