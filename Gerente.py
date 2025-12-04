from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self,nome,cpf,salario):
        super().__init__(nome,cpf,salario)

    def calcular_bonus(self,valor_bonus):
        return self.salario + valor_bonus
    


