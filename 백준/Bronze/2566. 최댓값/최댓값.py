array = []

for arr in range(9):
    arr = list(map(int, input().split()));
    array.append(arr)

max_value = max(map(max, array))
print(max_value)

for i in range(9):
    for j in range(9):
        if array[i][j] == max_value :
            print(i+1, j+1)

