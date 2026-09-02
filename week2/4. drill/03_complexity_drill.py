"""
[드릴 3] 시간 복잡도 - 느린 코드를 빠릿하게 만들기  ⊂(・﹏・⊂)

_slow 세 개는 '이미 답이 잘 나오는' 코드예요. 건드릴 필요 전혀 없어요!
할 일은 결과가 토씨 하나 안 틀리게 똑같은 _fast 버전을 짜는 거예요.

노리는 건 두 가지예요.
  1. list 의 `in`, `count`, `pop(0)` 이 각각 속으로 몇 번 도는지 몸으로 알기
  2. 복잡도를 '주장' 하는 대신 '재보는' 버릇 들이기

순서가 좀 중요해요. 아래 COMPLEXITY_ANSWERS 를 **먼저** 채우고 나서 돌려봐요.
채점기가 n 이랑 2n 에서 실제 시간을 재서 비율을 보여주거든요.
  - 시간이 대략 2배가 되면 -> O(n)
  - 대략 4배가 되면        -> O(n^2)

내가 적은 답이랑 재본 비율이 안 맞으면? 그게 오늘 제일 크게 배우는 지점이에요.
틀리라고 만든 칸이니까 편하게 적어봐요 (๑>◡<๑)

돌려보기
  .venv/Scripts/python.exe "week2/4. drill/03_complexity_drill.py"
"""

import random
import sys
import time


# ============================================================================
# 문제 1 : 두 리스트의 공통 원소
# ============================================================================
def common_elements_slow(a, b):
    """a 안의 원소 중 b 에도 있는 것을, a 의 순서 그대로, 중복 없이 돌려줘요."""
    result = []
    for x in a:
        if x in b and x not in result:
            result.append(x)
    return result


def common_elements_fast(a, b):
    """[조건] a 의 순서 유지 + 중복 없음.

    위 slow 와 결과가 완전히 똑같아야 해요. 훨씬 빠르게! 여기를 채워봐요.
    """
    results = []
    for i, data in enumerate(a):
        data == set(b)

# ============================================================================
# 문제 2 : 순서를 유지한 중복 제거
# ============================================================================
def dedup_keep_order_slow(nums):
    """nums 에서 중복만 쏙 빼되, 처음 나온 순서는 그대로 지켜서 돌려줘요."""
    result = []
    for x in nums:
        if x not in result:
            result.append(x)
    return result


def dedup_keep_order_fast(nums):
    """[조건] 처음 나온 순서 유지.

    위 slow 와 결과가 완전히 똑같아야 해요. 훨씬 빠르게! 여기를 채워봐요.
    """
    set_nums = set(nums)
    return list(set_nums)


# ============================================================================
# 문제 3 : 합이 target 인 두 수의 존재 여부
# ============================================================================
def has_pair_with_sum_slow(nums, target):
    """서로 다른 두 자리 i < j 로 nums[i] + nums[j] == target 이 되면 True 예요."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True
    return False


def has_pair_with_sum_fast(nums, target):
    """[조건] 서로 다른 두 자리 i < j. 같은 칸을 두 번 쓰면 안 돼요.

    위 slow 와 결과가 완전히 똑같아야 해요. 훨씬 빠르게! 여기를 채워봐요.
    """
    pass


# ============================================================================
# 복잡도 답안 — 돌려보기 '전에' 먼저 채워주세요! (｡•̀ᴗ-)b
#   적는 법 예시: "O(1)", "O(n)", "O(n log n)", "O(n^2)", "O(n*m)"
#   n 은 첫 번째 인자의 길이, m 은 두 번째 리스트의 길이로 볼게요.
#   틀려도 괜찮아요. 아래 측정값이랑 맞춰보는 게 이 칸의 목적이에요.
# ============================================================================
COMPLEXITY_ANSWERS = {
    "common_elements_slow":  "nm",
    "common_elements_fast":  "",
    "dedup_keep_order_slow": "n",
    "dedup_keep_order_fast": "",
    "has_pair_with_sum_slow": "n^2",
    "has_pair_with_sum_fast": "",
}


# ============================================================================
# 채점기
# ============================================================================
SPEEDUP_REQUIRED = 5.0     # fast 가 slow 보다 최소 이만큼은 빨라야 통과예요


def _correctness(slow, fast, make_args, trials=30):
    """작은 입력을 마구 던져보면서 두 함수 결과가 늘 같은지 확인해요."""
    for _ in range(trials):
        args = make_args()
        expected = slow(*[list(a) if isinstance(a, list) else a for a in args])
        try:
            got = fast(*[list(a) if isinstance(a, list) else a for a in args])
        except Exception as e:
            return False, f"{type(e).__name__}: {e}", args, expected
        if got != expected:
            return False, got, args, expected
    return True, None, None, None


def _timed(fn, args):
    t0 = time.perf_counter()
    fn(*args)
    return time.perf_counter() - t0


def _bench(title, slow, fast, make_args, make_big):
    print(f"[{title}]")

    ok, got, args, expected = _correctness(slow, fast, make_args)
    if not ok:
        print(f"  [FAIL] 결과가 slow 랑 달라요")
        print(f"         입력   : {args}")
        print(f"         기대   : {expected}")
        print(f"         받은 값: {got}")
        print()
        return False

    print("  [PASS] 정확성 - slow 랑 결과가 똑같아요")

    small = make_big(1)
    big = make_big(2)
    ts_small = _timed(slow, small)
    ts_big = _timed(slow, [list(a) if isinstance(a, list) else a for a in big])
    tf_big = _timed(fast, [list(a) if isinstance(a, list) else a for a in big])

    ratio = ts_big / ts_small if ts_small > 0 else float("inf")
    speedup = ts_big / tf_big if tf_big > 0 else float("inf")

    print(f"  slow : n 에서 {ts_small*1000:8.2f} ms  ->  2n 에서 {ts_big*1000:8.2f} ms"
          f"   (시간이 {ratio:.1f} 배)")
    print(f"  fast : 2n 에서 {tf_big*1000:8.2f} ms   -> slow 대비 {speedup:.1f} 배 빠름")

    if speedup < SPEEDUP_REQUIRED:
        print(f"  [FAIL] 속도 - 최소 {SPEEDUP_REQUIRED:.0f} 배는 빨라져야 통과예요")
        print()
        return False

    print(f"  [PASS] 속도")
    print()
    return True


if __name__ == "__main__":
    print("=" * 68)
    print("드릴 3 : 시간 복잡도   - 주장하지 말고 재봐요")
    print("=" * 68)

    blank = [k for k, v in COMPLEXITY_ANSWERS.items() if not v.strip()]
    print("\n[복잡도 답안]")
    for k, v in COMPLEXITY_ANSWERS.items():
        print(f"  {k:<24} {v if v.strip() else '(비어 있음)'}")
    if blank:
        print(f"\n  -> {len(blank)}개가 비어 있어요. 측정값 보기 전에 먼저 적어봐요!")
    print()

    N = 2000
    rnd = random.Random(42)

    results = []

    results.append(_bench(
        "common_elements",
        common_elements_slow, common_elements_fast,
        make_args=lambda: ([rnd.randrange(20) for _ in range(rnd.randrange(0, 15))],
                           [rnd.randrange(20) for _ in range(rnd.randrange(0, 15))]),
        make_big=lambda mul: ([rnd.randrange(4 * N) for _ in range(N * mul)],
                              [rnd.randrange(4 * N) for _ in range(N * mul)]),
    ))

    results.append(_bench(
        "dedup_keep_order",
        dedup_keep_order_slow, dedup_keep_order_fast,
        make_args=lambda: ([rnd.randrange(10) for _ in range(rnd.randrange(0, 20))],),
        make_big=lambda mul: ([rnd.randrange(N * mul) for _ in range(N * mul)],),
    ))

    results.append(_bench(
        "has_pair_with_sum",
        has_pair_with_sum_slow, has_pair_with_sum_fast,
        make_args=lambda: ([rnd.randrange(20) for _ in range(rnd.randrange(0, 15))],
                           rnd.randrange(40)),
        # 짝수만 넣고 목표를 홀수로 두면 짝이 절대 안 생겨서 최악의 경우가 돼요
        make_big=lambda mul: ([2 * rnd.randrange(N) for _ in range(N * mul)], 1),
    ))

    print("-" * 68)
    print(f"통과 : {sum(results)} / {len(results)}")
    if blank:
        print(f"복잡도 답안 {len(blank)}개가 아직 비어 있어요")
    print("-" * 68)

    sys.exit(0 if (all(results) and not blank) else 1)
