import sys
cnt = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for i in range(cnt)]

zero = [1,0,1];
one = [0,1,1];

def fibonacci(n) :
    length = len(zero);
    if n  > length-1:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2]);
            one.append(one[i-1] + one[i-2]);
        
    print(f'{zero[n]} {one[n]}')
    return 

for j in num_list:
    fibonacci(j)