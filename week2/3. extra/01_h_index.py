"""
[정렬/카운팅 - H-Index]

▣ 출처
LeetCode 274. H-Index (Medium)
https://leetcode.com/problems/h-index/

▣ 상황 설명
어떤 연구자가 발표한 논문들의 피인용 횟수가 배열 citations 로 주어집니다.
citations[i] 는 i 번째 논문이 인용된 횟수입니다.

    예)  citations = [3, 0, 6, 1, 5]
         논문 5편이 각각 3회, 0회, 6회, 1회, 5회 인용됨

▣ 목표
이 연구자의 h-index 를 구하세요.

▣ h-index 의 정의
    "인용수가 h 회 이상인 논문이 h 편 이상 있다"
    를 만족하는 h 중에서 가장 큰 값.

  정의를 읽을 때 주의할 점 세 가지
    (1) "h 편 이상"  : 정확히 h 편이 아니라 h 편 이상이면 통과.
    (2) "h 회 이상"  : 등호를 포함한다. h=2 검사에서 2회 인용된 논문도 포함.
    (3) "가장 큰 값" : 조건을 만족하는 h 는 보통 여러 개다. 그중 최댓값을 답한다.

  ※ 위키백과 정의에는 "나머지 n-h 편은 h 회 이하로 인용되었다" 는 조건이
     함께 붙어 있지만, 최댓값을 취하는 순간 이 조건은 자동으로 따라온다.
     (초과하는 논문이 있었다면 h 가 최댓값이 아니게 되므로 모순)
     따라서 실제로 확인할 조건은 위의 한 문장 하나뿐이다.

▣ 답의 범위
    0 <= h <= n     (n = 논문 수)
  - 인용이 하나도 없어도 h = 0 은 항상 성립하므로 "답이 없는 경우" 는 없다.
  - 인용수가 아무리 커도 논문 수보다 큰 h 는 나올 수 없다.
    (citations[i] 는 최대 1000, n 은 최대 5000 이므로 범위를 인용수 쪽에서
     잡으면 어긋난다.)

▣ 예시
    citations = [3, 0, 6, 1, 5]  ->  3
        h=3 : 3회 이상 인용된 논문은 3, 6, 5 → 3편.  3 >= 3  통과
        h=4 : 4회 이상 인용된 논문은 6, 5    → 2편.  2 >= 4  실패
        따라서 답은 3

    citations = [1, 3, 1]  ->  1
        h=1 : 1회 이상 인용된 논문은 1, 3, 1 → 3편.  3 >= 1  통과
        h=2 : 2회 이상 인용된 논문은 3       → 1편.  1 >= 2  실패
        따라서 답은 1

▣ 구현할 함수
h_index(citations: list) -> int
  - 주어진 피인용 배열에 대한 h-index 를 정수로 반환합니다.

▣ 제약
- n == len(citations)
- 1 <= n <= 5000
- 0 <= citations[i] <= 1000
"""
from itertools import count


def h_index(citations: list) -> int:
    """
    피인용 횟수 배열 citations 에 대한 h-index 를 반환.

    예) h_index([3, 0, 6, 1, 5]) == 3
        h_index([1, 3, 1]) == 1
    """
    # TODO: h-index 를 구해서 반환하세요.
    citations.sort(reverse=True)


    n = len(citations)
    count = 0

    for i in range(n):
        if citations[i] >= i+1:
            count += 1


    return count


# ---------------------------------------------------------------------------
# 테스트: 문제의 예시 2개 + 경계 케이스들
# ---------------------------------------------------------------------------
TEST_CASES = [
    # (입력,                    정답,  이 케이스가 잡아내는 것)
    ([3, 0, 6, 1, 5],            3,   "문제 예시 1"),
    ([1, 3, 1],                  1,   "문제 예시 2"),
    ([0],                        0,   "h = 0 처리"),
    ([100],                      1,   "논문 수가 상한 (인용수가 커도 h <= n)"),
    ([0, 0, 0],                  0,   "전부 0"),
    ([2, 2],                     2,   "등호 포함 (h회 '이상')"),
    ([4, 4, 4, 4],               4,   "h == n 인 경우"),
    ([1, 1, 1, 1, 1],            1,   "편수는 많지만 인용이 적음"),
    ([11, 15, 3, 7, 1],          3,   "일반 케이스"),
    ([1, 2, 3, 4, 5, 6],         3,   "큰 값이 많아도 h 는 안 올라감"),
]


if __name__ == "__main__":
    print("[테스트] H-Index")
    print()

    passed = 0
    for citations, expected, note in TEST_CASES:
        got = h_index(list(citations))
        ok = (got == expected)
        passed += ok
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] h_index({citations}) -> {got}  (정답 {expected})")
        if not ok:
            print(f"         ^ {note}")

    print()
    print(f"  {passed} / {len(TEST_CASES)} 통과")
