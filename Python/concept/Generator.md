# Generator
---
- 파이썬의 시퀀스를 생성하는 객체이다.
- 전체 시퀀스를 한 번에 메모리에 생성하고 정렬할 필요 없이, 잠재적으로 아주 큰 시퀀스를 순회할 수 있다.
- 제너레이터는 이터레이터에 대한 데이터의 소스로 자주 사용된다.
- 제너레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환한다.
- 제너레이터는 일반 함수와 다르다. 일반 함수는 이전 호출에 대한 메모리가 없고, 항상 똑같은 상태로 첫 번째 라인부터 수행한다.
---
### Code Example
```python
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)
for x in ranger(1, 5):
    print(x) # 1 2 3 4
```