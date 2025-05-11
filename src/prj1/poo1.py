

class carro:

    def __init__(self, marca, modelo, cor):

        """Metódo contrutor que é chamado ao instanciar
           um objeto """

        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):

        """Metódo que incrementa a velocidade em 10 km/h"""

        self.velocidade += 10

        print(f"Velocidade atual é: {self.velocidade} Km/h")


    def frear(self):

        """Metódo para frear o carro"""

        if self.velocidade > 0:
            self.velocidade -= 15

            print(f"Velocidade atual é : {self.velocidade} Km/h")

        else:
            print(f"Carro {self.modelo}, {self.cor} da marcar {self.marca} não está em movimento!")


    def dados_carro(self):

        """Metódo para retornar dados do carro"""

        print(f"Marca: {self.marca}, Modelo: {self.modelo} e a cor: {self.cor}")



carro1 = carro("Fiat", "Uno Vivave", "Branco")
carro2 = carro("Hilux", "Hilux", "Vermelho")

print("\n")
carro1.dados_carro()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()
carro1.acelerar()
carro1.acelerar()
carro1.frear()

print(" \n ---------------------------------- \n")

carro2.dados_carro()
carro2.acelerar()
carro2.acelerar()
carro2.frear()
carro2.acelerar()
carro2.frear()
carro2.frear()