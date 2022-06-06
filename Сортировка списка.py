massive = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']
massive.pop(11)
del massive[4:7]


def sorter(massive):
    massive.sort()
    return massive

print(sorter(massive))