from Funcionario import Funcionario
from Gerente import Gerente
from Vendedor import Vendedor

print("Funcionario comuns:")
funcionario1 = Funcionario("Marcos", "123483728111",2000)
funcionario1.exibirDados()

print("------------------------")

print("Gerentes:")
gerente1 = Gerente("Marcio", "281726152345",3000)
gerente1.exibirDados()

print("----------------------")

print("Vendedores:")
vendedor1 = Vendedor("Ana", "283726392345",2000)
vendedor1.exibirDados()

print(vendedor1.calcular_bonus(10))