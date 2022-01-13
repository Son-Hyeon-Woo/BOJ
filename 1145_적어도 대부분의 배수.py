import sys
a,b,c,d,e = map(int,sys.stdin.readline().split())
# a,b,c,d,e = 30,45,23,26,56


startNum = min(a,b,c,d,e)
cnt = 0
while cnt < 3 :
    cnt = 0
    if startNum % a == 0:
        cnt += 1
        
    if startNum % b == 0:
        cnt += 1
        
    if startNum % c == 0:
        cnt += 1
        
    if startNum % d == 0:
        cnt += 1
    if startNum % e == 0:
        cnt += 1
    startNum += 1
print(startNum-1)