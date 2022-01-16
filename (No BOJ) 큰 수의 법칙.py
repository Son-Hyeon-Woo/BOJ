from re import M
import sys
N,M,K = map(int, sys.stdin.readline().split())
numLi = list(map(int, sys.stdin.readline().split()))
numLi.sort(reverse=True)
maxNum = numLi[0]
nextNum = numLi[1]

x = M // (K + 1)
y = M % (K + 1)

print(maxNum, nextNum, x, y)
print((maxNum*(K) + nextNum) * x + (maxNum * y))