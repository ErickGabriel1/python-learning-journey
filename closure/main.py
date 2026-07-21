def operation(multiplier):
    def number(multiplicand):
        product = multiplier * multiplicand
        return product
    return number


double = operation(2)
triple = operation(3)
quadruple = operation(4)

print(double(10))
print(triple(10))
print(quadruple(10))

