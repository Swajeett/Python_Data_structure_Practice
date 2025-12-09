# 2. Write an iterator that returns only even numbers up to a given number N.

class EvenIterator:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.num = 2
        return self
    def __next__(self):
        if self.num <= self.n:
            val = self.num
            self.num += 2
            return val
        else:
            raise StopIteration
        
for i in EvenIterator(10):
    print(i)


