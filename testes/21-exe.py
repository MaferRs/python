import datetime
from Extrato import Extrato


class Conta:
    def__init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.sata abertura = datetime.satetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.trasacoes.append(
            ["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferencia Realizada"

    def gerarsaldo(self):
        print(f"numero: {self.unmero}\n saldo:{self.saldo}")
