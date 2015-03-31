__author__ = 'alexmcneill'


class UkPostalAddress():

    def __init__(self, recipient="", org="", building_name="", address_line="", locality="", city="", post_code=""):
        self.recipient = recipient
        self.org = org
        self.building_name = building_name
        self.address_line = address_line
        self.locality = locality
        self.city = city
        self.post_code = post_code

    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, new_post_code):
        if len(new_post_code) != 7:
            raise ValueError
        else:
            self._post_code = new_post_code

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
    def address_line(self):
        return self._address_line

    @address_line.setter
    def address_line(self, new_address_line):
        if len(new_address_line) < 1:
            raise ValueError
        else:
            self._address_line = new_address_line

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        if len(new_city) < 1:
            raise ValueError
        else:
            self._city = new_city

    def get_address_string(self):
        output = ""

        output += "To: " + self.recipient

        if(len(self.org) > 0):
            output += "Organisation: " + self.org

        if(len(self.building_name) > 0):
            output += "Building: " + self.building_name

        output += "Address: " + self.address_line

        if(len(self.locality) > 0):
            output += "Locality: " + self.locality

        output += "City: " + self.city

        output += "Post Code: " + self.post_code

        return output

    def __str__(self):
        return self.get_address_string()