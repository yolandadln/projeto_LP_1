import numpy as np
from random import random

class Pessoa:
    
    def __init__(self):
        self.sexo       = None
        self.cor        = None
        self.rede       = None
        self.modalidade = None
        self.ocupacao   = None

        
    def pessoa(self):
           if random() < np.random.uniform(0.428-0.0095, 0.428+0.0095):
            self.sexo = "mulher"
        else: 
            self.sexo = "homem"
            
            
        if random() < np.random.uniform(0.421-0.012, 0.421+0.012):
            self.cor = "preta_parda"
        else: 
            self.cor = "branca"
            
            
        if random() < np.random.uniform(0.22-0.052, 0.22+0.052):
            self.rede = "publica"
        else:
            self.rede = "particular" 
            
            
        if random() < np.random.uniform(0.178-0.051, 0.178+0.051):
            self.modalidade = "distancia"
        else:
            self.modalidade = "presencial"


        if random() < np.random.uniform(0.346-0.011,0.346+0.011):
            self.ocupacao = "nao_ocupado"
        else:
            self.ocupacao = "ocupado"
            
            
            
class Populacao:
    
    def __init__(self, N=1000):
        self.pop = N
        self.pessoas = []

        for i in range(0, N):
            p = Pessoa()
            p.pessoa()
            self.pessoas.append(p)

    def amostra(self, n = 100):
        return np.random.choice(self.pessoas, n)
