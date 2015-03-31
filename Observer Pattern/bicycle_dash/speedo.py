__author__ = 'alexmcneill'


class Speedometer:

    wheelCircumference = 205

    def __init__(self, subject):
        self.subject = subject
        self.subject.add_observer(self)
        self.speed = 0

    def update(self, rpms):
        rev_per_hour = rpms * 60
        meter_per_hour = rev_per_hour * self.wheelCircumference
        self.speed = meter_per_hour / 1000