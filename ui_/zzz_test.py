def f(x):
    result = {
        'a': lambda x: x * 25,
        'b': lambda x: x + 7,
        'c': lambda x: x - 2
    }[x](x)
    return result


print(f(3))

