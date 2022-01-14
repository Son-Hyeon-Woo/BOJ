from statistics import mean, median
import sys
from collections import Counter
N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for i in range(N)]
num = sorted(num)
print(round(mean(num)))
print(median(num))



if N != 1:
    if Counter(num).most_common()[0][1] == Counter(num).most_common()[1][1]:
        print(Counter(num).most_common()[1][0])
    else:
        print(Counter(num).most_common()[0][0])
        
    print(max(num) - min(num))
    
else :
    print(*num)
    print(0)