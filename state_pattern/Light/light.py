__author__ = 'alexmcneill'
import light_on
import light_off


class Light:

    def __init__(self):
        self.light_state = light_off.LightOff()

    def display(self):
        return self.light_state.display()

    def switch(self):
        self.light_state = self.light_state.switch()