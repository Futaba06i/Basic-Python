while True:
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == 0 and l[1] == 0:
        break
    print(l[0], l[1])
