class Member:

    def __init__(self):
        self.member = {}

    def make_member(self):
        self.member[1] = {'First name': '', 'Last name': '', 'Relationship': ''}

class Mother(Member):

    def __init__(self):
        super().__init__()
        self.make_member()

    def make_member(self):
        self.member[1] = {'First name': 'Wendy', 'Last name': 'Willett', 'Relationship': 'Mother:'}


class Brother(Member):

    def __init__(self):
        super().__init__()
        self.make_member()

    def make_member(self):
        self.member[2] = {'First name': 'David', 'Last name': 'Dunlap', 'Relationship': 'Brother:'}


class Sister(Member):

    def __init__(self):
        super().__init__()
        self.make_member()

    def make_member(self):
        self.member[3] = {'First name': 'Myranda', 'Last name': 'Ealey', 'Relationship': 'Sister:'}


class Son(Member):

    def __init__(self):
        super().__init__()
        self.make_member()

    def make_member(self):
        self.member[4] = {'First name': 'jaxen', 'Last name': 'Willett', 'Relationship': 'Son:'}


class Daughter(Member):

    def __init__(self):
        super().__init__()
        self.make_member()

    def make_member(self):
        self.member[5] = {'First name': 'Laici', 'Last name': 'Willett', 'Relationship': 'Daughter:'}