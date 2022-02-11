import sys
import math

N = int(sys.stdin.readline())
num = [sys.stdin.readline().strip() for i in range(N)]

for i in num:
    ans = 1                         # 1로만 이루어지는 경우는 모든 경우에 포함됨
    i = int(i)
    for num_2 in range(1,(i//2)+1):     # 2와 1로 구성되는 경우의 수 and 2로만 구성
        num_1 = (i-(2 * num_2))
        lenght = num_2 + num_1
        num_comb = math.factorial(lenght) / math.factorial(num_2) / math.factorial(num_1)
        ans += num_comb
        
    for num_3 in range(1,(i//3)+1):     # 3과 1로 구성되는 경우의 수 and 3으로만 구성
        num_1 = (i-(3 * num_3))
        lenght = num_3 + num_1
        
        num_comb = math.factorial(lenght) / math.factorial(num_3) / math.factorial(num_1)
        
        ans += num_comb
        
    for num_3 in range(1,(i//3)+1):     # 3과 2와 1로 구성되는 경우의 수 and 3과 2로 구성되는 경우
        temp = (i-(3 * num_3))
        
        for num_2 in range(1,(temp//2)+1):     
            num_1 = (temp-(2 * num_2))
            lenght = num_2 + num_1 + num_3
            num_comb = math.factorial(lenght) / math.factorial(num_2) / math.factorial(num_1) / math.factorial(num_3)
            
            ans += num_comb
            
    print(int(ans))