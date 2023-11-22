import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(10000)

def dfs(data, v, visited):
    # 최초 탐색 위치 True 할당
    visited[v] = True
    # 입력받은 위치를 수열에서 탐색
    next = data[v]
    # 탐색하지 않은 위치면 재귀
    if not visited[next]:
        # 계속 탐색하다가 True를 만나면 탈출
        dfs(data, next, visited)
    return
# 테스트 케이스 횟수 입력
t = int(input())
for _ in range(t):
    result = 0
    # 수열 크기 입력
    n = int(input())
    # 수열이 1부터 시작하기 때문에 탐색 용이를 위해 n+1 배열 생성
    visited = [False] * (n+1)
    # 동일한 이유로 [1]부터 입력
    numList = [0] + list(map(int, input().split()))

    # 전체 배열 탐색
    for i in range(1, n+1):
        # 순열 사이클 하나당 result + 1
        if not visited[i]:
            dfs(numList, i, visited)
            result += 1
    print(result)