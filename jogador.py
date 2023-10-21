from datetime import datetime

class jogador:
    def __init__(self):
        self.__nome = ""
        self.__endereco = ""
        self.__telefone = 0
        self.__dataNascimento = datetime.date
        self.__nivelHabilidade = ""
        self.__derrotas = 0
        self.__vitorias = 0
        
        self.__jogador = []
    
    def registrarJogador(self):
        
        nome = input('Digite o nome: ')
        endereco = input('Digite o endereco: ')
        tel = input('Digite o telefone: ')
        dataNascimento = input('Digite o data de nascimento (dd/mm/yyyy): ')
        nivelHabilidade = input('Digite o nivel de habilidade: ')
        
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = tel
        
        date = datetime.strptime(dataNascimento, '%d/%m/%Y').date()
        self.__dataNascimento = date
        
        self.__nivelHabilidade = nivelHabilidade
        self.__derrotas = 0
        self.__vitorias = 0

        self.__jogador.append([nome,endereco,tel,dataNascimento,nivelHabilidade,nivelHabilidade,self.__derrotas,self.__vitorias])
        
        '''!Logica!'''
        
        return f"Jogador {self.__nome} registrado!"
    
    def consultarJogador (self, n):
        for i in self.__jogador:

            if n in i:
                return f'Jogador {n} encontrado!'
            else:
                return f'Jogador {n} não existe!'
            
    def consultarJogadores(self):
        list = []
        for i in self.__jogador:
            list.append(i[0])
        return list
    
    def removerJogador(self, n):
        for i in self.__jogador:

            if n in i:
                self.__jogador.pop(i)
                return f'Jogador {n} excluido!'
        return f'Jogador {n} não encontrado!'  