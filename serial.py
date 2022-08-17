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

    def __init__(self, start=0):
        '''Make a generator, starting at 0'''

        self.start = self.next = start

    def __repr__(self):
        '''Translates to text'''

        return f"<Serial Generator start = {self.start} next = {self.next}>"

    def generate(self):
        '''Returns the next serial number'''

        self.next += 1
        return self.next - 1
    
    def reset(self):
        '''Resets serial to starting number'''

        self.next = self.start