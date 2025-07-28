def squares(n):
    for i in range(1,n+1):
        yield i*i
for i in squares(5):
    print(i)
print(type(squares))
print([*squares(6)])