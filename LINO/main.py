from pessoa import Pessoa
from conta_bancaria import ContaBancaria

pessoa = Pessoa(
    'Felipe Lino',
    '123.456.789.10',
    'felipelino2007.fl@gmail.com',
    '(81) 98771-4812'
)
    
conta1 = ContaBancaria(
    '1324',
    'Corrente',
    '67880-9',
    400000,
    pessoa
)
    
conta1.exibir_dados_conta()
conta1.exibir_saldo()
conta1.exibir_dados_pessoais()
