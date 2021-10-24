class Motor():
    def __init__(self,velocidade=0):
        self.velocidade = velocidade
    def Acelerar(self):
        self.velocidade+=1
    def Freiar(self):
        self.velocidade-=2
        self.velocidade=max(0,self.velocidade)


class Direcao():
    def __init__(self):
        self.c=0
        self.direc = ['norte', 'este', 'sul', 'oeste']
        self.valor =self.direc[0]
    def Girar_a_direita(self):
        if 0<self.c>3 :
            self.c=0
        self.c+=1
        self.valor=self.direc[self.c]
    def Girar_a_esquerda(self):
        if 0<self.c<0:
            self.c=3
        self.c-=1
        self.valor=self.direc[self.c]
class Carro(Motor,Direcao):
    pass
