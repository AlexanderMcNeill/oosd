__author__ = 'alexmcneill'


def generate_prime(n):
    count = 0

    while count < n:
        if count == 0:
            yield []
        elif count == 1:
            yield [1]
        else:
