"""numero = int(input('digite um numero: '))
if numero % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')"""

"""# teste de calculadora

print('Calculadora')
print('1.Soma','2.Subtração','3.Multiplicação','4.Divisão','0.Sair',sep='\n')

opção = int(input('Escolha uma opção: '))
print('Opção escolhida: ',opção)

# função de verificação de opção escolhida
if opção == 0:
    print('Saindo...')
    exit()
elif opção == 1:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print('A soma é: ',num1 + num2)
elif opção == 2:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print('A subtração é: ',num1 - num2)
elif opção == 3:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print('A multiplicação é: ',num1 * num2)
elif opção == 4:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print('A divisão é: ',num1 / num2)
else:
    print('Opção inválida!')
"""


"""nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média do aluno é: {media}')
"""


"""# Lista de numeros
numeros = []

for i in range(10):
    numeros.append(int(input(f'Digite o {i+1}º numero: ')))

    print('Maior numero: ', max(numeros))
    print('Menor numero: ', min(numeros))
    print('Media dos numeros: ', sum(numeros) / len(numeros))
    print('Impares:', [num for num in numeros if num % 2!= 0])
    print('Pares: ', [num for num in numeros if num % 2 == 0])
"""

"""# teste de palindromo
palavra = input('Digite uma palavra: ')
palavra = palavra.lower().replace(' ', '')
if palavra == palavra[::-1]:
    print(f'A palavra {palavra} é um palíndromo')
else:
    print(f'A palavra {palavra} não é um palíndromo')
"""

"""# contador de palavras e caracteres
frase = input('Digite uma frase: ')
palavras = frase.split()
print(f'A frase tem {len(palavras)} palavras')
print(f'A frase tem {len(frase)} caracteres')
"""

"""# sistema de login
usuario = "admin"
senha = 1234

for tenativas in range(3):
    login_usuario = input('Digite o usuario: ')
    login_senha = int(input('Digite a senha: '))
    if login_usuario == usuario and login_senha == senha: 
        print('login realizado com sucesso!')
        break
    else: 
        print('usuario ou senha incorretos!')
else:
    print('Limite de tentativas atingido!')
"""

'''# listas, dicionarios e funções
pessoas = []

# Função criada para cadastrar uma pessoa
def cadastrar_pessoa():
    
    # Dicionario com dados da pessoa
    pessoa = {
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "cidade": input("Cidade: "),
    }

    # Adiciona o Dicionario na lista de pessoas
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

# Função criada para listar todas as pessoas cadastradas
def listar():
    
    # Percorre cada pessoa dentro da lista
    for pessoa in pessoas:
        print(pessoa)

# Função responsável por pesquisar uma pessoa pelo nome
def pesquisar():
    
    # Solicita o nome da pessoa a ser pesquisada
    nome = input("Nome: ")
    
    # Percorre a lista de pessoas e verifica se o nome informado existe
    for pessoa in pessoas:
        # Verifica se o nome da pessoa é igual ao nome informado
        if pessoa["nome"] == nome:
            print(pessoa)
            break

# Função responsável por remover uma pessoa pelo nome
def remover():
    # Solicita o nome da pessoa a ser removida
    nome = input("Nome: ")
    #percorre a lista de pessoas e verifica se o nome informado existe
    for pessoa in pessoas:
        #Verifica se o nome existe na lista de pessoas e depois remove a pessoa da lista
        if pessoa["nome"] == nome:
            pessoas.remove(pessoa)

# Loop principal do programa
# Executa o menu de opções até que o usuário escolha a opção de sair
while True:
    # Exibe o menu de opções para o usuário
    print("\n1-Cadastrar \n2-Listar \n3-Pesquisar \n4-Remover \n0-Sair")
    # Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        pesquisar()
    elif opcao == "4":
        remover()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
'''