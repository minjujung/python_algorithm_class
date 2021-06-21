import sys

input = sys.stdin.readline

number = int(input())

stairs_num = []
for i in range(number):
    num = int(input())
    stairs_num.append(num)

dp = []

if number == 1:
    print(stairs_num[0])
    exit()
elif number == 2:
    print(stairs_num[0] + stairs_num[1])
    exit()

dp.append(stairs_num[0])
dp.append(stairs_num[0] + stairs_num[1])
dp.append(max(stairs_num[0], stairs_num[1]) + stairs_num[2])
for i in range(3, number):
    dp.append(max(dp[i - 2] + stairs_num[i], dp[i - 3] + stairs_num[i - 1] + stairs_num[i]))

print(dp[len(dp) -1])