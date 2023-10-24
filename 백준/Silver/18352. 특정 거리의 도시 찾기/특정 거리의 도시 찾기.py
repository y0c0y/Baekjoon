import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)

distance = [-1] * (n + 1)
distance[x] = 0
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)
