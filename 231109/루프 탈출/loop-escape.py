import sys

input = sys.stdin.readline
n = int(input())

graph = [0] * (n + 1)
loop = [False] * (n + 1)
stack = []


def is_loop(v):
    visited = [False] * (n + 1)

    while True:
        visited[v] = True
        next = graph[v]
        if next == 0:
            return False
        if visited[next]:
            return True
        v = next


for start in range(1, n + 1):
    graph[start] = int(input())

cnt = 0
for i in range(1, n + 1):
    if is_loop(i):
        cnt += 1

result = n - cnt

print(result)