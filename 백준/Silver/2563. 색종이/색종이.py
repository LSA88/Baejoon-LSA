array = [[0] * 101 for i in range(101)]

num = int(input())

for n in range(num):
    x,y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1

result = 0
for arr in array:
    result += arr.count(1)

print(result)