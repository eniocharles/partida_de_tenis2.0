from datetime import datetime
from jogador import jogador

class partida():
    def __init__(self):
        self.__data = datetime.date
        self.__hora = datetime.time
        self.__quadra = ""
        self.__jogador1 = jogador
        self.__jogador2 = jogador
    
    def agendarPartida (self, d, h, q, j1, j2):
        self.__data = d
        self.__hora = h
        self.__quadra = q
        self.__jogador1 = j1
        self.__jogador2 = j2
        
    def apresentarPlacar (self):
        return f'O placar atual é: \n'  
    
    