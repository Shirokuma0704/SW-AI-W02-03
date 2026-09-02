"""
드릴 전체 채점기예요 ⊂( ˆoˆ )⊃

이렇게 써요
  .venv/Scripts/python.exe "week2/4. drill/check.py"
  .venv/Scripts/python.exe "week2/4. drill/check.py" 01     # 하나만 볼 때

잠깐 곁다리 이야기 하나!
'2. advanced/check.py' 는 subprocess 로 'python3' 를 불러요. 그런데 이 컴퓨터의
python3 는 마이크로소프트 스토어 껍데기라, 아무것도 실행 안 하고 빈 출력만 뱉어요.
그래서 코드가 멀쩡한데도 전부 '실행 오류' 로 찍혔던 거예요. 억울하죠 (；一_一)

여기서는 sys.executable, 그러니까 '지금 이 파일을 돌리고 있는 바로 그 인터프리터'를
써요. 어떤 파이썬으로 실행하든 같은 파이썬으로 채점되니까 안전해요!
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
DRILLS = sorted(p for p in HERE.glob("*.py") if p.name != "check.py")


def main():
    targets = DRILLS
    if len(sys.argv) > 1:
        key = sys.argv[1]
        targets = [p for p in DRILLS if p.name.startswith(key)]
        if not targets:
            print(f"'{key}' 로 시작하는 드릴 파일이 없네요!")
            return 1

    results = []
    for path in targets:
        print("\n" + "#" * 68)
        print(f"# {path.name}")
        print("#" * 68)
        proc = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        print(proc.stdout, end="")
        if proc.stderr.strip():
            print("--- stderr ---")
            print(proc.stderr, end="")
        results.append((path.name, proc.returncode == 0))

    print("\n" + "=" * 68)
    print("전체 결과")
    print("=" * 68)
    for name, ok in results:
        print(f"  [{'통과' if ok else '아직'}] {name}")
    done = sum(ok for _, ok in results)
    print(f"\n  {done} / {len(results)}")
    return 0 if done == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
