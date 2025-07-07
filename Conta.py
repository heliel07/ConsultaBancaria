class Conta:

    '''Constructor'''
    def __init__(self, titular, numero):
        self._titular = titular
        self._numero = numero
        self._saldo = 0.0

    '''Getters and Setters'''
    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def get_saldo(self):
        return self._saldo

    '''Property'''
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print("O saldo deve ser positivo")
        else:
            self._saldo = saldo


    '''Method Consult'''
    def consultarSaldo(self):
        print("Saldo: ", self._saldo)

    '''Method Deposit'''
    def depositar(self):
        valor = float(input("Digite o valor do deposito: "))
        self._saldo += valor
        print("Valor de", valor, "reais depositado com sucesso.\nNovo Saldo:", self._saldo)

    '''Method Withdraw'''
    def sacar(self):
        valor = float(input("Digite o valor para sacar: "))
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Valor de ",valor," reais sacado com sucesso.\nNovo saldo: ", self._saldo)
        else:
            print("Saldo insuficiente ou valor inválido.")