#  Задача №4
Реализовать функцию по рекуррентной формуле:

![image](https://github.com/user-attachments/assets/5980c7f1-92a7-47ef-af1b-05cda12089ff)

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
import math


def main(n):
    if n == 0:
        return -0.06
    elif n == 1:
        return 0.31
    else:
        return math.cos(main(n - 1)) ** 3 - main(n - 2) ** 2 - 1

```

## 2-е по популярности решение

```python
import math


def recurrence_generator():
    yield -0.06  # f(0)
    yield 0.31   # f(1)
    fn_minus_2 = -0.06
    fn_minus_1 = 0.31
    while True:
        fn = math.cos(fn_minus_1) ** 3 - fn_minus_2 ** 2 - 1
        yield fn
        fn_minus_2, fn_minus_1 = fn_minus_1, fn


def main(n):
    gen = recurrence_generator()
    result = None
    for _ in range(n + 1):
        result = next(gen)
    return result

```
## 3-е по популярности решение

```python
import math


def main(n):
    dp = [-0.06, 0.31] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = math.cos(dp[i - 1]) ** 3 - dp[i - 2] ** 2 - 1
    return dp[n]

```

## 4-е по популярности решение

```python
import math


def main(n):
    sign = n
    match sign:
        case 0:
            return -0.06
        case 1:
            return 0.31

    return (math.cos(main(n - 1)) ** 3 - main(n - 2) ** 2 - 1)

```

## 5-е по популярности решение

```python
import math


def main(n):
    return (
        -0.06 if n == 0 else
        0.31 if n == 1 else
        math.cos(main(n - 1)) ** 3 - main(n - 2) ** 2 - 1
    )

```
