#  Задача №6
Реализовать целочисленную функцию, вычисляющую  на основе входного множества :

![image](https://github.com/user-attachments/assets/38726a30-258f-42ef-b915-4184c5f3bdfb)

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
def main(delta_set):
    O_set = {d % 3 + d for d in delta_set if -12 <= d < 57}
    Xi = {5 * d for d in delta_set if (d <= 71) ^ (d > -10)}
    T_set = {x ** 2 for x in Xi if x > 42 or x <= -58}
    beta = len(O_set | T_set) + sum(abs(t) for t in T_set)
    return beta

```

## 2-е по популярности решение

```python
def _calculate_o_set(delta_set):
    O_set = set()
    for d in delta_set:
        if -12 <= d < 57:
            O_set.add(d % 3 + d)
    return O_set


def _calculate_xi(delta_set):
    Xi = set()
    for d in delta_set:
        if (d <= 71) ^ (d > -10):
            Xi.add(5 * d)
    return Xi


def _calculate_t_set(xi):
    T_set = set()
    for x in xi:
        if x > 42 or x <= -58:
            T_set.add(x ** 2)
    return T_set


def main(delta_set):
    O_set = _calculate_o_set(delta_set)
    Xi = _calculate_xi(delta_set)
    T_set = _calculate_t_set(Xi)
    beta = len(O_set | T_set) + sum(abs(t) for t in T_set)
    return beta

```
