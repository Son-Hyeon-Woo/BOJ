import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num = sorted(num)
M = sum(num) / N
temp = 100000
index = 0
for i,j in enumerate(num):
    if temp > abs(M - j):
        temp = abs(M - j)
        index = i

print(num[index])