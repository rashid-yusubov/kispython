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
