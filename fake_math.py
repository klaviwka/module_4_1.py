def divide(first, second):
    if second == 0:
        return "Ошибка"
    num1 = first / second
    return round(num1, 1)