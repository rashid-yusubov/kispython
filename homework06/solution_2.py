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
