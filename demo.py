

class TopTen:

    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
        print(i)

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))

for i in values:
    pass
