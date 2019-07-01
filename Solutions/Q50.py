# Define a class named American and its subclass NewYorker.


class American(object):
    @staticmethod
    def printNationality():
        print('American')


class NewYorker(American):
    pass


american = American()
ny_er = NewYorker()

american.printNationality()
ny_er.printNationality()
