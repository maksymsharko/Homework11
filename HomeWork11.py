# 1. double_result
# This decorator function should return the result of another function multiplied by two
print("_______________________________________________________________________")
print("1. Double result ")


def double_result(func):
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b


print(add(5, 5))


@double_result
def add(a, b):
    return a + b


print(add(5, 5))
print("_______________________________________________________________________")
# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!

print("2. Only odd parametres ")


def only_odd_parametres(func):
    def inner(*args):
        for arr in args:
            if arr % 2 == 0:
                print(f'{args}')
                return 'Please, use only odd numbers!'
        return func(*args)

    return inner


@only_odd_parametres
def add(a, b):
    print(f'{a} + {b}')
    return a + b


print(add(5, 5))
print(add(4, 4))


@only_odd_parametres
def multiply(a, b, c, d, e):
    print(f"Result: {a} * {b} * {c} * {d} * {e}")
    return a * b * c * d * e


print(multiply(1, 2, 3, 4, 5))
print(multiply(5, 5, 3, 6, 2))
print("_______________________________________________________________________")
# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):
print("3. Logged")


def logged(func):
    def inner(*args, **kwargs):
        print(f'Result: {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return inner


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


print(func(4, 4, 4))
print("_______________________________________________________________________")

# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.
print("4. Type check")


def type_check(correct_type):
    def type_dec(func):
        def inner(arr):
            if isinstance(arr, correct_type):
                return func(arr)
            else:
                print(f'Wrong Type: {type(arr)}')
        return inner
    return type_dec


@type_check(int)
def times2(num):
    return f'{num * 2}'


print(times2(2))
times2('Not a Number')


@type_check(str)
def first_letter(word):
    return f'{word[0]}'


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
print("_______________________________________________________________________")
