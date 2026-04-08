"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
dados = {}
dados['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2026 - nascimento
dados['idade'] = idade
dados['ctps'] = int(input('Digite a Carteira de Trabalho (digite 0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salário: '))
    dados['aposentadoria'] = dados['contratacao'] - nascimento + 35

for k, v in dados.items():
    print(f'{k} tem o valor {v}')
