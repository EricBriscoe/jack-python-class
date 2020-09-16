def safeDivision(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error! Cannot divide by zero!"

def unsafeDivision(numerator, denominator):
    return numerator / denominator

print(safeDivision(4, 2))
print(safeDivision(2, 0))
print(safeDivision(3, 2))




print(unsafeDivision(4, 2))
print(unsafeDivision(2, 0))
print(unsafeDivision(3, 2))

