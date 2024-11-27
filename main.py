# Калькулятор ипотеки


class CreditCalculator:

    def __init__(self, S: int, R: int, T: int):
        self.S = S
        self.R = R
        self.T = T

    def calc_ann_credit(self, flag=True):
        result = 0
        r = (self.R / 12) * 0.01
        A = (r * (1 + r) ** self.T) / (-1 + (1 + r) ** self.T)
        x = round(self.S * A, 2)
        result = round(x * self.T, 2)
        P = round(result - self.S, 2)
        if flag:
            print(f"""Рассчет кредита с аннуететными платежами
        Сумма кредита = {self.S} руб;    Срок кредита = {self.T} месяцев
        Годовая процентная ставка {self.R} %
        Итоговая сумма выплат = {result} руб; Ежемесячная выплата {x} руб
        Начисленные проценты = {P} руб
        """)
        return result

    def calc_diff_credit(self, flag=True):
        result = 0
        C = self.S
        r = (self.R / 12) * 0.01
        s = round(self.S / self.T, 2)
        for t in range(self.T):
            p = C * r
            x = s + p
            result += x
            C -= s
        P = result - self.S
        if flag:
            print(f"""Рассчет кредита с диффренцированными платежами
        Сумма кредита = {self.S} руб;    Срок кредита = {self.T} месяцев
        Годовая процентная ставка {self.R} %
        Итоговая сумма выплат = {result} руб;   Начисленные проценты = {P} руб
        """)
        return round(result, 2)

    def compare(self):
        A = self.calc_ann_credit(flag=False)
        D = self.calc_diff_credit(flag=False)
        print(f"""Сравнение
        Сумма выплат по аннуететным платежам: {A} руб
        Сумма выплат по диффренцированным платежам:{D} руб""")


if __name__ == '__main__':
    credit = CreditCalculator(500000, 12, 6)
    credit.calc_ann_credit()
    credit.calc_diff_credit()
    credit.compare()
