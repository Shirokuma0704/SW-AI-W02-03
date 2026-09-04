"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []
    
    # TODO ① — 출발선 세팅
    #   BFS는 "발견은 했는데 아직 안 들여다본 정점"을 줄 세워두고
    #   하나씩 꺼내 처리하는 방식이야. 그 대기줄을 하나 만들고,
    #   시작 정점을 첫 손님으로 세워두면 준비 끝.
    #   그리고 이미 발견한 정점이 뭐였는지 적어둘 곳도 하나 필요해.
    queue = deque([start])
    discovered = {start}


    # TODO ② — 대기줄이 빌 때까지 반복
    #   줄이 비었다 = 더 갈 곳이 없다 = 탐색 끝.
    #   한 바퀴 도는 동안 하는 일은 세 가지야.
    #     · 줄에서 정점 하나를 꺼낸다
    #     · 그 정점의 이웃 목록을 훑는다
    #     · 그중 아직 발견 안 된 이웃만 줄 뒤에 세운다
    while queue:
        node = queue.popleft()
        visited.append(node)

        for neighbor in graph[node]:
            if neighbor not in discovered:
                discovered.add(neighbor)
                queue.append(neighbor)

    
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

