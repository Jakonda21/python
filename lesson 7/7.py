def present(x, y):
    if x > y:
        x, y = y, x
    return sum(range(x, y+1))

print(present(5, 14))
print(present(-3, 6))


