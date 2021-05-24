class Month:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.days = []

    def number_of_days(self, days):
        self.days.append(days)
