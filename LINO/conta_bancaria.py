from pessoa import Pessoa

class ContaBancaria:
    def __init__(self, agencia, tipo_conta, numero_conta, saldo, titular: Pessoa):
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular
        
    def exibir_saldo(self):
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        
    def exibir_dados_conta(self):
        print(f' === Dados da Conta ===')
        print(f'Agência: {self.agencia}')
        print(f'Número da Conta: {self.numero_conta}')
        print(f'Tipo de Conta: {self.tipo_conta}')
        print(f'Saldo: {self.saldo:.2f}')
        print(f'Titular: {self.titular.nome}')
        
