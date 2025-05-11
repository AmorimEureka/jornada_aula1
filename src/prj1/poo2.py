
class Carro:

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

        print(f"Marca: {self.marca}, Modelo: {self.modelo} e a cor: {self.cor}...Velocidade Atual {self.velocidade} Km/h")


lista_carros = []

while True:

    print("\n ----- MENU ----- \n")

    print("1 - Adicionar novo carro")
    print("2 - Exibir dados dos carros")
    print("3 - Acelerar um carro")
    print("4 - Frear um carro")
    print("5 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":

        marca = input("Digite a marca do carro: ")
        modelo = input("Digite a marca do modelo: ")
        cor = input("Digite a marca do cor: ")

        novo_carro = Carro(marca, modelo, cor)

        lista_carros.append(novo_carro)

    elif opcao == "2":

        if lista_carros:
            for carro in lista_carros:
                carro.dados_carro()

        else:
            print("Nenhum carro foi adicionado ainda")

    elif opcao == "3":

        modelo_select = input("Digite o Modelo: ")

        for carro in lista_carros:
            if carro.modelo == modelo_select:
                carro.acelerar()
                break
            else:
                print("Modelo não cadastrado")

    elif opcao == "4":
        modelo_select == input("Digite o Modelo: ")

        for carro in lista_carros:
            if carro.modelo == modelo_select:
                carro.frear()
                break
            else:
                print("Modelo não cadastrado!")

    elif opcao == "5":

        print("Saindo do menu")

        break
