"""
[드릴 1] 연결 리스트 - 삽입 / 삭제 / 뒤집기  ٩(๑˃ᴗ˂๑)۶

이미 짜 봤던 것 (그대로 줄게요) : append, to_list
이번에 직접 짤 것              : insert_at, delete_value, reverse

포인터 세 개 굴리는 거라 C 감각 그대로예요. next 가 곧 `struct node *next`,
None 이 곧 NULL. 새로 배우는 게 아니라 손에 붙이는 시간이라고 생각하면 편해요.

이렇게 놀아봐요
  1. 함수 본문은 비워뒀어요. 힌트도 뼈대도 일부러 안 넣었어요.
     여기서 헤매는 게 내일 안 헤매는 방법이라서요 (˶ˊᵕˋ˶)
  2. 각 CASES 아래에 "직접 추가" 칸이 있어요. 최소 개수를 안 채우면
     통과로 안 쳐줘요. 어디서 깨질지 찾아내는 것도 절반은 연습이거든요!
  3. 에러가 나야 맞는 케이스는, 기대값 자리에 IndexError 라고 그냥 적으면 돼요.

돌려보기
  .venv/Scripts/python.exe "week2/4. drill/``01_linked_list_drill.py"
"""

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # ------------- 이미 짜 봤던 거라 그냥 드려요 ヽ(・∀・)ﾉ -------------
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values

    # ------------------- 여기서부터 직접! (๑•̀ㅂ•́)و -------------------
    def insert_at(self, index, data):
        """
        index 번째 자리에 data 를 가진 새 노드가 오도록 끼워넣어 주세요.

        - index == 0        : 맨 앞에 쏙
        - index == 길이     : 맨 뒤에 쏙 (append 랑 결과가 같아요)
        - 0 <= index <= 길이 를 벗어나면 IndexError 를 내주세요
        - 반환값은 없어요

        예) [10, 20, 30] 에서 insert_at(1, 15) -> [10, 15, 20, 30]
        """
        current = self.head
        new_node = Node(data)

        if index == 0:
            self.head = new_node
            return

        for i in range(index):
            if i < index and current is None:
                return IndexError
            else: current = current.next

        current, current.next = new_node, current


    def delete_value(self, data):
        """
        값이 data 인 노드를 앞에서부터 찾아서 '첫 번째 하나만' 빼주세요.
        (뒤에 같은 값이 또 있어도 그건 그대로 둬요!)

        Returns:
            지웠으면 True, 그런 값이 없으면 False

        예) [10, 20, 30, 20] 에서 delete_value(20) -> True, 리스트는 [10, 30, 20]
        """
        pass

    def reverse(self):
        """
        연결 방향을 홀랑 뒤집어 주세요. 새 리스트를 만들면 반칙이고,
        원래 있던 노드들의 next 를 바꿔서 해봐요.

        - 반환값은 없어요 (대신 self.head 가 바뀌어요)

        예) [1, 2, 3] -> [3, 2, 1]
        """
        pass


# ============================================================================
# 테스트 케이스
#   (초기값 리스트, ... , 기대 결과, 설명)
# ============================================================================

PROVIDED = {"insert": 2, "delete": 2, "reverse": 1}
MIN_EXTRA = 3   # 항목마다 직접 채워야 하는 최소 개수예요

# (초기 리스트, index, data, 기대 리스트 또는 IndexError, 설명)
INSERT_CASES = [
    ([10, 20, 30], 1, 15, [10, 15, 20, 30], "중간 삽입"),
    ([10, 20, 30], 0, 5,  [5, 10, 20, 30],  "맨 앞 삽입"),

    # --- 직접 추가 (최소 3개) -------------------------------------------
    # 위 두 개는 전부 '얌전히 잘 되는 경우'예요.
    # 얘를 어떻게 괴롭히면 터질까? 를 생각하면서 채워봐요 ( •̀ω•́ )✧

]

# (초기 리스트, 지울 값, 기대 리스트, 기대 반환값, 설명)
DELETE_CASES = [
    ([10, 20, 30], 20, [10, 30], True, "중간 삭제"),
    ([10, 20, 30], 99, [10, 20, 30], False, "없는 값"),

    # --- 직접 추가 (최소 3개) -------------------------------------------

]

# (초기 리스트, 기대 리스트, 설명)
REVERSE_CASES = [
    ([1, 2, 3], [3, 2, 1], "홀수 개"),

    # --- 직접 추가 (최소 3개) -------------------------------------------

]


# ============================================================================
# 채점기
# ============================================================================
def _build(values):
    ll = LinkedList()
    for v in values:
        ll.append(v)
    return ll


def _run():
    passed = total = 0

    print("[insert_at]")
    for init, idx, data, expected, note in INSERT_CASES:
        ll = _build(init)
        try:
            ll.insert_at(idx, data)
            got = ll.to_list()
        except IndexError:
            got = IndexError
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        ok = (got == expected)
        total += 1
        passed += ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {init} .insert_at({idx}, {data}) -> {got}")
        if not ok:
            print(f"         기대: {expected}   ({note})")

    print("\n[delete_value]")
    for init, target, expected, expected_ret, note in DELETE_CASES:
        ll = _build(init)
        try:
            ret = ll.delete_value(target)
            got = ll.to_list()
        except Exception as e:
            ret, got = None, f"{type(e).__name__}: {e}"
        ok = (got == expected and ret == expected_ret)
        total += 1
        passed += ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {init} .delete_value({target}) -> {got}, 반환 {ret}")
        if not ok:
            print(f"         기대: {expected}, 반환 {expected_ret}   ({note})")

    print("\n[reverse]")
    for init, expected, note in REVERSE_CASES:
        ll = _build(init)
        try:
            ll.reverse()
            got = ll.to_list()
        except Exception as e:
            got = f"{type(e).__name__}: {e}"
        ok = (got == expected)
        total += 1
        passed += ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {init} .reverse() -> {got}")
        if not ok:
            print(f"         기대: {expected}   ({note})")

    return passed, total


if __name__ == "__main__":
    print("=" * 60)
    print("드릴 1 : 연결 리스트   - 포인터 세 개만 잘 굴리면 돼요")
    print("=" * 60)

    passed, total = _run()

    extra = {
        "insert":  len(INSERT_CASES)  - PROVIDED["insert"],
        "delete":  len(DELETE_CASES)  - PROVIDED["delete"],
        "reverse": len(REVERSE_CASES) - PROVIDED["reverse"],
    }
    print("\n" + "-" * 60)
    print(f"테스트 결과 : {passed} / {total} 통과")
    print("직접 채운 케이스 :")
    short = False
    for name, n in extra.items():
        mark = "OK" if n >= MIN_EXTRA else f"조금만 더! (최소 {MIN_EXTRA}개)"
        if n < MIN_EXTRA:
            short = True
        print(f"  {name:<8} {n}개  {mark}")
    print("-" * 60)

    if short:
        print("\n어디서 깨질지 찾아내는 것도 연습이에요. 케이스를 조금만 더 채워봐요!")
    sys.exit(0 if (passed == total and not short) else 1)
