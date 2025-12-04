"""
Docstring for models.Funcionario
Conceitos: herança
Classes:

Funcionario (base)

Gerente (herda funcionário, ganha bônus maior)

Vendedor (com comissão)

Polimorfismo para calcular salário final.
"""
class Funcionario:
    def __init__(self,nome,cpf,salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def __str__(self):
        return f"nome:{self.__nome}, cpf:{self.__cpf}, salario:{self.__salario}"
    
    #metodos getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def salario(self):
        return self.__salario
    
    #metodos setters
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
       
    @cpf.setter
    def cpf(self,novo_cpf):
        if len(novo_cpf) == 11 and novo_cpf.isdigit() :
            self.__cpf = novo_cpf
        else:
            print(f"CPF precisa ter 11 digitos")

    @salario.setter
    def salario(self,novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
        else:
            print("Erro: salario negativo")

    
    def exibirDados(self):
        print(f"Nome do funcionario:{self.nome}")
        print(f"CPF:{self.cpf}")
        print(f"Salario:{self.salario}")

    

        
    
