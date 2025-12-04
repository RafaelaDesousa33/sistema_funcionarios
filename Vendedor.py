from Funcionario import Funcionario
from Gerente import Gerente

class Vendedor(Funcionario):
    def __init__(self,nome,cpf,salario):
        super().__init__(nome,cpf,salario)

    def calcular_bonus(self,percentual_comissao):
        bonus = self.salario * (percentual_comissao / 100)
        return self.salario + bonus
    