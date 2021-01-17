"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        self.start = start-1
        self.ssn = self.start
    def generate(self):
        self.ssn += 1
        return self.ssn
    def reset(self):
        self.ssn = self.start 


# ssn = SerialGenerator(100)
# for ea in range(10):
#     print(ssn.generate())




