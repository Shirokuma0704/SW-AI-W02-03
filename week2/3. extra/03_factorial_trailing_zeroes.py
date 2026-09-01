"""
[수론 - Factorial Trailing Zeroes]

▣ 출처
LeetCode 172. Factorial Trailing Zeroes (Medium)
https://leetcode.com/problems/factorial-trailing-zeroes/

▣ 상황 설명
정수 n 이 주어집니다. n! (n 팩토리얼) 의 끝에 붙은 0 의 개수를 구하세요.

    n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
    0! = 1  (약속)

▣ 목표
n! 을 십진수로 적었을 때 맨 뒤에 연속으로 붙어 있는 0 의 개수를 반환.

▣ 규칙 (읽을 때 주의할 것)
  (1) "끝에 붙은" 0 만 센다. 중간에 있는 0 은 세지 않는다.
        3628800  ->  2   (맨 뒤 "00")
        1010     ->  1   (가운데 0 은 무관)
        1000     ->  3
  (2) 0 이 하나도 없으면 0 을 반환한다. (예: 6 -> 0)
  (3) n = 0 도 입력으로 들어온다. 0! = 1 이므로 답은 0.

▣ 예시
    n = 3   ->  0        3! = 6
    n = 5   ->  1        5! = 120
    n = 0   ->  0        0! = 1

▣ 구현할 함수
trailing_zeroes(n: int) -> int
  - n! 의 뒤에 붙은 0 의 개수를 정수로 반환합니다.
  - 리트코드에서는 메서드 이름이 trailingZeroes(self, n) 입니다.
    로컬에서는 아래 이름을 그대로 두고, 제출할 때만 클래스 안에 옮겨 담으세요.
    (이름을 바꿔버리면 아래 테스트 하네스가 못 찾습니다)

▣ 제약
- 0 <= n <= 10^4

▣ Follow up (원문)
- Could you write a solution that works in logarithmic time complexity?
  (로그 시간에 도는 풀이를 쓸 수 있을까?)

▣ 참고 - 스스로 정답을 만들어 검증하는 법
파이썬 정수는 자릿수 제한이 없으므로 n! 을 실제로 곱해서 끝의 0 을 직접
세어볼 수 있습니다. 느리지만 "확실히 맞는 답"을 만들 수 있으니, 새로운
n 에 대한 기댓값이 필요할 때 이 방법으로 정답을 뽑아 쓰면 됩니다.

  ※ 함정: 큰 n 에서 str(factorial) 로 문자열 변환을 시도하면 터집니다.
      ValueError: Exceeds the limit (4300 digits) for integer string conversion
    파이썬 3.11 부터 정수 -> 문자열 변환에 4300 자리 제한이 걸려 있습니다
    (거대한 수를 출력하다 멈추는 사고를 막으려고 생긴 안전장치).
    계산 자체는 아무 문제 없고 변환만 막히는 것이므로, 문자열로 바꾸지 말고
    10 으로 계속 나누면서 세면 제한에 걸리지 않습니다.

  참고로 10000! 은 35660 자리입니다. Follow up 이 요구하는 풀이는
  이 방향이 아닙니다.
"""


def trailing_zeroes(n: int) -> int:
    """
    n! 의 끝에 붙은 0 의 개수를 반환.

    예) trailing_zeroes(5) == 1      # 5! = 120
        trailing_zeroes(10) == 2     # 10! = 3628800
    """
    # TODO: n! 의 뒤에 붙은 0 의 개수를 구해서 반환하세요.
    result = 0
    i = 1
    while True:
        check = n // (5** i)
        if n < (5 ** i):
            break
        else: result , i = result + check, i+1

    return result




# ---------------------------------------------------------------------------
# 테스트
# ---------------------------------------------------------------------------
TEST_CASES = [
    # (n,       정답,   이 케이스가 잡아내는 것)
    (0,          0,    "0! = 1 (문제 예시 3)"),
    (1,          0,    "1! = 1"),
    (3,          0,    "3! = 6 (문제 예시 1)"),
    (4,          0,    "4! = 24 - 아직 0 이 안 생김"),
    (5,          1,    "5! = 120 (문제 예시 2) - 첫 0 이 생기는 지점"),
    (6,          1,    "6! = 720"),
    (9,          1,    "9! = 362880"),
    (10,         2,    "10! = 3628800"),
    (15,         3,    "일정하게 늘어나는 구간"),
    (24,         4,    "25 직전"),
    (25,         6,    "25 에서 4 -> 6 으로 두 칸 뛴다"),
    (26,         6,    "뛴 직후"),
    (30,         7,    "다시 한 칸씩"),
    (100,       24,    "중간 크기"),
    (125,       31,    "또 한 번 크게 뛰는 지점"),
    (1000,     249,    "큰 입력"),
    (10000,   2499,    "제약 상한 - 여기서 느리면 Follow up 미달"),
]


if __name__ == "__main__":
    print("[테스트] Factorial Trailing Zeroes")
    print()

    passed = 0
    for n, expected, note in TEST_CASES:
        got = trailing_zeroes(n)
        ok = (got == expected)
        passed += ok
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] trailing_zeroes({n:>5}) -> {got}  (정답 {expected})")
        if not ok:
            print(f"         ^ {note}")

    print()
    print(f"  {passed} / {len(TEST_CASES)} 통과")
