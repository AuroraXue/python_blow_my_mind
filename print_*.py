ls = [(1,2), (3,4), (5,6)]
print(*ls)
## result: (1, 2) (3, 4) (5, 6)

[print(*c) for c in ls]
# result:
# 1 2
# 3 4
# 5 6

print(*ls, sep = '\n')
# result:
# (1, 2)
# (3, 4)
# (5, 6)

