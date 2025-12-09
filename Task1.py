# 1.create an iterator that returns numbers from 1 to 10.

class OneToTen:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
for i in OneToTen():
    print(i)
    