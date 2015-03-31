__author__ = 'alexmcneill'


class UsPhoneNumber():

    def __init__(self, area_code, prefix, number):
        self.area_code = area_code
        self.prefix = prefix
        self.number = number

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, new_area_code):
        if len(new_area_code) != 3:
            raise ValueError
        else:
            self._area_code = new_area_code

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, new_prefix):
        if len(new_prefix) != 3:
            raise ValueError
        else:
            self._prefix = new_prefix

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number):
        if len(new_number) != 4:
            raise ValueError
        else:
            self._number = new_number

    def get_phone_number_string(self):
        return self.area_code + "-" + self.prefix + "-" + self.number

    def __str__(self):
        return self.get_phone_number_string()