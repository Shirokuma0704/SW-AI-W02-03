"""
[탐색 - Word Search]

▣ 출처
LeetCode 79. Word Search (Medium)
https://leetcode.com/problems/word-search/

▣ 상황 설명
m x n 크기의 문자 격자 board 와 문자열 word 가 주어집니다.
board 안에서 글자들을 이어 붙여 word 를 만들 수 있는지 판정하세요.

    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]

         0   1   2   3
     0   A   B   C   E
     1   S   F   C   S
     2   A   D   E   E

▣ 목표
word 를 만들 수 있으면 True, 없으면 False 를 반환.

▣ 규칙 (문제를 읽을 때 놓치기 쉬운 것들)
  (1) 인접 = 상하좌우 4방향뿐이다. 대각선은 인접이 아니다.
  (2) 글자들이 board 안에 존재하기만 하면 되는 게 아니라,
      한 칸에서 다음 칸으로 계속 이어지는 하나의 경로여야 한다.
  (3) 같은 칸을 두 번 쓸 수 없다. 단어 하나를 만드는 동안 각 칸은 한 번만.
      (글자가 같은 다른 칸을 쓰는 것은 당연히 허용된다. 금지되는 건 같은 '칸')
  (4) 시작 칸은 정해져 있지 않다. 어느 칸에서 시작해도 된다.
  (5) 대소문자를 구분한다. 'a' 와 'A' 는 다른 글자다.

▣ 예시
    word = "ABCCED"  ->  True
        A(0,0) → B(0,1) → C(0,2) → C(1,2) → E(2,2) → D(2,1)
        모든 이동이 상하좌우이고, 같은 칸을 다시 밟지 않는다.

    word = "SEE"  ->  True
        S(1,3) → E(2,3) → E(2,2)

    word = "ABCB"  ->  False
        A(0,0) → B(0,1) → C(0,2) 까지는 되지만,
        마지막 B 로 갈 곳이 이미 쓴 (0,1) 뿐이다. 규칙 (3) 위반.

▣ 구현할 함수
word_search(board: list, word: str) -> bool
  - board 에서 word 를 만들 수 있으면 True, 아니면 False.
  - 리트코드에서는 메서드 이름이 exist(self, board, word) 입니다.

▣ 제약
- m == len(board), n == len(board[0])
- 1 <= m, n <= 6           (최대 36칸)
- 1 <= len(word) <= 15
- board 와 word 는 영문 대소문자로만 이루어진다.

▣ Follow up (원문)
- Could you use search pruning to make your solution faster with a larger board?
  (더 큰 board 에서도 빠르도록 탐색 가지치기를 넣을 수 있을까?)
"""

def word_search(self, board, word):

    m = len(board)
    n = len(board[0])
    merged = set()

    for x in range(m):
        merged.update(board[x])

    if m * n < len(word): return False
    if set(merged) & set(word) != set(word): return False


    def near_check(x, y, x1, y1):

        if x == x1:
            if y == y1 - 1 or y == y1 + 1:
                return True
            else:
                return False
        elif y == y1:
            if x == x1 - 1 or x == x1 + 1:
                return True
            else:
                return False
        elif x1 == -5:
            return True  ##시작값
        else:
            return False

    def search(word_s, board_s, x1, y1, i):
        if len(word_s) == i: return True

        for x in range(m):
            for y in range(n):
                if board_s[x][y] == word_s[i]:
                     if near_check(x, y, x1, y1) is True:
                        board[x][y], temp = "Used", board[x][y]
                        result_loop = search(word_s, board, x, y, i + 1)
                        board[x][y] = temp
                        if result_loop:
                            return True

        return False

    result = search(word, board, -5, -5, 0)
    return result


# ---------------------------------------------------------------------------
# 테스트
#
# board 를 제자리에서 고치는 풀이(방문한 칸을 임시로 덮어쓰는 방식)도 흔하므로,
# 각 케이스마다 board 를 복사해서 넘긴다. 원본이 오염되면 뒤 케이스가 같이
# 틀리면서 원인을 못 찾게 되기 때문.
# ---------------------------------------------------------------------------
BOARD = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]

TINY = [["a"]]
SQUARE = [["A", "B"],
          ["C", "D"]]
CASE = [["a", "A"]]
ALL_A = [["A", "A", "A"],
         ["A", "A", "A"],
         ["A", "A", "A"]]
UNDO = [["A", "A"],
        ["A", "B"]]

TEST_CASES = [
    # (board,   word,           정답,   이 케이스가 잡아내는 것)
    (BOARD,  "ABCCED",          True,  "문제 예시 1"),
    (BOARD,  "SEE",             True,  "문제 예시 2"),
    (BOARD,  "ABCB",            False, "문제 예시 3 - 같은 칸 재사용 금지"),
    (BOARD,  "A",               True,  "한 글자"),
    (BOARD,  "Z",               False, "board 에 없는 글자"),
    (BOARD,  "ABCEE",           False, "글자는 다 있지만 경로가 안 이어짐"),
    (BOARD,  "ABCCEDFSA",       True,  "긴 경로 - 되돌아가기 필요"),
    (BOARD,  "AS",              True,  "세로 이동"),
    (BOARD,  "AF",              False, "대각선은 인접이 아님"),
    (TINY,   "a",               True,  "1x1 격자"),
    (TINY,   "aa",              False, "칸 수보다 긴 단어"),
    (SQUARE, "ABDC",            True,  "시계 방향 한 바퀴"),
    (SQUARE, "ABCD",            False, "B 와 C 는 인접이 아님"),
    (CASE,   "aA",              True,  "대소문자 구분"),
    (CASE,   "aa",              False, "대소문자 구분 - 소문자 a 는 한 칸뿐"),
    (ALL_A,  "AAAAAAAAA",       True,  "9칸 전부 사용 (9글자)"),
    (ALL_A,  "AAAAAAAAAA",      False, "칸이 9개인데 10글자"),
    (UNDO,   "AAA",             True,  "되돌리기 누락 - 앞 갈래가 막힌 뒤 그 칸을 다시 써야 함"),
]


def copy_board(board):
    """board 를 얕지 않게 복사 (행 리스트까지 새로 만든다)"""
    return [row[:] for row in board]


if __name__ == "__main__":
    print("[테스트] Word Search")
    print()

    passed = 0
    for board, word, expected, note in TEST_CASES:
        got = word_search(copy_board(board), word)
        ok = (got == expected)
        passed += ok
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] word_search(<{len(board)}x{len(board[0])}>, {word!r}) -> {got}  (정답 {expected})")
        if not ok:
            print(f"         ^ {note}")

    print()
    print(f"  {passed} / {len(TEST_CASES)} 통과")
