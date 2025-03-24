#  Задача №8

Реализовать функцию для кодирования данных, содержащих битовые поля. В решении необходимо использовать побитовые операции. Неиспользуемые поля результата должны содержать нулевые биты.

*Входные данные:*

Список из битовых полей в виде пар имя-значение. Значения битовых полей имеют тип: целое.

![Без имени](https://github.com/user-attachments/assets/9d93a820-216b-4ef8-89af-4508aea83135)

*Выходные данные:*

Десятичная строка. 

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
def main(fields):
    result = 0
    for name, value in fields:
        if name == 'N1':
            result |= (value & 0b111) << 0
        elif name == 'N2':
            result |= (value & 0b111111) << 3
        elif name == 'N3':
            result |= (value & 0b111111111) << 9
        elif name == 'N5':
            result |= (value & 0b1111111111) << 27
    return str(result)

```

## 2-е по популярности решение

```python
def main(fields):
    result = 0
    field_specs = {
        'N1': {'start_bit': 0, 'size': 3},
        'N2': {'start_bit': 3, 'size': 6},
        'N3': {'start_bit': 9, 'size': 9},
        'N5': {'start_bit': 27, 'size': 10}
    }
    for name, value in fields:
        if name in field_specs:
            start_bit = field_specs[name]['start_bit']
            size = field_specs[name]['size']
            mask = (1 << size) - 1
            masked_value = value & mask
            result |= (masked_value << start_bit)
    return str(result)

```
