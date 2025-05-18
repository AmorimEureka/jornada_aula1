vendas = [('rodrigo', 123),('tobias', 546), ('pixolia', 666), ('panda', 543), ('tobias', 111), ('pixolia', 666)]
print(vendas)


dicionario = {}
for item_lista in vendas:
    chave, valor = item_lista
    print(chave)
    print(valor)

    if chave in dicionario:
        dicionario[chave] += valor
    else:
        dicionario[chave] = valor

print(dicionario)






# import os

# notes = []
# sair = False

# while not sair:
#     resp = input('Fazer anotação? (s/n)')
#     if resp == "s":
#         text = input("Anotação: ")
#         notes.append(text)

#     print('\n'+"Anotações".center(30, "="))

#     for note in notes:
#         text_size = len(note)
#         note_size = text_size+6
#         print('-'*note_size)
#         print(note.center(note_size))
#         print('-'*note_size)

#     r = input("sair? (s/n)")

#     if r == "s":
#         sair = True

#     os.system('cls' if os.name == 'nt' else 'clear')





# class ErroDeLogin(Exception):

#     def __init__(self, usuario, descricao):
#         super().__init__(usuario, descricao)

#         self.usuario = usuario
#         self.descricao = descricao

#     def __str__(self):
#         return f"❌ - O usuário fonecido: '{self.usuario}' não existe! \n⚠️ Motivo do error: {self.descricao} "


# def logar(usuario, senha):

#     if usuario != "admin" or senha != '1234':
#         raise ErroDeLogin(usuario, "Login ou Senha incorretos")
#     print(f"Seja bem-vindo Sr. {usuario} !")


# try:
#     login = input("Digite seu usuário: ")
#     senha = input("DDigite sua senha: ")

#     resultado = logar(login, senha)
# except ErroDeLogin as e:
#     print(f"\n ============= ENTRADA INVALIDA =============  \n{e} \n============================================\n")
#     print(f"Imprimindo a tupla '.args': {e.args}\n")
#     u, d = e.args
#     print(f"{u=} e {d=} \n")






# while True:
#     try:
#         x = int(input("Foneça um número válido: "))
#         print(f"O número {x=} fornecido")
#         break
#     except ValueError:
#         print("Você não está fornecendo um dígito!")
#     except KeyboardInterrupt:
#         print("O programa foi incerrado por você!!")
#         break
