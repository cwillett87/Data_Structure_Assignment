class Locations:

    def __init__(self):
        self.locations = {'Va Beach, Va', 'Outer Banks, Nc', 'Myrtle Beach, Sc'}
        self.show_locations()

    def show_locations(self):
        print(self.locations)

    def future_locations(self, location):
        final = set((location, ))
        self.locations.update(final)
