#  Задача №1
Реализовать функцию:

![image](https://github.com/user-attachments/assets/2e0210ae-a505-427d-a2ac-71d6470bbdaf)

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
import math


def main(x, y, z):
    term1 = y ** 2
    term2 = 11 * (math.floor(z ** 3 - 32 * x)) ** 6
    term3 = 34 * (math.sqrt(38 * z ** 2)) ** 6
    term4 = math.floor(y - 83 * x ** 3 - 67) ** 4

    return term1 - term2 - (term3 + term4)

```

## 2-е по популярности решение

```python
import math


def main(x, y, z):
    return (
        y ** 2
        - 11 * (math.floor(z ** 3 - 32 * x)) ** 6
        - (34 * (math.sqrt(38 * z ** 2)) ** 6
           + math.floor(y - 83 * x ** 3 - 67) ** 4)
    )

```

## 3-е по популярности решение

```python
from math import floor, sqrt


def main(x, y, z):
    term1 = y ** 2
    term2 = 11 * (floor(z ** 3 - 32 * x)) ** 6
    term3 = 34 * (sqrt(38 * z ** 2)) ** 6
    term4 = floor(y - 83 * x ** 3 - 67) ** 4

    return term1 - term2 - (term3 + term4)

```

## 4-е по популярности решение

```python
from math import floor, sqrt


def main(x, y, z):
    return (
        y ** 2
        - 11 * (floor(z ** 3 - 32 * x)) ** 6
        - (34 * (sqrt(38 * z ** 2)) ** 6
           + floor(y - 83 * x ** 3 - 67) ** 4)
    )

```
