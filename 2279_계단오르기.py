import sys
x = int(sys.stdin.readline())
num_list = [0] + [int(sys.stdin.readline()) for _ in range(x)]
ans = []

index = -x;
ans.append(num_list[index])
while True:
    
    if num_list[x-1] > num_list[x-2]:
        ans.append(num_list[x-1])
        index -= 1
        
    elif num_list[x-1] < num_list[x-2]:
        ans.append(num_list[x-2])
        index -= 2    