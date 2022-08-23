class Dice:
    def __init__(self, num):
        self.num_a = num[0]
        self.num_b = num[1]
        self.num_c = num[2]
        self.num_d = num[3]
        self.num_e = num[4]
        self.num_f = num[5]

    def E(self):
        self.num_a, self.num_c, self.num_f, self.num_d = \
            self.num_d, self.num_a, self.num_c, self.num_f

    def W(self):
        self.num_a, self.num_c, self.num_f, self.num_d = \
            self.num_c, self.num_f, self.num_d, self.num_a

    def S(self):
        self.num_a, self.num_b, self.num_f, self.num_e = \
            self.num_e, self.num_a, self.num_b, self.num_f

    def N(self):
        self.num_a, self.num_b, self.num_f, self.num_e = \
            self.num_b, self.num_f, self.num_e, self.num_a

num = list(map(int, input().split()))
str = input()
dice = Dice(num)
for i in str:
    if i == "E":
                dice.E()
    elif i == "W":
        dice.W()
    elif i == "S":
        dice.S()
    elif i == "N":
        dice.N()
print(dice.num_a)
