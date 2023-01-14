def f(n):
    if n == 0:
        return 1
    return n - m(f((n-1)))
def m(n):
    if n == 0:
        return 0
    return n - f(m((n-1)))

counter = 0
while counter<20:
    counter += 1
    print(f"{f(counter),m(counter)}")
    