__author__ = 'alexmcneill'


class CalorieMeter():

    def __init__(self, subject):
        self.subject = subject
        subject.add_observer(self)
        self.calories = 0

    def update(self, rpms):
        self.calories = rpms * 2