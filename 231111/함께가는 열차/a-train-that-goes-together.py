import sys
input = sys.stdin.readline
n = int(input())
speed = []
for _ in range(n):
    start, sp = map(int, input().split())
    speed.append(sp)
result = 1

for i in range(n - 1, 0, -1):
    if speed[i - 1] > speed[i]:
        speed[i - 1] = speed[i]
    else:
        result += 1
print(result)