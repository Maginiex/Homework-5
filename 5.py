def func_one(x):
    def wrapper():
        print(x()**2)
    return wrapper()


@func_one
def func_two():
    return 2 + 3