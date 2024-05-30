def add(*args):
    x = 0
    for n in args:
        x += n
    return x

print(add(3, 4, 5, 6))