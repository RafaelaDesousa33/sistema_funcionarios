Sistema de Funcionários — Python (POO)

Este projeto foi desenvolvido com o objetivo de praticar Programação Orientada a Objetos (POO) em Python, criando um sistema simples, mas bem estruturado, para gerenciamento de funcionários de uma empresa.
O foco foi trabalhar herança, encapsulamento e polimorfismo, além de organização de código e boas práticas.

🚀 Objetivo do Projeto

Criar um sistema que permita cadastrar diferentes tipos de funcionários, exibindo seus dados e calculando salários com bônus específicos para cada categoria.

No sistema, temos três tipos de colaboradores:

Funcionário (classe base)

Gerente

Vendedor

Cada classe possui características próprias e comportamento individualizado no cálculo de bônus.

🧠 Conceitos de POO aplicados
✔️ Herança

As classes Gerente e Vendedor herdam da classe base Funcionario, reaproveitando código e permitindo especializações.

✔️ Encapsulamento

Os atributos são privados (__nome, __cpf, __salario), garantindo segurança e controle no acesso aos dados.

✔️ Polimorfismo

Cada tipo de funcionário implementa seu próprio método calcular_bonus, permitindo comportamentos diferentes dependendo do cargo.

✔️ Organização Modular

As classes foram separadas em arquivos distintos dentro da pasta models/, deixando o projeto mais limpo e fácil de manter.

📂 Estrutura do Projeto
sistema_funcionarios/
│
├── models/
│   ├── Funcionario.py
│   ├── Gerente.py
│   ├── Vendedor.py
│
└── app.py

🔧 Como funciona cada classe
🧑‍💼 Classe Funcionario

Possui nome, CPF e salário.

Serve como base para outras classes.

👨‍💼 Classe Gerente

Herda de Funcionario.

Possui método calcular_bonus que soma um valor fixo ao salário.

🧑‍🔧 Classe Vendedor

Herda de Funcionario.

Seu bônus é calculado por percentual de comissão.

▶️ Exemplo de uso
from Funcionario import Funcionario
from Gerente import Gerente
from Vendedor import Vendedor

funcionario1 = Funcionario("Marcos", "12348372811", 2000)
gerente1 = Gerente("Marcio", "281726152345", 3000)
vendedor1 = Vendedor("Ana", "283726392345", 2000)

print(vendedor1.calcular_bonus(10))  # 10% de comissão

🎯 O que aprendi desenvolvendo este projeto

Como estruturar um sistema orientado a objetos de forma clara e escalável.

Diferenças práticas entre herança e polimorfismo.

Importância do encapsulamento para proteger dados sensíveis.

Boas práticas de modularização e separação de responsabilidades.

Como escrever código mais limpo, reaproveitável e fácil de entender.

🛠️ Tecnologias Utilizadas

Python 3

Paradigma de Programação Orientada a Objetos

VS Code

📌 Próximos Passos

Quero evoluir o projeto futuramente adicionando:

Persistência em arquivos ou banco de dados

Menu interativo

Cadastro de múltiplos funcionários

Relatórios automáticos

Interface gráfica simples

💬 Feedback ou sugestões?

Fique à vontade para abrir uma issue ou entrar em contato!
Estou sempre aberta a aprimorar minhas habilidades e aprender novas ideias do mercado. 😊
