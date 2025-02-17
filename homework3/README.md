#  Задача №3. 
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
