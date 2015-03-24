__author__ = 'alexmcneill'


class UkPostalAddress():

    def __init__(self, recipient, org, building_name, address_line, locality, city, post_code):
        self.recipient = recipient
        self.org = org
        self.building_name = building_name
        self.address_line = address_line
        self.locality = locality
        self.city = city
        self.post_code = post_code

    @property
    def post_code(self):
        return self.post_code

    @post_code.setter
    def post_code(self, post_code):
        if len(self.post_code) != 7:
            raise ValueError