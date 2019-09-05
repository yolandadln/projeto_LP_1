import numpy as np


class Pessoa:
    def __init__(self):
        self.sexo       = None
        self.cor        = None
        self.rede       = None
        self.modalidade = None
        self.ocupacao   = None

    def pessoa(self):
        pass

class Populacao:
    def __init__(self, N=1000):
        self.pop = N
        self.pessoas = []

        for i in range(0, N):
            p = Pessoa()
            p.pessoa()
            self.pessoas.append(p)

    def amostra(self, n = 100):
        np.random.choice(self.pessoas, n)
