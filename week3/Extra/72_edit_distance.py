r"""
[LeetCode 72 - Edit Distance / 편집 거리]
난이도: Medium (체감은 Hard 쪽입니다)
https://leetcode.com/problems/edit-distance/

▣ 문제
문자열 word1 을 word2 로 바꾸는 데 필요한 **최소 연산 횟수**를 반환하세요.
쓸 수 있는 연산은 세 가지입니다.

  - 글자 하나 삽입 (insert)
  - 글자 하나 삭제 (delete)
  - 글자 하나 교체 (replace)

▣ 예시
    word1 = "horse", word2 = "ros"
    출력: 3

        horse -> rorse   ('h' 를 'r' 로 교체)
        rorse -> rose    ('r' 삭제)
        rose  -> ros     ('e' 삭제)

    word1 = "intention", word2 = "execution"
    출력: 5

        intention -> inention   ('t' 삭제)
        inention  -> enention   ('i' 를 'e' 로 교체)
        enention  -> exention   ('n' 을 'x' 로 교체)
        exention  -> exection   ('n' 을 'c' 로 교체)
        exection  -> execution  ('u' 삽입)

▣ 제약
- 0 <= len(word1), len(word2) <= 500     ← 0 입니다. 빈 문자열이 들어옵니다.
- 둘 다 소문자 알파벳뿐

▣ 이번엔 다른 점
124 번은 재귀가 무엇을 돌려줄지를 정하는 문제였습니다.
이번엔 **표(table)의 칸 하나가 무슨 뜻인지**를 정하는 문제입니다.

그리고 지금까지 푼 DP 와 달리 **상태가 2차원**입니다. 상태 하나를 가리키려면
정수가 두 개 필요해요. word1 을 어디까지 봤는지(i), word2 를 어디까지 봤는지(j).
상태를 정하고 나면 "이 상태로 오는 길이 몇 가지인가"만 따지면 됩니다.

칸의 뜻을 한 문장으로 못 적으면 코드는 절대 안 나옵니다.
반대로 그 한 문장이 나오면 나머지는 거의 기계적입니다. 정의부터 적으세요.
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        if n == 0:
            return m
        elif m == 0:
            return n

        for x in range(n + 1):
            for y in range(m + 1):
                if x == 0:
                    dp[0][y] = y
                    continue
                elif y == 0:
                    dp[x][0] = x
                    continue
                if word2[y - 1] == word1[x - 1]:
                    dp[x][y] = dp[x - 1][y - 1]
                else:
                    dp[x][y] = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1

        return dp[n][m]

        # TODO: 여기에 구현하세요.
        #
        # 코드를 치기 전에 답해볼 질문들:
        #
        #  - 먼저 dp[i][j] 가 무엇을 뜻하는지 **한 문장으로** 적으세요.
        #    두 문자열을 통째로 비교하려 하지 말고, 앞에서 몇 글자까지만 잘라서
        #    본다고 생각하면 문장이 나옵니다. 이 문장이 이 문제의 전부입니다.
        #
        #  - 정의를 적었으면 표의 크기를 정할 수 있습니다. 그런데 len(word1) x len(word2)
        #    로 잡으면 "한쪽이 빈 문자열인 경우"를 적어둘 칸이 없습니다.
        #    몇 칸짜리 표가 필요한가요?
        #
        #  - 빈 문자열 자리부터 채워보세요. word1 이 비어 있고 word2 가 3글자라면
        #    답이 몇인가요? 그 반대는요? 이 두 줄(첫 행과 첫 열)은 계산 없이 바로 적을 수
        #    있습니다. 여기가 출발점입니다.
        #
        #  - 이제 가운데 칸입니다. dp[i][j] 를 채우는 시점에 **이미 값이 적혀 있는 칸**은
        #    어디어디인가요? 표를 왼쪽 위부터 채워나간다고 할 때 손가락으로 짚어보세요.
        #    그 칸들과 세 연산(삽입/삭제/교체)을 하나씩 짝지으면 점화식이 나옵니다.
        #
        #  - word1 과 word2 의 지금 보고 있는 글자가 **같다면** 연산이 필요한가요?
        #    이 경우가 왜 위의 세 가지와 따로 처리돼야 하는지 한 줄 적어두세요.
        #
        #  - 표의 칸이 몇 개이고 칸 하나 채우는 데 몇 번 계산하나요?
        #    500 x 500 이면 총 몇 번인지 계산해두세요.

# ─────────────────────────────────────────────────────────────
#  로컬 테스트
#  LeetCode 에 낼 때는 위의 class Solution 부분만 복사해서 붙이면 됩니다.
# ─────────────────────────────────────────────────────────────

fails = 0


def check(w1, w2, expected, label=""):
    global fails
    got = Solution().minDistance(w1, w2)
    ok = got == expected
    if not ok:
        fails += 1
    print(f"  [{' OK ' if ok else 'FAIL'}] {label}")
    print(f"         word1={w1!r}")
    print(f"         word2={w2!r}")
    print(f"         기대 {expected}  실제 {got}")
    print()


if __name__ == "__main__":
    print("[LeetCode 제공 예시]")
    check("horse", "ros", 3, "예시 1")
    check("intention", "execution", 5, "예시 2")

    print("[직접 채울 테스트]")
    # 아래 다섯 칸은 비워뒀습니다. 어떤 입력이 이 코드를 깨뜨릴지 직접 고르세요.
    # 기대값은 손으로 먼저 세서 적고, 그 다음에 돌리세요.
    # 라벨은 서로 다르게 붙여야 FAIL 났을 때 어느 쪽인지 보입니다.
    #
    # 이런 축들이 있습니다 (전부 쓸 필요는 없습니다):
    #   · 한쪽이 빈 문자열이면? 제약이 0 부터라 반드시 들어옵니다.
    #     LeetCode 예시에는 없어서 그냥 넘기기 쉬운데, 여기서 제일 많이 터집니다.
    #   · 양쪽 다 빈 문자열이면?
    #   · 두 문자열이 완전히 같으면?
    #   · 공통 글자가 하나도 없으면? 길이가 다르면 답이 어느 쪽 길이일까요?
    #   · 길이는 같은데 한 글자만 다르면?
    #   · 500 글자 두 개면 시간 안에 끝나나요?
    #     -> check("a" * 500, "b" * 500, 500, "최대크기")
    #        이건 답을 미리 적어뒀습니다. 전부 교체하면 되니까요.
    #
    check("", "exec", 4, "하나가 빈")
    check("", "", 0, "두개가 빈")
    check("aaaqqqq", "ddddd", 7, "모두다른")
    check("apple", "applc", 1, "하나만 다른")
    check("eat", "sea", 2, "예시 1")





    print(f"실패 {fails}개" if fails else "전부 통과했습니다")
