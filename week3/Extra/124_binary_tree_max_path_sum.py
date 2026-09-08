r"""
[LeetCode 124 - Binary Tree Maximum Path Sum / 이진 트리 최대 경로 합]
난이도: Hard
https://leetcode.com/problems/binary-tree-maximum-path-sum/

▣ 문제
이진 트리에서 **경로(path)** 란 노드를 죽 이어놓은 것인데, 이웃한 두 노드 사이에는
반드시 간선이 있어야 하고, 같은 노드를 두 번 지날 수는 없습니다.
경로의 합은 그 경로에 들어 있는 노드 값들을 전부 더한 값입니다.

root 가 주어질 때, **비어 있지 않은 경로** 중 합이 가장 큰 값을 반환하세요.
경로가 루트를 지나야 한다는 조건은 없습니다.

▣ 예시
    입력: root = [1,2,3]

            1
           / \
          2   3

    출력: 6
    설명: 2 -> 1 -> 3 이 최선이고 합은 2 + 1 + 3 = 6 입니다.

    입력: root = [-10,9,20,null,null,15,7]

           -10
           /  \
          9    20
              /  \
            15    7

    출력: 42
    설명: 15 -> 20 -> 7 이 최선이고 합은 42 입니다.
          루트인 -10 은 아예 안 지나갑니다. 지나면 손해라서요.

▣ 제약
- 노드 개수는 1 개 이상 3 * 10^4 개 이하
- -1000 <= 노드 값 <= 1000     ← 음수가 들어옵니다. 이게 이 문제의 절반입니다.

▣ 이번엔 다른 점
208 번에서는 자료구조를 설계했다면, 이번엔 **재귀 함수가 무엇을 돌려줄지** 를 설계합니다.
이 한 문장만 제대로 정하면 나머지는 열 줄이 안 됩니다. 거꾸로, 이걸 안 정하고 시작하면
아무리 오래 붙잡아도 안 풀립니다. 그러니 코드보다 정의를 먼저 적으세요.
"""

from typing import Optional
from collections import deque


class TreeNode:
    """LeetCode 가 제공하는 노드입니다. 그대로 쓰시면 됩니다."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]):

        def maxpathsum_(root: Optional[TreeNode]) -> int:
            """
            root: 트리의 루트 노드 (노드가 최소 1개는 있습니다)
            반환: 가장 큰 경로 합
            """
            # TODO: 여기에 구현하세요.
            #
            # 코드를 치기 전에 답해볼 질문들:
            #
            #        - 이 문제의 전부는 "경로가 한 노드에서 꺾일 수 있다" 는 것입니다.
            #    예시 1 의 2 -> 1 -> 3 은 1 에서 꺾인 경로이고, 예시 2 의 15 -> 20 -> 7 도
            #    20 에서 꺾인 경로입니다. 꺾인 경로와 안 꺾인 경로가 무엇이 다른지
            #    한 문장으로 적고 시작하세요.
            #
            #  - 재귀 함수를 하나 만든다고 해봅시다. 그 함수가 **부모에게 돌려주는 값** 을
            #    한 문장으로 정의해보세요. 힌트는 이겁니다: 꺾인 경로를 부모에게 돌려주면
            #    부모가 그걸 자기 경로에 이어붙일 수 있나요? 안 된다면, 돌려줄 수 있는 건
            #    무엇인가요? 208 번의 "노드가 무엇을 들고 있어야 하나" 에 해당하는 질문입니다.
            #
            #  - 위 정의를 적고 나면 이상한 걸 발견하게 됩니다. 정답(꺾인 경로가 될 수도 있는
            #    그 값)은 그 반환값으로 표현이 안 됩니다. 그러면 정답은 어디에 모아둬야 하나요?
            #    돌려주는 값과 모아두는 값이 서로 다르다는 것, 이게 이 문제의 핵심입니다.
            #
            #  - 노드 하나를 몇 번 방문하나요? 그 답이 곧 시간복잡도입니다.
            if root.left is None:
                left = 0
            else:
                left = maxpathsum_(root.left)
                if left <= 0: left = 0
            
            if root.right is None:
                right = 0
            else:
                right = maxpathsum_(root.right)
                if right <= 0: right = 0


            if right >= left:
                maximum = right
            else:
                maximum = left

            result.append(root.val + right + left)
            return root.val + maximum


        result = []
        maxpathsum_(root)
        return max(result)

# ─────────────────────────────────────────────────────────────
#  로컬 테스트
#  LeetCode 에 낼 때는 위의 class Solution 부분만 복사해서 붙이면 됩니다.
#  (TreeNode 는 LeetCode 쪽에 이미 있으니 안 넣어도 됩니다.)
#
#  build() 는 LeetCode 의 [1,2,null,3] 표기를 실제 트리로 바꿔주는 도구입니다.
#  파이썬이라 null 대신 None 을 씁니다.
# ─────────────────────────────────────────────────────────────

fails = 0


def build(vals):
    """레벨 순서 리스트를 트리로 만듭니다. None 은 '자식 없음' 입니다."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        for side in ("left", "right"):
            if i >= len(vals):
                break
            v = vals[i]
            i += 1
            if v is not None:
                child = TreeNode(v)
                setattr(node, side, child)
                q.append(child)
    return root


def skewed(n, val=1):
    """왼쪽으로만 n 개 이어진 트리를 만듭니다. 깊이 테스트용입니다."""
    root = TreeNode(val)
    node = root
    for _ in range(n - 1):
        node.left = TreeNode(val)
        node = node.left
    return root


def check(vals, expected, label=""):
    global fails
    root = vals if isinstance(vals, TreeNode) else build(vals)
    got = Solution().maxPathSum(root)
    ok = got == expected
    if not ok:
        fails += 1
    print(f"  [{' OK ' if ok else 'FAIL'}] {label}")
    if not isinstance(vals, TreeNode):
        print(f"         입력 {vals}")
    print(f"         기대 {expected}  실제 {got}")
    print()


if __name__ == "__main__":
    print("[LeetCode 제공 예시]")
    check([1, 2, 3], 6, "예시 1")
    check([-10, 9, 20, None, None, 15, 7], 42, "예시 2")

    print("[직접 채울 테스트]")
    # 아래 다섯 칸은 비워뒀습니다. 어떤 트리가 이 코드를 깨뜨릴지 직접 고르세요.
    # 기대값은 손으로 먼저 더해서 적고, 그 다음에 돌리세요.
    # 라벨은 서로 다르게 붙여야 FAIL 났을 때 어느 쪽인지 보입니다.
    #
    # 이런 축들이 있습니다 (전부 쓸 필요는 없습니다):
    #   · 노드가 딱 하나뿐인 트리는?
    #   · 값이 전부 음수인 트리는? 답도 음수가 될 수 있다는 걸 잊지 마세요.
    #   · 최적 경로가 루트를 아예 안 지나는 트리는? (예시 2 가 그런 경우입니다)
    #   · 자식이 한쪽에만 있는 노드는?
    #   · 한쪽으로만 3만 개 이어진 트리는? -> check(skewed(30000), 30000, "깊은트리")
    #     이건 답을 미리 적어뒀습니다. 값이 전부 1 이니까요. 돌려보면 알게 됩니다.
    #
    check([5], 5, "")
    check([-3], -3, "")
    check([-1,-2,-3], -1, "")
    check([-1,3,-3], 3, "")



    # check([...], ..., "설명")
    # check([...], ..., "설명")
    # check([...], ..., "설명")
    # check([...], ..., "설명")

    print(f"실패 {fails}개" if fails else "전부 통과했습니다")
