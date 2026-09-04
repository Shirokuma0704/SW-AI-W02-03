"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

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
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO ① — visited 준비
    #   이 함수는 자기 자신을 계속 불러. 그래서 방문 기록은
    #   모든 호출이 같은 것 하나를 공유해야 의미가 있어.
    #   맨 처음 호출일 때만(= visited가 아직 없을 때만) 새로 만들고,
    #   그 뒤로는 넘겨받은 걸 그대로 쓴다.
    if visited is None: visited = []

    # TODO ② — 지금 서 있는 정점을 방문 처리
    #   재귀로 이 함수에 들어왔다 = start에 도착했다는 뜻이야.
    #   방문 순서에 남긴다.
    visited.append(start)

    # TODO ③ — 이웃들로 더 깊이 내려가기
    #   현재 정점의 이웃을 하나씩 보면서, 아직 안 가본 이웃이면
    #   그쪽으로 자기 자신을 다시 호출한다.
    #   그 호출이 끝까지 갔다 돌아오면 그때 다음 이웃 차례.

    for x,y in enumerate(graph[start]):
        if y not in visited:
            dfs(graph,y,visited)

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

    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


