from collections import deque

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]


# BFS 메서드 정의
def bfs():
        
    # 노드의 순서 저장할 큐
    queue = deque()

    # 출발점 위치를 큐에 삽입
    queue.append(n)

    # bfs 큐 생성
    while queue:

        # 큐에서 꺼내기
        x = queue.popleft()

        # K와 같으면 그 떄의 depth를 출력하고 종료
        if x == k:
            print(visited[x])
            break

        # 3갈래의 좌표 유효성을 판단해서 큐에 넣기
        for j in (x-1, x+1, 2*x):
            # 주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0 <= j <= 100000 and not visited[j]:
                # 이동한 위치에 현재 이동한 시간 표시
                visited[j] = visited[x] + 1
                # 큐에 추가
                queue.append(j)

bfs()

