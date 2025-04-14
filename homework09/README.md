#  Задача №9

Реализовать функцию для разбора строки, содержащей данные в текстовом формате. Изучить детали формата по приведенным ниже примерам. Результат вернуть в виде словаря.

*Пример 1*

Входная строка:

```bash
begin <section> equ @"soaran_728" := #-2539 </section>, <section>equ
@"orre":= #1618</section>, <section> equ @"alaaner_614" := #-4006
</section>,<section> equ @"xeri_304" := #8685 </section>, end
```

Разобранный результат:

```bash
{'soaran_728': -2539,
 'orre': 1618,
 'alaaner_614': -4006,
 'xeri_304': 8685}
```

*Пример 2*

Входная строка:

```bash
begin<section>equ @"laquza":= #2886 </section>, <section> equ
@"onrile" :=#3726 </section>, <section> equ @"gexeen" :=
#-1457</section>,end
```

Разобранный результат:

```bash
{'laquza': 2886, 'onrile': 3726, 'gexeen': -1457}
```

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Самое популярное решение

```python
import re


def main(text: str) -> dict:
    pattern = re.compile(r'@"(.*?)"\s*:=\s*#(-?\d+)')
    return {match[0]: int(match[1]) for match in pattern.findall(text)}

```

## 2-е по популярности решение

```python
def main(text: str) -> dict:
    result = {}
    text = text[text.find("begin") + 5:text.rfind("end")].strip()
    sections = text.split("<section>")
    for section in sections:
        if "@\"" in section and "#" in section:
            key_start = section.find("@\"") + 2
            key_end = section.find("\"", key_start)
            key = section[key_start:key_end]
            value_start = section.find("#", key_end) + 1
            value_end = section.find("</section>", value_start)
            value = int(section[value_start:value_end].strip())
            result[key] = value
    return result

```
 