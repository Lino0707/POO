class Pessoa:
    def __init__(self, nome, cpf, email, telefone):
        self.nome =nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        
    def exibir_dados_pessoais(self):
        print(" === Dados Pessoais ===")
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Email: {self.email}')
        print(f'Telefone: {self.telefone}')
        
    
