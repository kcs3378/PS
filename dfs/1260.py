from collections import deque

def dfs(data, v, visited):
    visited[v] = 1 # 해당 v값 방문 처리
    print(v, end=" ")
    for i in range(1, n + 1):
        # i 값을 방문하지 않았고, v와 연결이 되어 있다면
        if visited[i] == 0 and data[v][i] == 1:
            # 해당 i 값으로 탐색
            dfs(data, i, visited)

def bfs(data, v, visited):
  q = deque([v]) # pop 메서드의 메서드 사용       
  visited[v] = 1 # 해당 v값을 방문 처리
  while q: # q가 빌 때까지 실행
    v = q.popleft() # 큐에 있는 첫번 째 값
    print(v, end = " ")
    for i in range(1, n + 1):
      # 만약 해당 i값을 방문하지 않았고 v와 연결이 되어 있다면
      if visited[i] == 0 and data[v][i] == 1:
        q.append(i) # 그 i값을 추가
        visited[i] = 1 # i 값을 방문처리 

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited_list = [0] * (n + 1) # 방문 기록용 리스트
visited_list2 = [0] * (n + 1) # 방문 기록용 리스트

# 탐색용 그래프
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(graph, v, visited_list)
print()
bfs(graph, v, visited_list2)
