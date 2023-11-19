import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(1, n + 1):
    t, p = map(int, input().split())
    arr.append((i + t, p, i))
arr.sort()

dp = [0] * (n + 2)
for i in range(n):
    e, p, s = arr[i]
    if e > n + 1:
        continue
    dp[e] = max(dp[e], dp[s] + p)
    if i < n - 1:
        if arr[i + 1][0] <= n + 1:
            for j in range(e, arr[i + 1][0] + 1):
                dp[j] = dp[e]
print(dp[n + 1])