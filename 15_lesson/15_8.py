def arithmetic_operation(a):
    if a == '+':
        return lambda x, y: x + y
    elif a == '-':
        return lambda x, y: x - y
    elif a == '*':
        return lambda x, y: x * y
    elif a == '/':
        return lambda x, y: x / y


operation = arithmetic_operation('*')
print(operation(2, 4))
