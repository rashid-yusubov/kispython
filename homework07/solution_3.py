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
