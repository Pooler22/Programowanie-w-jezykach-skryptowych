class Chess:
    def __init__(self):
        self.list1 = []
        self.litery = "abcdefgh"
        self.liczby = "12345678"

    @staticmethod
    def correct(i):
        return 8 > i >= 0

    def check(self, i, j, stan_litera, stan_cyfra):
        if self.correct(stan_litera) and self.correct(stan_cyfra):
            self.list1.append(str(self.litery[stan_litera]) + str(self.liczby[stan_cyfra]))
            self.check(i, j, stan_litera + i, stan_cyfra + j)

    def chess(self, parm1):
        for i in [1, -1]:
            for j in [1, -1]:
                self.check(i, j, self.litery.index(parm1[0]), self.liczby.index(parm1[1]))
        return [x for x in self.list1 if x != parm1]


print(Chess().chess("d4"))
