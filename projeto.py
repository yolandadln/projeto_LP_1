import numpy as np


class Pessoa:
    def __init__(self):
        self.sexo = None
        self.cor = None
        self.rede = None
        self.modalidade = None
        self.ocupacao = None

    def pessoa(self):
        pass


class Populacao:
    def __init__(self, N=1000, n=200):
        self.pop = N
        self.amostra = n
        self.pessoas = []

        for i in range(0, N):
            random.random()

    def amostra(self, n):
        np.random.choice(self.pessoas, n)