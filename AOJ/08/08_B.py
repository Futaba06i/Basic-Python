while True:
    x = str(input())
    if x == "0":
        break
    print(sum([int(i) for i in x]))
