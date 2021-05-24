from month import Month


class Year:

    def __init__(self, year):
        self.year = year
        self.months = ()
        self.make_month()

    def find_pie(self):
        l1 = list(self.months)
        i = 0
        while i < len(l1):
            if l1[i].number == 3:
                print(f'{l1[i].name} has Pie!')
                self.months = tuple(l1)
            else:
                self.months = tuple(l1)
            i = i+1

    def make_month(self):
        l1 = list(self.months)
        jan = Month('January', 1)
        jan.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        l1.append(jan)
        feb = Month('February', 2)
        feb.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
        l1.append(feb)
        mar = Month('March', 3)
        mar.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        l1.append(mar)
        apr = Month('April', 4)
        apr.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        l1.append(apr)
        may = Month('May', 5)
        may.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        l1.append(may)
        jun = Month('June', 6)
        jun.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        l1.append(jun)
        jul = Month('July', 7)
        jul.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        l1.append(jul)
        aug = Month('August', 8)
        aug.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        l1.append(aug)
        sep = Month('September', 9)
        sep.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        l1.append(sep)
        octo = Month('October', 10)
        octo.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        l1.append(octo)
        nov = Month('November', 11)
        nov.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        l1.append(nov)
        dec = Month('December', 12)
        dec.number_of_days(['Days', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        l1.append(dec)
        self.months = tuple(l1)
