__author__ = 'alexmcneill'
import uk_phone_number
import uk_postal_address


class UKContactFactory():

    def create_postal_address(self):
        return uk_postal_address.UkPostalAddress()

    def create_phone_number(self):
        return uk_phone_number.UkPhoneNumber()