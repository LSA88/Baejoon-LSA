
from collections import deque

n,k = map(int, input().split())
array = deque()
result = []

for i in range(1,n+1):
    array.append(i)

while array:
    for _ in range(k-1):
        array.append(array.popleft())
    
    result.append(array.popleft())

print(str(result).replace('[', '<').replace(']', '>'))