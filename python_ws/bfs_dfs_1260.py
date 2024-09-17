from collections import deque

# n: 정점의 개수, m: 간선의 개수, v: 탐색할 정점의 번호
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def bfs(graph, start_node):
    
    # 방문 여부 리스트 및 큐 정의
    visited = []
    bfs_q = deque()

    # 시작 노드를 큐에 넣기
    bfs_q.append(start_node)
    visited.append(start_node)

    # bfs_q가 존재한다면
    while bfs_q:
        # 큐에서 가장 앞의 놈 빼기
        node = bfs_q.popleft()
        
        # 인접한 놈들 중에 방문 안했던 놈 (낮은 번호를 우선 탐색)
        if graph[node]:
            reversed_graph = sorted(graph[node], reverse=False)

            for node_i in reversed_graph:
                if node_i not in visited:
                    visited.append(node_i)
                    bfs_q.append(node_i)
    
    return visited
                

def dfs(graph, start_node):

    # 방문 여부 리스트 및 큐 정의
    visited = []
    dfs_q = deque()

    # 시작 노드를 큐에 넣기
    dfs_q.append(start_node)

    # dfs_q가 아직 존재한다면
    while dfs_q:
        # 시작 노드 지정
        node = dfs_q.pop()

        # 만약 visited에 없다면
        if node not in visited:
            # visited 에 노드 추가
            visited.append(node)
            # 인접 노드들을 큐에 추가 (낮은 번호를 우선 탐색)
            if graph[node]:
                reversed_graph = sorted(graph[node], reverse=True)
                dfs_q.extend(reversed_graph)
    
    return visited

for i in dfs(graph, v):
    print(i, end=' ')

print("")

for i in bfs(graph, v):
    print(i, end=' ')


