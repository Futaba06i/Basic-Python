import itertools
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    m = 0
    for i in itertools.combinations(range(1, n+1, 1), 3):
        if sum(i) == x:
            m += 1
    print(m)
