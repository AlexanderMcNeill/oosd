__author__ = 'alexmcneill'


class Bicycle:

    def __init__(self):
        self.observers = []
        self.rpms = 0

    @property
    def rpms(self):
        return self._rpms

    @rpms.setter
    def rpms(self, new_value):
        self._rpms = new_value
        self.update_observers()

    def update_observers(self):
        for o in self.observers:
            o.update(self.rpms)

    def add_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)