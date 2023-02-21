
import sys
input = sys.stdin.readline
card_num = int(input())
mycard = set(map(int,input().split()))
compare_num = int(input())
compare_card= list(map(int,input().split()))



for i in range(compare_num):
    if compare_card[i] in mycard : 
        print(1,end=' ')
    else : print(0,end=' ')