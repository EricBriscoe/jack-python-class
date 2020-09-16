def division(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error! Cannot divide by zero!"


print(division(4, 2))
print(division(3, 2))
print(division(2, 0))
