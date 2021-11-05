class Pessoa:
    def __init__(self,nome=None,idade=35,*filhos):
        self.idade = idade
        self.nome=nome
        self.filhos=list(filhos)
        
    def cumprimentar(self):
        return 'ola'
    @staticmethod
    def estatico():
        return 42
    @classmethod
    def  nome_atributos_de_classes(cls):
        return cls.estatico()
class Homen(Pessoa):
    pass
if __name__ == '__main__':
    darion=Homen('dario')
    paulo=Homen('paulo', 13, darion)
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
    print(darion.nome_atributos_de_classes())