r"""
[LeetCode 300 - Longest Increasing Subsequence (가장 긴 증가하는 부분 수열)]
난이도: Medium
https://leetcode.com/problems/longest-increasing-subsequence/

▣ 문제
정수 배열 nums 가 주어질 때, 가장 긴 "강한 증가(strictly increasing)"
부분 수열의 **길이**를 반환하세요. 수열 자체가 아니라 길이만 있으면 됩니다.

▣ 용어 정리
- 부분 수열(subsequence): 원래 배열에서 원소를 0개 이상 **지우고**, 남은 것들의
  **순서는 그대로 둔** 것. 연속일 필요가 없습니다.
      [10, 9, 2, 5, 3, 7] 에서 [10, 5, 7] 은 부분 수열이 맞고,
                              [5, 10] 은 순서가 바뀌었으므로 아닙니다.
- 강한 증가(strictly increasing): 바로 앞 원소보다 **반드시 커야** 합니다.
  같은 값은 이어붙일 수 없습니다. (예시 3이 이걸 확인합니다.)

▣ 예시
    입력: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    출력: 4
    설명: [2, 3, 7, 101] 이 가장 긴 증가 부분 수열이라 길이가 4.

    입력: nums = [0, 1, 0, 3, 2, 3]
    출력: 4

    입력: nums = [7, 7, 7, 7, 7, 7, 7]
    출력: 1
    설명: 같은 값끼리는 이어붙일 수 없으니 하나만 고르는 게 최선.

▣ 제약
- 1 <= len(nums) <= 2500        (빈 배열은 들어오지 않습니다)
- -10^4 <= nums[i] <= 10^4      (음수가 들어옵니다)

▣ Follow up
O(n log n) 풀이가 존재합니다. 다만 순서를 지키세요 —
먼저 O(n^2) 로 정답을 확실히 맞춘 뒤에 도전하는 게 훨씬 남는 게 많습니다.
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        nums: 정수 배열 (길이 1 이상 2500 이하, 원소는 -10^4 ~ 10^4)
        반환: 가장 긴 강한 증가 부분 수열의 길이 (int)

        주의: 같은 값은 이어붙일 수 없습니다 (strictly).
        """
        routes = [1 for _ in range(len(nums))]
        total=len(nums)

        for x in reversed(range(total)):
            for y in reversed(range(x+1, total)):
                if nums[x] < nums[y]:
                    if routes[x] <= routes[y]:
                        routes[x] = routes[y] + 1


        return max(routes)


# ─────────────────────────────────────────────────────────────
#  로컬 테스트
#  LeetCode 에 낼 때는 위의 class Solution 부분만 복사해서 붙이면 됩니다.
# ─────────────────────────────────────────────────────────────

def check(nums, expected, label=""):
    got = Solution().lengthOfLIS(nums)
    mark = " OK " if got == expected else "FAIL"
    print(f"  [{mark}] {label}")
    print(f"         nums={nums}")
    print(f"         기대={expected}  실제={got}")
    print()


if __name__ == "__main__":
    print("[LeetCode 제공 예시]")
    check([10, 9, 2, 5, 3, 7, 101, 18], 4, "예시 1")
    check([0, 1, 0, 3, 2, 3], 4, "예시 2")
    check([7, 7, 7, 7, 7, 7, 7], 1, "예시 3")

    print("[직접 채울 테스트]")
    # 아래 네 칸은 비워뒀습니다. 어떤 입력이 이 코드를 깨뜨릴 수 있을지
    # 직접 골라서 채워보세요. 엣지 케이스를 찾아내는 것도 문제 풀이의 일부입니다.
    # 기대값은 손으로 세서 먼저 적고, 그 다음에 돌려보세요.
    check([x for x in range(-500,500)],1000,"예시 4")
    check([x for x in reversed(range(-500,500))],1,"예시 5")
    check([1],1,"예시6")
    # check([...], ..., "설명")
    # check([...], ..., "설명")
    # check([...], ..., "설명")
    # check([...], ..., "설명")
