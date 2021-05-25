class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def contains_data(self, data):
        if self.data == data:
            return True
        else:
            return False