from random import randrange as RR

def r(x, y):
    s = True
    while s:
        v = RR(x, y)
        if v % 5 == 0:
            s = False
            yield RR(x, y)

result = []
for x in range(3):
    result += list(r(500, 999))

print(result)
