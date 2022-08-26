import random


def move(num, r):

    if r == "E":
        return[num[3], num[1], num[0], num[5], num[4], num[2]]
    elif r == "S":
        return[num[4], num[0], num[2], num[3], num[5], num[1]]
    elif r == "W":
        return[num[2], num[1], num[5], num[0], num[4], num[3]]
    elif r == "N":
        return[num[1], num[5], num[2], num[3], num[0], num[4]]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
h = ("N", "W", "S", "E")
for i in range(100):
    num = random.randrange(4)
    a = move(a, h[num])
    if a == b:
        print("Yes")
        exit()
print("No")
