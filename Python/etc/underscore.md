파이썬에서 변수에 Underscore(_)를 붙이는 이유는 주로 다음과 같은 경우에 사용된다.

1. **Private variable**: 클래스의 멤버 변수를 private으로 표시하기 위해 단일 언더스코어(_)를 사용한다. 이는 파이썬에서는 강제적으로 private이 아닌, 관례적인 표시이므로 외부에서 접근이 가능하지만, 개발자가 클래스 내부에서만 사용하기를 원하는 변수임을 나타낸다.

```python
class MyClass:
    def __init__(self):
        self._private_variable = 10
```

2. **Name mangling**: 클래스 내부에서 사용되는 변수나 메서드에 더 강력한 private 기능을 제공하기 위해 두 개의 언더스코어(__)를 사용한다. 이렇게 정의된 변수나 메서드는 클래스 외부에서 직접적으로 접근하기 어려워진다. 파이썬에서는 이러한 경우 이름 변경(name mangling)을 통해 변수나 메서드 이름을 변경하여 접근을 어렵게 한다.

```python
class MyClass:
    def __init__(self):
        self.__private_variable = 10
```

3. **더미 변수**: 언더스코어(_)를 사용하여 더미 변수(dummy variable)를 표시하기도 한다. 이는 변수가 필요하지만 실제로 사용되지 않는 경우에 사용된다. 이를 통해 코드의 가독성을 높이고 불필요한 변수 사용을 줄일 수 있다.

```python
for _ in range(5):
    print("Hello, World!")
```