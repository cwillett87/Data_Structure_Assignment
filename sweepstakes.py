import random


class Sweepstakes:

    def __init__(self):
        self.contestants = {}
        self.add_contestant()
        self.show_contestants()

    def show_contestants(self):
        print(' ')
        print('The contestants are:',
              self.contestants['Contestant 1']['First name'], self.contestants['Contestant 1']['Last name'],
              ',', self.contestants['Contestant 2']['First name'], self.contestants['Contestant 2']['Last name'],
              ',', self.contestants['Contestant 3']['First name'], self.contestants['Contestant 3']['Last name'],
              ',', self.contestants['Contestant 4']['First name'], self.contestants['Contestant 4']['Last name'],
              ',', self.contestants['Contestant 5']['First name'], self.contestants['Contestant 5']['Last name'])
        print(' ')

    def add_contestant(self):
        self.contestants['Contestant 1'] = {'First name': 'Brian', 'Last name': 'Williams!', 'Age': '21',
                                            'Saying': 'Woot Woot!'}
        self.contestants['Contestant 2'] = {'First name': 'Chris', 'Last name': 'Willett!', 'Age': '34',
                                            'Saying': 'I WIN!'}
        self.contestants['Contestant 3'] = {'First name': 'Leighton', 'Last name': 'Schmidt!', 'Age': '29',
                                            'Saying': 'Woo Hoo!'}
        self.contestants['Contestant 4'] = {'First name': 'Corey', 'Last name': 'Jordan!', 'Age': '26',
                                            'Saying': 'Yippee!'}
        self.contestants['Contestant 5'] = {'First name': 'Ricky', 'Last name': 'Bobby!', 'Age': '42',
                                            'Saying': 'If you are not first you are last!'}

    def winner(self):
        winner = random.choice(list(self.contestants))
        print("AND...")
        print('The winner is:  ', self.contestants[winner]['First name'], self.contestants[winner]['Last name'],
              self.contestants[winner]['Saying'])
