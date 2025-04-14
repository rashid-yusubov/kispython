def main(delta_set):
    O_set = {d % 3 + d for d in delta_set if -12 <= d < 57}
    Xi = {5 * d for d in delta_set if (d <= 71) ^ (d > -10)}
    T_set = {x ** 2 for x in Xi if x > 42 or x <= -58}
    beta = len(O_set | T_set) + sum(abs(t) for t in T_set)
    return beta
