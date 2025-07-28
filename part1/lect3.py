def squares():
    yield 1
    yield 4
    yield 9
    yield 16
for i in squares():
    print(i)
print(type(squares))