__author__ = 'alexmcneill'


class Speedometer():

    WHEEL_CIRCUMFERENCE = 200

    def __init__(self, subject):
        self.subject = subject
        subject.add_observer(self)
        self.speed = 0

    def update(self, rpms):
        self.speed = rpms * self.WHEEL_CIRCUMFERENCE