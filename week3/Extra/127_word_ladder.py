r"""
[LeetCode 127 - Word Ladder (단어 사다리)]
난이도: Hard
https://leetcode.com/problems/word-ladder/

▣ 문제
beginWord 에서 endWord 까지 가는 "변환 수열"은 다음을 만족하는
    beginWord -> s1 -> s2 -> ... -> sk
형태의 단어 나열입니다.

  - 인접한 두 단어는 **딱 한 글자만** 다릅니다.
  - s1 부터 sk 까지 모든 단어가 wordList 안에 있어야 합니다.
    (beginWord 는 wordList 에 없어도 됩니다.)
  - sk == endWord

가장 짧은 변환 수열에 들어 있는 **단어의 개수**를 반환하세요.
그런 수열이 없으면 0 을 반환합니다.

▣ 예시
    beginWord = "hit", endWord = "cog"
    wordList  = ["hot", "dot", "dog", "lot", "log", "cog"]
    출력: 5

    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
      1       2        3        4        5      ← 단어를 세면 5개

    beginWord = "hit", endWord = "cog"
    wordList  = ["hot", "dot", "dog", "lot", "log"]
    출력: 0
    설명: endWord 인 "cog" 가 wordList 에 없어서 도착할 방법이 없습니다.

▣ 제약
- 1 <= len(beginWord) <= 10
- len(endWord) == len(beginWord) == len(wordList[i])   (전부 같은 길이)
- 1 <= len(wordList) <= 5000
- 모든 단어는 소문자 알파벳뿐
- beginWord != endWord
- wordList 안의 단어는 서로 중복이 없습니다
"""

from typing import List
from collections import deque



class Solution:
    def ladderLength(self, beginword: str, endword: str, wordlist: List[str]) -> int:
        """
        beginWord: 출발 단어 (wordList 에 없을 수 있음)
        endWord:   도착 단어
        wordList:  사용 가능한 단어 목록 (최대 5000개, 전부 같은 길이, 중복 없음)
        반환: 가장 짧은 변환 수열의 **단어 개수** (도달 불가면 0)
        """
        # TODO: 여기에 구현하세요.
        n=len(endword)

        if endword not in wordlist: return 0
        wildcards = {}
        for words in wordlist:
            for i in range(n):
                x = list(words)
                x[i] = "*"
                wildcards.setdefault("".join(x), []).append(words)

        queue = deque()
        queue.append((beginword,1))
        discovered = {beginword}

        while queue:
            word,index = queue.popleft()

            for j in range(n):
                y = list(word)
                y[j] = "*"
                find_words = wildcards.get("".join(y))

                if find_words is None: continue

                if endword in find_words:
                    return index+1

                for find_word in find_words:
                    if find_word not in discovered:
                        discovered.add(find_word)
                        queue.append((find_word, index+1))
        return 0



        # 코드를 치기 전에 답해볼 질문들:
        #  - 이 문제를 그래프로 본다면 "정점"은 무엇이고 "간선"은 언제 연결되나요?
        #    그걸 한 문장으로 적고 시작하세요. (지난 LIS 에서 배운 그거입니다)
        # 정점 - (알파벳,알파벳,...) 간선은 정확하게 한 요소가 다르면 그쪽으로 갈수있음

        #  - 문제에 "가장 짧은" 이 들어 있습니다. week3 에서 다룬 것 중에
        #    무엇과 같은 모양인가요? 그리고 여기서 간선의 가중치는 몇인가요?
        # bfs(다익스트라?), 1
        #  - 반환값이 "변환 횟수"가 아니라 "단어의 개수"입니다.
        #    예시 1에서 화살표는 4개인데 답은 5죠. 어디서 1이 갈리는지 정해두세요.
        # 출발지가 그래프안에 없음
        #  - 두 단어가 한 글자만 다른지 확인하는 비용을 계산해보세요.
        #    단어 5000개를 모든 쌍끼리 비교하면 몇 번이고, 단어 길이 10을 곱하면
        #    몇 번인가요? 그 숫자가 감당되는지 보고, 안 되면 "한 글자만 다른 이웃"을
        #    비교 없이 찾아낼 방법이 있는지 생각해보세요.
        # 3*26? 3*10? 혹은 2차원 리스트안에 박아넣는게 바로생각이남.



# ─────────────────────────────────────────────────────────────
#  로컬 테스트
#  LeetCode 에 낼 때는 위의 class Solution 부분만 복사해서 붙이면 됩니다.
# ─────────────────────────────────────────────────────────────

def check(begin, end, words, expected, label=""):
    got = Solution().ladderLength(begin, end, words)
    mark = " OK " if got == expected else "FAIL"
    print(f"  [{mark}] {label}")
    print(f"         begin={begin!r}  end={end!r}")
    print(f"         wordList={words}")
    print(f"         기대={expected}  실제={got}")
    print()


if __name__ == "__main__":
    print("[LeetCode 제공 예시]")
    check("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5, "예시 1")
    check("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0, "예시 2")

    print("[직접 채울 테스트]")
    # 아래 네 칸은 비워뒀습니다. 어떤 입력이 이 코드를 깨뜨릴지 직접 고르세요.
    # 기대값은 손으로 먼저 세서 적고, 그 다음에 돌리세요.
    # 라벨은 서로 다르게 붙여야 FAIL 났을 때 어느 쪽인지 보입니다.
    check("wid","azx",["wid","azx"],0,"연결불가")
    check("wid","azx",["wid","wix","azx"],0,"연결불가")
    check("dog","doc",["doc"],2,"최소값")
    check("hit", "cog", ["hot","hit", "dot", "dog", "lot", "log", "cog"], 5, "비긴이 들어가있음")


    # check("...", "...", [...], ..., "설명")
    # check("...", "...", [...], ..., "설명")
    # check("...", "...", [...], ..., "설명")
    # check("...", "...", [...], ..., "설명")
