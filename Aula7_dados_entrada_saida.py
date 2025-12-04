# -----------------------------------------------
# TEMA: ENTRADA E SAÍDA DE DADOS EM PYTHON
# -----------------------------------------------
# Baseado no conteúdo do curso Ctrl+Play – Introdução à Informática
# -----------------------------------------------
# Em Python, usamos as funções input() e print() para interagir com o usuário.
# A função input() serve para ENTRADA de dados (receber informações do usuário)
# e a função print() serve para SAÍDA de dados (mostrar informações na tela).
# -----------------------------------------------


# ======= ENTRADA DE DADOS =======

# A função input() lê o que o usuário digitar no teclado e retorna sempre uma string.
# Exemplo:
nome = input("Digite seu nome: ")  # O texto entre aspas é uma mensagem que aparece na tela
print("Olá,", nome, "! Seja bem-vindo(a)!")

# Se quisermos trabalhar com números, precisamos CONVERTER o valor de string para número.
# Para isso, usamos as funções int() (para inteiros) e float() (para números com casas decimais).

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

print("Você tem", idade, "anos e mede", altura, "metros.")


# ======= SAÍDA DE DADOS =======

# A função print() pode exibir textos, números e variáveis.
# Podemos separar os itens com vírgulas (Python adiciona automaticamente espaços).

print("A soma de 5 + 3 é", 5 + 3)

# Também podemos usar f-strings (forma moderna e prática de formatar textos)
# Basta colocar um 'f' antes das aspas e as variáveis entre chaves { }.

nome = "Ana"
idade = 12
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Podemos formatar números, como limitar casas decimais:
preco = 9.9876
print(f"O preço do produto é R$ {preco:.2f}")  # Mostra com 2 casas decimais


# ======= EXEMPLO PRÁTICO =======

# Programa simples que calcula a média de duas notas
print("\n=== CÁLCULO DE MÉDIA ===")

aluno = input("Nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"\nAluno: {aluno}")
print(f"Média: {media:.1f}")

# Podemos usar condições junto com a saída
if media >= 6:
    print("Situação: Aprovado ✅")
else:
    print("Situação: Reprovado ❌")


# ======= DICA EXTRA =======
# Podemos personalizar o final e o separador dos prints:
print("Olá", "mundo", sep=" - ", end="!!!\n")
# sep altera o separador padrão (espaço)
# end altera o que é colocado no final (por padrão é uma quebra de linha)

# Exemplo sem quebrar linha entre prints:
print("Ctrl", end="+")
print("Play")  # Saída: Ctrl+Play
