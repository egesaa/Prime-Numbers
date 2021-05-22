class prime:
    def __init__(self, num):
        self.number = num
        self.dividers = range(2, self.number)
        self.remainder = []

    def is_prime(self):
        for element in self.dividers:
            self.remainder.append(self.number % element)

        if 0 in self.remainder:
            print(f'{self.number} is not prime')
        else:
            print(f'{self.number} is prime')

num = int(input('Enter your number: '))
prime(num).is_prime()
