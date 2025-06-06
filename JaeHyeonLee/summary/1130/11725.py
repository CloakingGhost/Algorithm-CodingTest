import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

V = int(input())

adj_lst = [[] for _ in range(V+1)]
for _ in range(V - 1):
  u, v = map(int, input().split())
  adj_lst[u].append(v)
  adj_lst[v].append(u)
print(adj_lst)
##################################

parent = [0] * (V + 1)
visited = [0] * (V + 1)
visited[1] = 1

def DFS(p, cur):
  parent[cur] = p
  
  for nxt in adj_lst[cur]:
    if not visited[nxt]:
      visited[nxt] = 1
      DFS(cur, nxt)

print(parent)