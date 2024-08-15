from math import inf
def divide(first, second):
    if second == 0:
        return inf
    num2 = first / second
    return round(num2, 1)
