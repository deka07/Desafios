def menu():
    x = 0
    while True:
        print('=======================================')
        print('Agenda Telefonia'.center(40))
        print('=======================================')
        print(' 1 - Adicionar')
        print(' 2 - Listar')
        print(' 3 - Sair')

        opcao = int(input('Digite a opção: '))
        print('=======================================')

        if opcao == 1:
            adcionar()
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            print('Finalizar Programa!')
            break
        else:
            print('ERRO! Opção inválida!')

# Metodo para adicionar os contatos
def adcionar():
    nome = input('=> Digite o nome: ')
    tel = input('=> Digite o numero do telefone: ')

    contato = nome, tel

    lista.append(contato)
    print('')
    print('# Contato adicionado com sucesso! #')
    print('')
    print('=======================================')

# Listar os contatos
def listar(lista):
    print('Lista de contatos: ')
    print(lista)


lista = []
menu()

