"""
[드릴 2] 이분 탐색 변형  ᕕ( ᐛ )ᕗ

이미 짜 봤던 것   : 정확히 일치하는 값 찾기 (10_binary_search.py)
이번에 직접 짤 것 : lower_bound, upper_bound, count_occurrences, max_unit_length

네 개 다 while 뼈대는 거의 똑같아요. 진짜로 다른 건 딱 두 군데예요.
  - 조건이 <= 냐 < 냐
  - 돌려주는 게 mid 냐 left 냐

그 한 글자 차이를 눈으로 읽으면 다 아는 것 같은데, 손으로 짜면 꼭 한 번은
무한 루프가 나요. 그 한 번을 오늘 밤에 겪어두자는 게 이 드릴이에요 (｡•̀ᴗ-)✧

이렇게 놀아봐요
  1. 함수 본문은 비워뒀어요. 힌트도 뼈대도 일부러 없어요.
  2. 각 CASES 아래 "직접 추가" 칸을 최소 개수만큼 채워야 통과로 쳐줘요.
  3. 무한 루프가 나면 Ctrl+C 로 멈추고, left / right / mid 를 매 반복마다
     print 로 찍어봐요. 코드를 다시 노려보는 것보다 훨씬 빨라요, 진짜로!

돌려보기
  .venv/Scripts/python.exe "week2/4. drill/02_binary_search_drill.py"
"""

import sys


def lower_bound(arr, target):
    """
    arr 는 오름차순으로 정렬돼 있어요.
    target '이상'인 첫 원소의 인덱스를 돌려주세요.
    그런 원소가 아예 없으면 len(arr) 를 돌려주면 돼요.

    예) [1, 3, 3, 5], target=3 -> 1
        [1, 3, 3, 5], target=4 -> 3
        [1, 3, 3, 5], target=9 -> 4
    """
    pass


def upper_bound(arr, target):
    """
    arr 는 오름차순으로 정렬돼 있어요.
    이번엔 target '초과'인 첫 원소의 인덱스예요. (이상 아니고 초과!)
    그런 원소가 없으면 len(arr) 를 돌려주면 돼요.

    예) [1, 3, 3, 5], target=3 -> 3
        [1, 3, 3, 5], target=0 -> 0
    """
    pass


def count_occurrences(arr, target):
    """
    정렬된 arr 안에 target 이 몇 개 있는지 세어주세요.
    위에서 만든 두 함수를 조합하면 O(log n) 에 끝나요. 그렇게 풀어봐요!
    (arr.count 는 O(n) 이라 여기선 반칙이에요 ˘•_•˘)

    예) [1, 3, 3, 3, 5], target=3 -> 3
    """
    pass


def max_unit_length(lines, k):
    """
    [파라메트릭 서치 - 답 자체를 이분 탐색하기]

    lines : 가지고 있는 랜선들의 길이 (양의 정수 리스트)
    k     : 만들어야 하는 랜선 개수

    랜선은 원하는 만큼 잘라 쓸 수 있고, 자르고 남은 자투리는 그냥 버려요.
    길이가 전부 똑같은 랜선을 k 개 이상 만들고 싶을 때,
    가능한 '최대 정수 길이' 를 돌려주세요. 하나도 못 만들면 0 이에요.

    "답을 이분 탐색한다" 는 게 처음엔 좀 얄궂은데, 배열이 아니라
    '길이 1 ~ 최대길이' 라는 숫자 구간을 반으로 접는다고 보면 똑같아요.

    예) lines=[802, 743, 457, 539], k=11 -> 200
        (200 짜리로 자르면 4 + 3 + 2 + 2 = 11 개, 201 로는 11개가 안 나옴)
        lines=[10], k=100 -> 0
    """
    pass


# ============================================================================
# 테스트 케이스
# ============================================================================

PROVIDED = {"lower": 3, "upper": 2, "count": 2, "unit": 2}
MIN_EXTRA = 3

# (arr, target, 기대 인덱스, 설명)
LOWER_CASES = [
    ([1, 3, 3, 5], 3, 1, "중복의 첫 위치"),
    ([1, 3, 3, 5], 4, 3, "없는 값 - 들어갈 자리"),
    ([1, 3, 3, 5], 9, 4, "전부보다 큼 -> len(arr)"),

    # --- 직접 추가 (최소 3개) -------------------------------------------
    # 빈 리스트, 원소 하나, 전부 같은 값... 뭐가 제일 위험해 보여요?
    # 직접 골라서 넣어봐요 (๑˘︶˘๑)

]

# (arr, target, 기대 인덱스, 설명)
UPPER_CASES = [
    ([1, 3, 3, 5], 3, 3, "중복의 다음 위치"),
    ([1, 3, 3, 5], 0, 0, "전부보다 작음 -> 0"),

    # --- 직접 추가 (최소 3개) -------------------------------------------

]

# (arr, target, 기대 개수, 설명)
COUNT_CASES = [
    ([1, 3, 3, 3, 5], 3, 3, "중복 3개"),
    ([1, 3, 3, 3, 5], 2, 0, "없는 값"),

    # --- 직접 추가 (최소 3개) -------------------------------------------

]

# (lines, k, 기대 길이, 설명)
UNIT_CASES = [
    ([802, 743, 457, 539], 11, 200, "대표 예제"),
    ([10], 100, 0, "아무리 잘라도 개수가 안 됨"),

    # --- 직접 추가 (최소 3개) -------------------------------------------
    # 힌트는 안 줄게요! 대신 하나만 물어볼게요.
    # 탐색 범위의 '오른쪽 끝' 을 뭘로 잡았어요? 그 경계를 콕 찌르는
    # 케이스를 하나는 꼭 넣어봐요 (｀・ω・´)

]


# ============================================================================
# 채점기
# ============================================================================
def _section(title, cases, fn, fmt):
    passed = 0
    print(f"[{title}]")
    for case in cases:
        *args, expected, note = case
        try:
            got = fn(*args)
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        ok = (got == expected)
        passed += ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {fmt(*args)} -> {got}")
        if not ok:
            print(f"         기대: {expected}   ({note})")
    print()
    return passed, len(cases)


if __name__ == "__main__":
    print("=" * 60)
    print("드릴 2 : 이분 탐색 변형   - 다른 건 조건 한 글자, 반환값 한 개")
    print("=" * 60)

    results = [
        _section("lower_bound", LOWER_CASES, lower_bound,
                 lambda a, t: f"lower_bound({a}, {t})"),
        _section("upper_bound", UPPER_CASES, upper_bound,
                 lambda a, t: f"upper_bound({a}, {t})"),
        _section("count_occurrences", COUNT_CASES, count_occurrences,
                 lambda a, t: f"count_occurrences({a}, {t})"),
        _section("max_unit_length", UNIT_CASES, max_unit_length,
                 lambda l, k: f"max_unit_length({l}, {k})"),
    ]
    passed = sum(p for p, _ in results)
    total = sum(t for _, t in results)

    extra = {
        "lower": len(LOWER_CASES) - PROVIDED["lower"],
        "upper": len(UPPER_CASES) - PROVIDED["upper"],
        "count": len(COUNT_CASES) - PROVIDED["count"],
        "unit":  len(UNIT_CASES)  - PROVIDED["unit"],
    }
    print("-" * 60)
    print(f"테스트 결과 : {passed} / {total} 통과")
    print("직접 채운 케이스 :")
    short = False
    for name, n in extra.items():
        if n < MIN_EXTRA:
            short = True
        print(f"  {name:<8} {n}개  {'OK' if n >= MIN_EXTRA else f'조금만 더! (최소 {MIN_EXTRA}개)'}")
    print("-" * 60)

    sys.exit(0 if (passed == total and not short) else 1)
