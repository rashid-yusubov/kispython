#  Задача №7
Реализовать функцию для вычисления дерева решений:

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
def zero(items, left, right):
    if items[0] == 2020:
        return left
    if items[0] == 1973:
        return right


def one(items, left, midd, right):
    if items[1] == 2014:
        return left
    if items[1] == 2018:
        return midd
    if items[1] == 1997:
        return right


def two(items, left, midd, right):
    if items[2] == 2002:
        return left
    if items[2] == 1972:
        return midd
    if items[2] == 2005:
        return right


def three(items, left, midd, right):
    if items[3] == 2002:
        return left
    if items[3] == 1960:
        return midd
    if items[3] == 1963:
        return right


def four(items, left, midd, right):
    if items[4] == "EBNF":
        return left
    if items[4] == "YACC":
        return midd
    if items[4] == "CHUCK":
        return right


def main(items):
    result = two(
        items,
        13,
        12,
        one(
            items,
            four(
                items,
                11,
                three(items, 10, 9, 8),
                7
            ),
            three(items, 6, 5, 4),
            zero(
                items,
                3,
                four(items, 2, 1, 0)
            )
        )
    )
    return result

```

## 2-е по популярности решение

```python
s = (
    {2005, 1997, 1973, "CHUCK"},
    {2005, 1997, 1973, "YACC"},
    {2005, 1997, 1973, "EBNF"},
    {2005, 1997, 2020},
    {2005, 2018, 1963},
    {2005, 2018, 1960},
    {2005, 2018, 2002},
    {2005, 2014, "CHUCK"},
    {2005, 2014, "YACC", 1963},
    {2005, 2014, "YACC", 1960},
    {2005, 2014, "YACC", 2002},
    {2005, 2014, "EBNF"},
    {1972},
    {2002},
)


def main(r):
    s1 = set(r)
    s2 = [i for i in range(len(s)) if not (len(s[i] - s1))][0]
    return s2

```

## 3-е по популярности решение

```python
def zero(items, left, right):
    match items[0]:
        case 2020:
            return left
        case 1973:
            return right


def one(items, left, midd, right):
    match items[1]:
        case 2014:
            return left
        case 2018:
            return midd
        case 1997:
            return right


def two(items, left, midd, right):
    match items[2]:
        case 2002:
            return left
        case 1972:
            return midd
        case 2005:
            return right


def three(items, left, midd, right):
    match items[3]:
        case 2002:
            return left
        case 1960:
            return midd
        case 1963:
            return right


def four(items, left, midd, right):
    match items[4]:
        case "EBNF":
            return left
        case "YACC":
            return midd
        case "CHUCK":
            return right


def main(items):
    result = two(
        items,
        13,
        12,
        one(
            items,
            four(
                items,
                11,
                three(items, 10, 9, 8),
                7
            ),
            three(items, 6, 5, 4),
            zero(
                items,
                3,
                four(items, 2, 1, 0)
            )
        )
    )
    return result

```

## 4-е по популярности решение

```python
s = (
    {2005, 1997, 1973, "CHUCK"},
    {2005, 1997, 1973, "YACC"},
    {2005, 1997, 1973, "EBNF"},
    {2005, 1997, 2020},
    {2005, 2018, 1963},
    {2005, 2018, 1960},
    {2005, 2018, 2002},
    {2005, 2014, "CHUCK"},
    {2005, 2014, "YACC", 1963},
    {2005, 2014, "YACC", 1960},
    {2005, 2014, "YACC", 2002},
    {2005, 2014, "EBNF"},
    {1972},
    {2002},
)


def main(items):
    s1 = set(items)
    for i, v in enumerate(s):
        if not(len(v - s1)):
            return i

```

## 5-е по популярности решение

```python

```