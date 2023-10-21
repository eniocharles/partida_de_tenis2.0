from partida import partida

class pontuacao():
    def __init__(self):
        self.__pontosJogadorA = 0
        self.__pontosJogadorB = 0
        self.__partida = partida
        
    def registrarPontuacao (self, p, j):
        if j == 'A':
            self.__pontosJogadorA += p
            return f'{p} ponto(s) adicionado(s) ao jogador A'
        
        else:
            self.__pontosJogadorB += p
            return f'{p} ponto(s) adicionado(s) ao jogador B'
            
    def penalizarPontuacao (self, p, j):
        if j == 'A':
            self.__pontosJogadorA -= p
            return f'{p} ponto(s) retirado(s) do jogador A'
        
        else:
            self.__pontosJogadorB -= p
            return f'{p} ponto(s) retirado(s) do jogador B'
        
    def getPontosJogadorA(self):
        return f'Pontos jogador A: {self.__pontosJogadorA}'
    
    def getPontosJogadorB(self):
        return f'Pontos jogador B: {self.__pontosJogadorB}'