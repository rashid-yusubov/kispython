#  Задача №2
Реализовать кусочную функцию:

![image](https://github.com/user-attachments/assets/5127484d-e00b-4383-b4e4-805b11d8f71e)

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
import math


def main(z):
    if z < 109:
        return math.log10(1 + z / 65 + z**3)

    elif 109 <= z < 121:
        return 90 * (z**3 + z**2 + 1) + math.log(z)

    else:
        arctg = math.atan(z**2 - 19 - (z**3 / 8))
        return 92 + 60 * math.log10(z) ** 2 + 34 * (arctg) ** 3

```

## 2-е по популярности решение

```python
import math


def main(z):
    conditions = [
        (
            lambda z: z < 109,
            lambda z: math.log10(1 + z / 65 + z**3)
        ),
        (
            lambda z: 109 <= z < 121,
            lambda z: 90 * (z**3 + z**2 + 1) + math.log(z)
        ),
        (
            lambda z: z >= 121,
            lambda z: (
                92 +
                60 * math.log10(z) ** 2 +
                34 * (math.atan(z**2 - 19 - (z**3 / 8))) ** 3
            )
        )
    ]

    return next(
        func(z)
        for condition, func in conditions
        if condition(z)
    )

```

## 3-е по популярности решение

```python
import math
import bisect


def main(z):
    limits = [109, 121]
    funcs = [
        lambda z: math.log10(1 + z / 65 + z**3),
        lambda z: 90 * (z**3 + z**2 + 1) + math.log(z),
        lambda z: 92 + 60 * math.log10(z) ** 2 +
        34 * (math.atan(z**2 - 19 - (z**3 / 8))) ** 3,
    ]
    return funcs[bisect.bisect(limits, z)](z)

```
