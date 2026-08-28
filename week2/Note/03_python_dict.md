# 자료구조 층위 혼동

student는 딕셔너리가 아니라 딕셔너리들이 든 리스트였다.

```
struct Student { char *name; int score; };
struct Student students[4];
// students.score    → 컴파일 에러 (배열 전체에 필드를 물음)
// students[0].score → 정상
```

## 1. 1차 시도
| 코드 | 에러 | 원인 |
|---|---|---|
| `students.get('score')` | `AttributeError: 'list' object has no attribute 'get'` | 리스트를 딕셔너리로 착각 |
| `average = score / members` | — | 리스트를 정수로 나눔 |
| `[[] for x in students['name'] if students[score] >= average]` | — | 표현식/이터러블/조건 **세 자리 모두** 틀림 |

## 2. 2차 시도

```
for x in range(members):   # x = 0,1,2,3        (숫자)
for x in students:         # x = {"name":...}   (딕셔너리)
```
같은 x인데 안에 담긴게 다름, 아래에서 student[x]를 붙여 typeerror: list indices must be integers of slices, not dict 발생
