__author__ = 'alexmcneill'


def fib_closure():
    sequence = [1, 1]

    def get_fib(n):
        try:
            value = sequence[n]
            return value
        except IndexError:
            value = get_fib(n-2) + get_fib(n-1)
            sequence.append(value)
            return sequence[n]

    return get_fib

fib_method = fib_closure()

print(fib_method(9))

print(fib_method(9))