__author__ = 'alexmcneill'
import us_phone_number
import us_postal_address


class USContactFactory():

    def create_postal_address(self):
        us_postal_address.UsPostalAddress()

    def create_phone_number(self):
        us_phone_number.UsPhoneNumber()