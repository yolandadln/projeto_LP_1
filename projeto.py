import numpy as np
from random import random


class Pessoa:
    def __init__(self, parametros):
        self.parametros = parametros


''' 
parametros é uma lista com os atributos do individuo: 
elemento_1 = sexo 
elemento_2 = cor 
elemento_3 = salario 
elemento_4 = rede de ensino 
elemento_5 = modalidade de ensino 
'''


class Populacao:
    def __init__(self, N=1000, n=200):
        self.pop = N
        self.amostra = n
        self.pessoas = []

        for i in range(0, N):

        random.random()

    def amostra(self, n):
        np.random.choice(self.pessoas, n)