class Dice:
    def __init__(self, num):
        self.num_a = num[0]
        self.num_b = num[1]
        self.num_c = num[2]
        self.num_d = num[3]
        self.num_e = num[4]
        self.num_f = num[5]

    def top(self):
        print(self.num_a)

    def E(self, r):
        if r == "E":
            self.num_a, self.num_c, self.num_f, self.num_d = \
                self.num_d, self.num_a, self.num_c, self.num_f

    def W(self, r):
        if r == "W":
            self.num_a, self.num_c, self.num_f, self.num_d = \
                self.num_c, self.num_f, self.num_d, self.num_a

    def S(self, r):
        if r == "S":
            self.num_a, self.num_b, self.num_f, self.num_e = \
                self.num_e, self.num_a, self.num_b, self.num_f

    def N(self, r):
        if r == "N":
            self.num_a, self.num_b, self.num_f, self.num_e = \
                self.num_b, self.num_f, self.num_e, self.num_a

    def state(self):
        return ([self.num_a, self.num_b, self.num_c, self.num_d,
                self.num_e, self.num_f])

    def right(self, a, b):
        d = self
        directions = " EEENEEENEEESEEESEEENEEEN"
        for i in directions:
            d.E(i) or d.W(i) or d.S(i) or d.N(i)
            st = d.state()
            if a == st[0] and b == st[1]:
                return st[2]

    def compare(self, d1):
        st1 = self.state()
        directions = " EEENEEENEEESEEESEEENEEEN "
        for i in directions:
            d1.E(i) or d1.W(i) or d1.S(i) or d1.N(i)
            st2 = d1.state()
            if st2 == st1:
                return True
        return False

n = int(input())
L = []
for i in range(n):
    nums = list(map(int, input().split()))
    dice = Dice(nums)
    for d in L:
        if dice.compare(d):
            break
    else:
        L.append(dice)
        continue
    print("No")
    break
else:
    print("Yes")
