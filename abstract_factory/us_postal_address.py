__author__ = 'alexmcneill'
import re


class UsPostalAddress():

    def __init__(self, recipient="", org="", address_line_1="", address_line_2="", city="", state="", post_code=""):
        self.recipient = recipient
        self.org = org
        self.address_line_one = address_line_1
        self.address_line_two = address_line_2
        self.city = city
        self.state = state
        self.post_code = post_code

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, new_recipient):
        if len(new_recipient) < 1:
            raise ValueError
        else:
            self._recipient = new_recipient

    @property
    def address_line_one(self):
        return self._address_line_one

    @address_line_one.setter
    def address_line_one(self, new_address):
        if len(new_address) < 1:
            raise ValueError
        else:
            self._address_line_one = new_address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        if len(new_city) < 1:
            raise ValueError
        else:
            self._city = new_city


    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        if len(new_state) != 2:
            raise ValueError
        else:
            self._state = new_state

    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, new_post_code):
        if len(new_post_code) != 9:
            raise ValueError
        else:
            self._post_code = new_post_code

    def get_address_string(self):
        output = ""

        output += self.recipient

        if(len(self.org) > 0):
            output += self.org

        output += self._address_line_one

        if len(self.address_line_two) > 0:
            output += self.address_line_two

        output += self.city

        output += self.state

        output += self.post_code

        return output

    def __str__(self):
        return self.get_address_string()