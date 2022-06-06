num = [1, 2, 3, 4, 5]
def func(x):
    return x>2
num = list(filter(func, num))
print(num)
def func2(y):
    return y**2
num = list(map(func2, num))
print(num)