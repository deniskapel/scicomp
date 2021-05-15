def get_input(ord_number: str) -> int:
    return int(input("Tell me the %s number: " % (ord_number)))


operations = {
    'add': int.__add__,
    'multiply': int.__mul__,
    'divide': int.__truediv__,
    'subtract': int.__sub__
}

ops = ", ".join(operations.keys())

x = get_input('first')
y = get_input('second')
op = input("tell me the operation (%s): " % (ops))

try:
    print(operations[op](x, y))
except:
    print('Error! There are only these options: %s.' % (ops))
