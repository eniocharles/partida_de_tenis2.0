from jogador import jogador
from partida import partida
from pontuacao import pontuacao

# Criando instâncias das classes
jogador1 = jogador()
jogador2 = jogador()
partida1 = partida()
pontuacao1 = pontuacao()

# Registrar jogadores
print(jogador1.registrarJogador())
print(jogador2.registrarJogador())

# Consultar jogadores
print(jogador1.consultarJogadores())

# Agendar uma partida
partida1.agendarPartida("2023-10-20", "15:00", "Quadra 1", jogador1, jogador2)

# Apresentar o placar
print(partida1.apresentarPlacar())
print(pontuacao1.getPontosJogadorA())
print(pontuacao1.getPontosJogadorB())

# Registrar pontuação
print(pontuacao1.registrarPontuacao(5, 'A'))
print(pontuacao1.registrarPontuacao(3, 'B'))

# Apresentar o placar novamente
print(partida1.apresentarPlacar())
print(pontuacao1.getPontosJogadorA())
print(pontuacao1.getPontosJogadorB())

# Penalizar pontuação
print(pontuacao1.penalizarPontuacao(2, 'A'))

# Apresentar o placar mais uma vez
print(partida1.apresentarPlacar())
