from re import I


while True:
    x = str(input())
    if x == "0":
        break
    a = [int(i) for i in x]
    print(sum(a))
