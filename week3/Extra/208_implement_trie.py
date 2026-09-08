r"""
[LeetCode 208 - Implement Trie (Prefix Tree) / 트라이 구현]
난이도: Medium
https://leetcode.com/problems/implement-trie-prefix-tree/

▣ 문제
트라이(trie, "트라이" 또는 "try"로 읽습니다)는 문자열 여러 개를 저장해두고
빠르게 찾기 위한 트리 자료구조입니다. 자동완성이나 맞춤법 검사에 쓰입니다.

Trie 클래스를 구현하세요.

  - Trie()                          트라이 객체를 초기화합니다.
  - insert(word)   -> None          문자열 word 를 트라이에 넣습니다.
  - search(word)   -> bool          word 가 **넣은 적 있는 단어**면 True.
  - startsWith(p)  -> bool          넣은 단어 중 p 로 **시작하는 것**이 있으면 True.

▣ 예시
    Trie trie = new Trie()
    trie.insert("apple")
    trie.search("apple")      -> True
    trie.search("app")        -> False   ← "app" 은 아직 넣은 적이 없습니다
    trie.startsWith("app")    -> True    ← "apple" 이 "app" 으로 시작하니까요
    trie.insert("app")
    trie.search("app")        -> True    ← 이제는 넣었으니 True

    search("app") 가 처음엔 False 인데 startsWith("app") 는 True 인 것,
    이 한 줄이 이 문제의 전부입니다.

▣ 제약
- 1 <= len(word), len(prefix) <= 2000
- word 와 prefix 는 전부 소문자 알파벳
- insert / search / startsWith 를 전부 합쳐 최대 3 * 10^4 번 호출됩니다

▣ 이번엔 다른 점
지금까지는 남이 만들어둔 자료구조 위에 알고리즘을 얹었습니다.
이번엔 **자료구조 자체를 설계**합니다. 노드에 무엇을 담을지 정하는 게 문제의 절반입니다.
"""


class Trie:

    def __init__(self):
        """
        빈 트라이를 만듭니다. 여기서 정한 모양이 아래 세 메서드를 전부 결정합니다.
        """
        # TODO: 여기에 구현하세요.
        self.end = False
        self.children = {}

        # 코드를 치기 전에 답해볼 질문들:
        #  - 노드 하나가 들고 있어야 할 정보는 무엇인가요? 자식들 말고 **하나가 더**
        #    필요합니다. 예시에서 "apple" 만 넣은 상태로 search("app") 가 False 인 이유를
        #    설명해보면 그 하나가 무엇인지 나옵니다. 한 문장으로 적고 시작하세요.
        #     끝단어 인지 저장?
        #  - 자식을 무엇으로 들고 있을까요? 26칸짜리 리스트와 딕셔너리 두 가지가 있습니다.
        #    각각 노드 하나가 차지하는 메모리와 "다음 글자로 내려가는" 비용을 적어보고
        #    고르세요. 고른 이유도 한 줄 적어두면 나중에 본인이 덜 헷갈립니다.
        #   리스트 인덱스로 내려가면 되는거 아닌가? 근데 딕셔너리가 더 직관적이긴 할듯?
        #  - 루트 노드에는 어떤 글자가 들어 있나요? 이 질문의 답이 이상하게 느껴지면
        #    그게 정상입니다. 이상한 이유를 적어두세요.
        # 다들어 가있을꺼 같은데

    def insert(self, word: str) -> None:
        """
        word: 넣을 단어 (소문자 알파벳, 길이 1~2000)
        반환값 없음
        """
        # TODO: 여기에 구현하세요.
        #
        #  - 단어 하나를 넣는 데 드는 비용은 단어 길이에 대해 몇 번인가요?
        #    호출이 3*10^4 번이고 길이가 최대 2000 이면 총합은 얼마인가요?

        node = self
        i = 1
        n = len(word)
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            if i == n:
                node = node.children[char]
                node.end = True
                break

            i += 1
            node = node.children[char]


    def search(self, word: str) -> bool:
        """
        word: 찾을 단어
        반환: 넣은 적 있는 단어면 True, 아니면 False
        """
        # TODO: 여기에 구현하세요.
        node = self
        i = 1
        n = len(word)

        for char in word:
            if char in node.children:
                node = node.children[char]
                if i == n and node.end is True:
                    return True
                else:
                    i += 1
                    continue
            else:
                return False
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        prefix: 찾을 접두사
        반환: prefix 로 시작하는 단어를 넣은 적이 있으면 True, 아니면 False
        """
        # TODO: 여기에 구현하세요.
        #
        #  - search 와 startsWith 는 하는 일이 거의 같습니다.
        #    **딱 한 군데**만 다릅니다. 어디인지 적어보세요.
        #    그 자리를 찾으면 둘 중 하나는 아주 짧아집니다.
        node = self
        i = 1
        n = len(prefix)

        for char in prefix:
            if char in node.children:
                if i == n:
                    return True
                else:
                    i += 1
                    node = node.children[char]
                    continue
            else:
                return False
        return False


# ─────────────────────────────────────────────────────────────
#  로컬 테스트
#  LeetCode 에 낼 때는 위의 class Trie 부분만 복사해서 붙이면 됩니다.
#
#  LeetCode 가 클래스 문제를 채점하는 방식 그대로 흉내낸 하네스입니다.
#  ops  : 호출할 메서드 이름들
#  args : 각 호출에 넘길 인자 (인자가 없으면 빈 리스트)
#  기대 : 각 호출의 반환값 (insert 와 생성자는 None)
# ─────────────────────────────────────────────────────────────

fails = 0


def check(ops, args, expected, label=""):
    global fails
    obj = None
    got = []
    for op, arg in zip(ops, args):
        if op == "Trie":
            obj = Trie()
            got.append(None)
        else:
            got.append(getattr(obj, op)(*arg))

    ok = got == expected
    if not ok:
        fails += 1
    print(f"  [{' OK ' if ok else 'FAIL'}] {label}")
    print(f"         호출 {ops}")
    print(f"         인자 {args}")
    print(f"         기대 {expected}")
    print(f"         실제 {got}")
    if not ok:
        for i, (o, g, e) in enumerate(zip(ops, got, expected)):
            if g != e:
                print(f"         └ 처음 어긋난 곳: {i}번째 호출 {o}{args[i]} "
                      f"→ 기대 {e}, 실제 {g}")
                break
    print()


if __name__ == "__main__":
    print("[LeetCode 제공 예시]")
    check(
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
        [None, None, True, False, True, None, True],
        "예시 1",
    )

    print("[직접 채울 테스트]")
    # 아래 네 칸은 비워뒀습니다. 어떤 호출 순서가 이 코드를 깨뜨릴지 직접 고르세요.
    # 기대값은 손으로 먼저 적고, 그 다음에 돌리세요.
    # 라벨은 서로 다르게 붙여야 FAIL 났을 때 어느 쪽인지 보입니다.
    #
    # 힌트가 필요하면 이런 축들이 있습니다 (전부 쓸 필요는 없습니다):
    #   · 한 번도 넣지 않은 단어를 찾으면?
    #   · 넣은 단어보다 **긴** 단어를 찾으면?
    #   · 같은 단어를 두 번 넣으면?
    #   · 한 글자짜리 단어는?
    check(
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["applee"], ["app"], ["app"], ["app"]],
        [None, None, True, False, True, None, True],
        "긴단어",
    )
    check(
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["apple"], ["app"]],
        [None, None, True, False, True, None, False],
        "같은단어",
    )
    check(
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["i"], ["i"]],
        [None, None, True, False, True, None, True],
        "짧은단어",
    )

    # check(["Trie", ...], [[], ...], [None, ...], "설명")
    # check(["Trie", ...], [[], ...], [None, ...], "설명")
    # check(["Trie", ...], [[], ...], [None, ...], "설명")
    # check(["Trie", ...], [[], ...], [None, ...], "설명")

    print(f"실패 {fails}개" if fails else "전부 통과했습니다")
