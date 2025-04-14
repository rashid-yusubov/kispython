class DecisionTree:
    def __init__(self, items):
        self.items = items

    def zero(self, left, right):
        if self.items[0] == 2020:
            return left
        elif self.items[0] == 1973:
            return right
        return None

    def one(self, left, midd, right):
        if self.items[1] == 2014:
            return left
        elif self.items[1] == 2018:
            return midd
        elif self.items[1] == 1997:
            return right
        return None

    def two(self, left, midd, right):
        if self.items[2] == 2002:
            return left
        elif self.items[2] == 1972:
            return midd
        elif self.items[2] == 2005:
            return right
        return None

    def three(self, left, midd, right):
        if self.items[3] == 2002:
            return left
        elif self.items[3] == 1960:
            return midd
        elif self.items[3] == 1963:
            return right
        return None

    def four(self, left, midd, right):
        if self.items[4] == "EBNF":
            return left
        elif self.items[4] == "YACC":
            return midd
        elif self.items[4] == "CHUCK":
            return right
        return None

    def main(self):
        return self.two(
            13,
            12,
            self.one(
                self.four(11, self.three(10, 9, 8), 7),
                self.three(6, 5, 4),
                self.zero(3, self.four(2, 1, 0))
            )
        )


def main(items):
    tree = DecisionTree(items)
    return tree.main()
