dice = list(map(int, input().split()))
dice.sort();
money = 0


for i in range(3):
    if (dice[0] == dice[1] == dice[2]):
        money = 10000+dice[i]*1000
    elif (dice[0] == dice[1] or dice[1] == dice[2]):
        money = 1000+dice[1]*100
    else:
        money = dice[2]*100

print(money)
