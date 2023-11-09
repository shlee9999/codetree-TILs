import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]



def dfs(color, x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color and not visited[nx][ny]:
            dfs(color, nx, ny)


def dfs(color, x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color and not visited[nx][ny]:
            dfs(color, nx, ny)


cnt_1 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(graph[i][j], i, j)
            cnt_1 += 1

# 색맹
cnt_2 = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(graph[i][j], i, j)
            cnt_2 += 1

print(cnt_1, cnt_2)