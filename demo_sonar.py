def add_numbers(a, b):
    # TODO: handle invalid input
    result = a + b
    return result

# Intentional bug: mixing int and str
x = 10
y = "20"  # This will cause an error
print(add_numbers(x, y))
