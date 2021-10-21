class Pessoa:
    def __init__(self,nome=None,idade=35,*filhos):
        self.idade = idade
        self.nome=nome
        self.filhos=list(filhos)
        
    def cumprimentar(self):
        return 'ola'
if __name__ == '__main__':
    darion= Pessoa('dario')
    paulo=Pessoa('paulo', 13, darion)
    print(darion.nome)
    darion.nome= 'dario nzita'
    print(darion.nome)
    print(darion.idade)
    print(paulo.idade)
    for filho in paulo.filhos:
        print(filho.nome)
    paulo.sobrenome='garcia'
    del darion.filhos
    print(paulo.sobrenome)
    