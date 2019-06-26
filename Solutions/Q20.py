class Generator:
    def __init__(self):
        pass

    def iterateNumbers(self, n):
        generator = (x for x in range(n + 1) if not x % 7)

        for i in generator:
            yield i


generator = Generator()
for i in generator.iterateNumbers(100):
    print(i)
