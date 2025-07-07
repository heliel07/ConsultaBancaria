from Conta import Conta

'''Method Data Client'''
def inputData():
    numero = int(input("Digite o numero da conta: "))
    nome = str(input("Digite o nome do cliente: "))
    saldo = 0

    contaData = Conta(nome, numero)
    return contaData

'''Method Switch Case Operation'''
def realizarOperacoes(conta):
    while True:
        opcao = input("\nOperação Bancária:\n0 - Consultar saldo\n1 - Depositar\n2 - Sacar\n3 - Sair\nDigite a opção: ")

        if opcao == "0":
            conta.consultarSaldo()
        elif opcao == "1":
            conta.depositar()
        elif opcao == "2":
            conta.sacar()
        elif opcao == "3":
            print("Encerrando...\nOperação encerrada.")
            break
        else:
            print("Opção inválida. Tente novamente.")

'''Method Call'''
contaDoCliente  = inputData()
realizarOperacoes(contaDoCliente)