class Pessoa:
    def __init__(self, nome,idade,sexo = "F",andando = False):

        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.andando = andando


    def falar(self):
        print("Ola, boa noite. Eu sou a ", self.nome)

    def andar(self, km):
        if self.andando:
            print(self.nome,"Ela ja esta andando")
            return
        else:
             print(self.nome, "caminhou", km,"quilometros hoje")
        self.andando = True

    def parar(self):
        print("A",self.nome, "parou!")
        self.andando = False