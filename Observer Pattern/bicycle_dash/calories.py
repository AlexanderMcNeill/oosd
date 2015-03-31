__author__ = 'alexmcneill'


class CalorieMeter:

    def __init__(self, subject):
        self.subject = subject
        self.subject.add_observer(self)
        self.calories = 0

    def update(self, rpms):
        self.calories = rpms * 100