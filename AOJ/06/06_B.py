n = int(input())
cards = [[False for i in range(13)]for j in range(4)]
pattern = ["S", "H", "C", "D"]
for i in range(n):
    ch, rank = map(str, input().split())
    r = int(rank)
    cards[pattern.index(ch)][r-1] = True

for i in range(4):
    for j in range(13):
        if not cards[i][j]:
            print(pattern[i], j+1)
