# Separation of concerns

```python
x = int(input("Tell me the first number: "))
y = int(input("Tell me the second number: "))
op = input("tell me the operation (add, multiply): ")

if op == "add":
  print("result: ", x+y)
elif op == "multiply":
  print("result: ", x*y)
```

## Exercise: In the above program, identify and describe at least two of the sub-problems which are solved multiple times. (I see at least three or four.)

1. It asks for the input several times - the first two are different in the ordinal number only.
2. Printing out differs in an operations


## Exercise: Choose one of the sub-problems, write a common solution to that subproblem in the form of a function, and modify the program to use your common solution instead of solving the problem multiple times.

```python
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
```