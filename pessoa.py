class Pessoa:
    def __init__(self,nome=None,idade=35):
            self.nome=nome
            self.idade=idade
    def cumprimentar(self):
        return 'ola'
if __name__ == '__main__':
    p= Pessoa('dario')
    print(Pessoa.cumprimentar(p))
    print(p.nome)
    p.nome='dario nzita'
    print(p.nome)
    print(p.idade)
    o=Pessoa('paulo',13)
    print(o.idade)