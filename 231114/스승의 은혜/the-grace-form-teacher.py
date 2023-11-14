n, b = map(int, input().split())
ps = [list(map(int, input().split())) for _ in range(n)]
ps_sum = [(sum(ps[i]), ps[i][0] * 0.5 + ps[i][1]) for i in range(n)]
ps_sum.sort()
s = 0
cnt = 1
result = -1

for i in range(n):
    s += ps_sum[i][0]
    if s > b:
        if cnt == 0:
            result = i
            break
        s = s - ps_sum[i][0] + ps_sum[i][1]
        if s > b:
            result = i
            break
        elif s == b:
            result = i + 1
            break
print(result)