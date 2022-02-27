import sys
import math
num_list = list(map(int, sys.stdin.readline().split()))

startnum1 = num_list[1]
startnum2 = num_list[2]
cnt = 0

while True:
    cnt += 1;
        
    if (startnum1 % 2 == 1) & (startnum1 + 1 == startnum2):
        print(cnt)
        break

    startnum1 = math.ceil(startnum1 / 2)
    startnum2 = math.ceil(startnum2 / 2)
    
