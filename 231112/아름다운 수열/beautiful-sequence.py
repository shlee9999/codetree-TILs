import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
m = int(input())
b = [int(input()) for _ in range(m)]
b.sort()
result = []
for i in range(n - m + 1):
    arr = a[i:i + m]
    arr.sort()
    diff = arr[0] - b[0]
    for j in range(m):
        if arr[j] - b[j] != diff:
            break
    else:
        result.append(i+1)
print(len(result))
for x in result:
    print(x)