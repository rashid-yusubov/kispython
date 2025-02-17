#  Задача №3
Реализовать итерационную функцию:

![image](https://github.com/user-attachments/assets/c185cafd-a314-441b-a44b-f4e781e3c09a)

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
import math


def main(n, m, a, x):
    result = 0
    for c in range(1, a + 1):
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                term = (
                    65 * math.cos(j) ** 6
                    - 61 * c ** 6
                    - 38 * (59 - i ** 3 - x) ** 4
                )
                result += term
    return result

```

## 2-е по популярности решение

```python
import math


def main(n, m, a, x):
    return sum(
        65 * math.cos(j) ** 6 - 61 * c ** 6 - 38 * (59 - i ** 3 - x) ** 4
        for c in range(1, a + 1)
        for j in range(1, m + 1)
        for i in range(1, n + 1)
    )

```
## 3-е по популярности решение

```python
from math import cos, pow
from functools import reduce


def main(n, m, a, x):
    return reduce(
        lambda acc_c, c: acc_c + reduce(
            lambda acc_j, j: acc_j + reduce(
                lambda acc_i, i: acc_i + (
                    65 * pow(cos(j), 6) - 61 * pow(c, 6) -
                    38 * pow(59 - pow(i, 3) - x, 4)
                ),
                range(1, n + 1),
                0
            ),
            range(1, m + 1),
            0
        ),
        range(1, a + 1),
        0
    )

```

## 4-е по популярности решение

```python
import math


def main(n, m, a, x):
    result = 0
    c = 1
    while c <= a:
        j = 1
        while j <= m:
            i = 1
            while i <= n:
                term = (
                    65 * math.cos(j) ** 6
                    - 61 * c ** 6
                    - 38 * (59 - i ** 3 - x) ** 4
                )
                result += term
                i += 1
            j += 1
        c += 1
    return result

```

## 5-е по популярности решение

```python
import math


def recursive_sum(c, m, n, a, x):
    if c > a:
        return 0
    result = 0
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            term = (
                65 * math.cos(j) ** 6
                - 61 * c ** 6
                - 38 * (59 - i ** 3 - x) ** 4
            )
            result += term
    return result + recursive_sum(c + 1, m, n, a, x)


def main(n, m, a, x):
    return recursive_sum(1, m, n, a, x)

```