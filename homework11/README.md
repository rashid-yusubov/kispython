#  Задача №11

Конечный автомат Мура представлен графом на картинке ниже. Необходимо реализовать этот конечный автомат в виде класса. Переходы из состояния в состояние осуществляются с помощью методов, названия которых основаны на словах, указанных на дугах графа (см. пример ниже).

1. Реализовать метод has_max_out_edges класса конечного автомата. Этот метод возвращает истину, если текущее состояние имеет максимальное число выходных дуг в графе.

2. Реализовать метод seen_edge класса конечного автомата. Этот метод возвращает число совершенных переходов между парой состояний-аргументов.

3. Реализовать методы для задания значений переменных. Эти переменные определяют выбор перехода там, где состояние имеет несколько выходных дуг, помеченных одним и тем же методом (см. граф).

4. Реализовать метод has_max_in_edges класса конечного автомата. Этот метод возвращает истину, если текущее состояние имеет максимальное число входных дуг в графе.

5. Реализовать функцию main, возвращающую экземпляр класса конечного автомата.

6. Реализовать обработку ошибок с помощью пользовательского класса исключения MachineException. При возбуждении (raise) исключения сообщение об ошибке является словом, которое определяет, оказался ли метод перехода неподдерживаемым ('unsupported') в данном состоянии или неизвестным ('unknown') для конечного автомата.

7. Реализовать функцию test для тестирования класса конечного автомата на основе метрики покрытия ветвей (branch coverage). Требуемая степень покрытия: 100%.

Детали работы методов класса конечного автомата показаны на примере, приведенном далее. Переменная obj содержит объект этого класса.



```
obj.set_u(0) # None
obj.select_init() # MachineException: 'unknown'
obj.set_g(1) # None
obj.set_v(1) # None
obj.seen_edge('m5', 'm4') # 0
obj.select_leer() # None
obj.seen_edge('m3', 'm1') # 0
obj.has_max_out_edges() # True
obj.seen_edge('m7', 'm4') # 0
obj.get_output() # 'H3'
obj.select_start() # None
obj.has_max_out_edges() # True
obj.get_output() # 'H3'
obj.select_swap() # None
obj.get_output() # 'H2'
obj.select_swap() # None
obj.select_scrub() # MachineException: 'unknown'
obj.get_output() # 'H5'
obj.seen_edge('m6', 'm6') # 0
obj.has_max_out_edges() # False
obj.select_init() # MachineException: 'unknown'
obj.select_post() # None
obj.select_copy() # MachineException: 'unknown'
obj.get_output() # 'H4'
obj.has_max_in_edges() # True
obj.select_warp() # None
obj.set_u(1) # None
obj.select_rush() # MachineException: 'unknown'
obj.get_output() # 'H4'
obj.has_max_out_edges() # False
obj.seen_edge('m7', 'm5') # 1
obj.select_warp() # None
obj.select_rush() # MachineException: 'unknown'
obj.get_output() # 'H4'
obj.seen_edge('m7', 'm4') # 0
obj.select_drag() # MachineException: 'unknown'
obj.select_start() # None
obj.get_output() # 'H2'
obj.select_post() # None
obj.get_output() # 'H6'
obj.select_post() # None
obj.get_output() # 'H2'
obj.select_leer() # MachineException: 'unsupported'
```

В отправляемом коде на языке программирования Python должна присутствовать функция main и не должно быть какого-либо ввода/вывода. Поддерживается использование модулей только из стандартной библиотеки Python.

## Решение

```python
class MachineException(Exception):
    pass


class MooreMachine:
    def __init__(self):
        self.state = 'm2'
        self.u = 0
        self.v = 0
        self.g = 0
        self.edge_count = {}
        self.outputs = {
            'm0': 'H6', 'm1': 'H2', 'm2': 'H5', 'm3': 'H4',
            'm4': 'H5', 'm5': 'H2', 'm6': 'H4', 'm7': 'H3'
        }
        self.out_edges = {
            'm0': 1, 'm1': 1, 'm2': 1, 'm3': 1, 'm4': 1,
            'm5': 2, 'm6': 2, 'm7': 3
        }
        self.in_edges = {
            'm0': 1, 'm1': 1, 'm2': 0, 'm3': 1, 'm4': 2,
            'm5': 2, 'm6': 3, 'm7': 2
        }

    def __getattr__(self, name):
        if name.startswith('select_'):
            def unknown_method(*args, **kwargs):
                raise MachineException('unknown')
            return unknown_method
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no "
            f"attribute '{name}'"
        )

    def set_u(self, value):
        self.u = value

    def set_v(self, value):
        self.v = value

    def set_g(self, value):
        self.g = value

    def get_output(self):
        return self.outputs[self.state]

    def has_max_out_edges(self):
        max_out = max(self.out_edges.values())
        return self.out_edges[self.state] == max_out

    def has_max_in_edges(self):
        max_in = max(self.in_edges.values())
        return self.in_edges[self.state] == max_in

    def seen_edge(self, from_state, to_state):
        key = (from_state, to_state)
        return self.edge_count.get(key, 0)

    def _increment_edge(self, from_state, to_state):
        key = (from_state, to_state)
        self.edge_count[key] = self.edge_count.get(key, 0) + 1

    def select_post(self):
        current = self.state
        if current == 'm0':
            self.state = 'm5'
        elif current == 'm1':
            self.state = 'm0'
        elif current == 'm4':
            self.state = 'm6'
        elif current == 'm5':
            self.state = 'm4'
        else:
            raise MachineException('unsupported')
        self._increment_edge(current, self.state)

    def select_start(self):
        current = self.state
        if current == 'm3':
            self.state = 'm1'
        elif current == 'm7':
            self.state = 'm7'
        else:
            raise MachineException('unsupported')
        self._increment_edge(current, self.state)

    def select_leer(self):
        current = self.state
        if current == 'm2':
            self.state = 'm7'
        else:
            raise MachineException('unsupported')
        self._increment_edge(current, self.state)

    def select_swap(self):
        current = self.state
        if current == 'm7':
            if self.g == 0:
                self.state = 'm4'
            else:
                self.state = 'm5'
        elif current == 'm5':
            if self.v == 0:
                self.state = 'm6'
            else:
                self.state = 'm4'
        else:
            raise MachineException('unsupported')
        self._increment_edge(current, self.state)

    def select_warp(self):
        current = self.state
        if current == 'm6':
            if self.u == 0:
                self.state = 'm6'
            else:
                self.state = 'm3'
        else:
            raise MachineException('unsupported')
        self._increment_edge(current, self.state)


def main():
    return MooreMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    # Создаем экземпляр машины
    obj = main()

    # Проверка начального состояния
    assert obj.state == 'm2'
    assert obj.u == 0
    assert obj.v == 0
    assert obj.g == 0
    assert obj.edge_count == {}
    assert obj.get_output() == 'H5'

    # Тесты для set_u, set_v, set_g
    obj.set_u(42)
    assert obj.u == 42
    obj.set_v(99)
    assert obj.v == 99
    obj.set_g(1)
    assert obj.g == 1

    # Тесты для get_output
    obj.state = 'm0'
    assert obj.get_output() == 'H6'
    obj.state = 'm7'
    assert obj.get_output() == 'H3'
    obj.state = 'm2'  # Возвращаем начальное состояние

    # Тесты для has_max_out_edges
    assert not obj.has_max_out_edges()  # m2: 1, max: 3
    obj.state = 'm7'
    assert obj.has_max_out_edges()  # m7: 3, max: 3
    obj.state = 'm5'
    assert not obj.has_max_out_edges()  # m5: 2, max: 3
    obj.state = 'm2'

    # Тесты для has_max_in_edges
    assert not obj.has_max_in_edges()  # m2: 0, max: 3
    obj.state = 'm6'
    assert obj.has_max_in_edges()  # m6: 3, max: 3
    obj.state = 'm4'
    assert not obj.has_max_in_edges()  # m4: 2, max: 3
    obj.state = 'm2'

    # Тесты для seen_edge и _increment_edge
    assert obj.seen_edge('m2', 'm7') == 0
    obj._increment_edge('m2', 'm7')
    assert obj.seen_edge('m2', 'm7') == 1
    obj._increment_edge('m2', 'm7')
    assert obj.seen_edge('m2', 'm7') == 2
    obj.edge_count.clear()  # Очищаем для следующих тестов

    # Тесты для select_post
    obj.state = 'm0'
    obj.select_post()
    assert obj.state == 'm5'
    assert obj.seen_edge('m0', 'm5') == 1
    obj.edge_count.clear()

    obj.state = 'm1'
    obj.select_post()
    assert obj.state == 'm0'
    assert obj.seen_edge('m1', 'm0') == 1
    obj.edge_count.clear()

    obj.state = 'm4'
    obj.select_post()
    assert obj.state == 'm6'
    assert obj.seen_edge('m4', 'm6') == 1
    obj.edge_count.clear()

    obj.state = 'm5'
    obj.select_post()
    assert obj.state == 'm4'
    assert obj.seen_edge('m5', 'm4') == 1
    obj.edge_count.clear()

    obj.state = 'm2'
    raises(lambda: obj.select_post(), MachineException)

    # Тесты для select_start
    obj.state = 'm3'
    obj.select_start()
    assert obj.state == 'm1'
    assert obj.seen_edge('m3', 'm1') == 1
    obj.edge_count.clear()

    obj.state = 'm7'
    obj.select_start()
    assert obj.state == 'm7'
    assert obj.seen_edge('m7', 'm7') == 1
    obj.edge_count.clear()

    obj.state = 'm2'
    raises(lambda: obj.select_start(), MachineException)

    # Тесты для select_leer
    obj.state = 'm2'
    obj.select_leer()
    assert obj.state == 'm7'
    assert obj.seen_edge('m2', 'm7') == 1
    obj.edge_count.clear()

    obj.state = 'm0'
    raises(lambda: obj.select_leer(), MachineException)

    # Тесты для select_swap
    obj.state = 'm7'
    obj.set_g(0)
    obj.select_swap()
    assert obj.state == 'm4'
    assert obj.seen_edge('m7', 'm4') == 1
    obj.edge_count.clear()

    obj.state = 'm7'
    obj.set_g(1)
    obj.select_swap()
    assert obj.state == 'm5'
    assert obj.seen_edge('m7', 'm5') == 1
    obj.edge_count.clear()

    obj.state = 'm5'
    obj.set_v(0)
    obj.select_swap()
    assert obj.state == 'm6'
    assert obj.seen_edge('m5', 'm6') == 1
    obj.edge_count.clear()

    obj.state = 'm5'
    obj.set_v(1)
    obj.select_swap()
    assert obj.state == 'm4'
    assert obj.seen_edge('m5', 'm4') == 1
    obj.edge_count.clear()

    obj.state = 'm2'
    raises(lambda: obj.select_swap(), MachineException)

    # Тесты для select_warp
    obj.state = 'm6'
    obj.set_u(0)
    obj.select_warp()
    assert obj.state == 'm6'
    assert obj.seen_edge('m6', 'm6') == 1
    obj.edge_count.clear()

    obj.state = 'm6'
    obj.set_u(1)
    obj.select_warp()
    assert obj.state == 'm3'
    assert obj.seen_edge('m6', 'm3') == 1
    obj.edge_count.clear()

    obj.state = 'm2'
    raises(lambda: obj.select_warp(), MachineException)

    # Тесты для неподдерживаемых методов через __getattr__
    raises(lambda: obj.select_scrub(), MachineException)
    raises(lambda: obj.select_debug(), MachineException)
    raises(lambda: obj.select_stop(), MachineException)

    # Тест для AttributeError в __getattr__ для не-select атрибута
    try:
        obj.some_attribute
    except AttributeError:
        pass


test()

```