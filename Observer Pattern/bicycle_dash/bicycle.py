__author__ = 'alexmcneill'


class Bicycle:

    def __init__(self):
        self.observers = []
        self.rpms = 0

    def add_observer(self, o):
        self.observers.add(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update(self.rpms)