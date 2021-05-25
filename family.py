from member import Mother
from member import Sister
from member import Brother
from member import Son
from member import Daughter


class Family:

    def __init__(self):
        self.family = []
        self.add_family()

    def show_family(self):
        print("Chris Willett's family is:")
        print(' ')
        print(self.family[0][1]['Relationship'], self.family[0][1]['First name'], self.family[0][1]['Last name'])
        print(self.family[1][2]['Relationship'], self.family[1][2]['First name'], self.family[1][2]['Last name'])
        print(self.family[2][3]['Relationship'], self.family[2][3]['First name'], self.family[2][3]['Last name'])
        print(self.family[3][4]['Relationship'], self.family[3][4]['First name'], self.family[3][4]['Last name'])
        print(self.family[4][5]['Relationship'], self.family[4][5]['First name'], self.family[4][5]['Last name'])

    def add_family(self):
        mother = Mother()
        self.family.append(mother.member)
        brother = Brother()
        self.family.append(brother.member)
        sister = Sister()
        self.family.append(sister.member)
        son = Son()
        self.family.append(son.member)
        daughter = Daughter()
        self.family.append(daughter.member)

