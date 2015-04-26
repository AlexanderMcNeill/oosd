__author__ = 'alexmcneill'
from math import sqrt


# def generate_prime(n):
#     count = 0
#
#     while count < n:
#         if count == 0:
#             yield []
#         elif count == 1:
#             yield [1]
#         else:
#             p = generate_prime(int(sqrt(n)))
#             no_p = {j for i in p for j in range(i*2, n, i)}
#             p = {x for x in range(2, n) if x not in no_p}
#             yield p
#
#  generator test
#
#
# prime_list = [prime for prime in generate_prime(10)]
#
# print(prime_list)