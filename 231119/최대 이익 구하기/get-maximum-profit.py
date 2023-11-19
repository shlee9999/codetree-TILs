import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(1, n + 1):
    t, p = map(int, input().split())
    arr.append((i + t, p, i))
arr.sort()

dp = [0] * (n + 2)
last = (0, 0)
for i in range(n):
    e, p, s = arr[i]
    if e > n + 1:
        continue
    for j in range(last[0], e + 1):
        dp[j] = last[1]
    dp[e] = max(dp[e], dp[s] + p)
    last = (e, dp[e])
    
print(dp[n + 1])