import sys

input = input = sys.stdin.readline

def find(x):
    if root_lst[x] == x:
        return x
    return find(root_lst[x])
        
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    
    if x_root < y_root:
        root_lst[y_root] = x_root
    else: 
        root_lst[x_root] = y_root

N = int(input())
M = int(input())
root_lst = [i for i in range(N)]

for y in range(N):
    con_info = list(map(int, input().split()))
    for x in range(N):
        if con_info[x] == 1:
            union(x, y)

plans = list(map(int, input().split()))
root_set = set([find(p - 1) for p in plans])
if len(root_set) > 1:
    print("NO")
else:
    print("YES")