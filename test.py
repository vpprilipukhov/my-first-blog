n = 0
a_min = 9505 # почему такое начальное значение?

for i in range(1107, 9504 + 1):
    if i % 9 == 0 and i %  7 != 0 and i % 15 != 0 \
                  and i % 17 != 0 and i % 19 != 0:
        n += 1
        a_min = min(a_min, i)

print(n, a_min)

print(min([3,4,3,-20]))