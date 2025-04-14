#  Задача №5
Реализовать функцию, оперирующую векторами длины:

![image](https://github.com/user-attachments/assets/bce78a1e-0a03-40d2-8b7a-23a30f6a4f27)

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
def main(x, y, z):
    n = len(x)
    result = 0.0
    for i in range(1, n + 1):
        term = (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
        result += term
    return 77 * result

```

## 2-е по популярности решение

```python
def main(x, y, z):
    n = len(x)
    return 77 * sum(
        (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
        for i in range(1, n + 1)
    )

```
## 3-е по популярности решение

```python
def main(x, y, z):
    n = len(x)
    result = 0.0
    i = 1

    while i <= n:
        term = (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
        result += term
        i += 1

    return 77 * result

```

## 4-е по популярности решение

```python
def helper(i, x, y, z, n):
    if i > n:
        return 0
    term = (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
    return term + helper(i + 1, x, y, z, n)


def main(x, y, z):
    return 77 * helper(1, x, y, z, len(x))

```
