class A:
    def __init__(self):
        self.calcI(30)
        print('i da Classe A', self.i)

    def calcI(self, i):
        self.I = 2 * i;

class B(A):
    def __init__(self):
        super().__init__()

    def calcI(self, i):
        self.i = 3 * i;

b = B()