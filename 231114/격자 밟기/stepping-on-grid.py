import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
input = sys.stdin.readline
visited = [[False] * 5 for _ in range(5)]
k = int(input())
graph = [[1] * 5 for _ in range(5)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 0  # 0은 벽, 1은 길
    visited[r - 1][c - 1] = True
visited[0][0] = True
visited[4][4] = True
result = 0


def check(x, y):
    if 0 <= x < 5 and 0 <= y < 5 and graph[x][y] and not visited[x][y]:
        return True
    return False


def dfs(x_a, y_a, x_b, y_b):
    global result
    if x_a == x_b and y_a == y_b:
        for x in visited:
            if False in x:
                return
        else:  # 모두 방문하고 딱 만남
            result += 1
            return
    for i in range(4):
        nx_a = x_a + dx[i]
        ny_a = y_a + dy[i]
        for j in range(4):
            nx_b = x_b + dx[j]
            ny_b = y_b + dy[j]
            if check(nx_a, ny_a) and check(nx_b, ny_b):  # 둘 다 이동 가능
                visited[nx_a][ny_a] = True
                visited[nx_b][ny_b] = True
                dfs(nx_a, ny_a, nx_b, ny_b)
                visited[nx_a][ny_a] = False
                visited[nx_b][ny_b] = False


dfs(0, 0, 4, 4)

print(result)