comp = {(0, 0): (0, 1) (1, 0)}
print(comp)
target = (0, 0)
a = {}
a |= set(comp[target])
print(a)