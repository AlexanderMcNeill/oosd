__author__ = 'alexmcneill'
import light_off


class LightOn():

    def switch(self):
        return light_off.LightOff()

    def display(self):
        return "Bright"