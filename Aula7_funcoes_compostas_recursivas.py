# -----------------------------------------------
# TEMA: FUNÇÕES COMPOSTAS E RECURSIVAS
# -----------------------------------------------
# Baseado no conteúdo do curso Ctrl+Play – Introdução à Informática
# -----------------------------------------------
# Em Python, uma FUNÇÃO é um bloco de código que realiza uma tarefa específica.
# Já vimos funções simples — agora vamos estudar as COMPOSTAS e RECURSIVAS.
# -----------------------------------------------


# ======= FUNÇÕES COMPOSTAS =======
# São funções que chamam OUTRAS funções dentro delas.
# Isso ajuda a organizar o código, tornando-o mais claro e reutilizável.


# Exemplo: calcular a média e verificar a situação do aluno
def calcular_media(n1, n2):
    return (n1 + n2) / 2


def verificar_situacao(media):
    if media >= 6:
        return "Aprovado ✅"
    else:
        return "Reprovado ❌"


def mostrar_resultado():
    nome = input("Nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = calcular_media(nota1, nota2)  # Chama uma função dentro de outra
    situacao = verificar_situacao(media)  # Outra chamada

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")


# Chamando a função principal
# mostrar_resultado()


# ======= FUNÇÕES RECURSIVAS =======
# Uma função RECURSIVA é aquela que CHAMA ELA MESMA dentro de seu código.
# É usada para resolver problemas que podem ser divididos em partes menores.
# ⚠️ Importante: toda função recursiva precisa ter um caso base (condição de parada),
# senão ela chamará a si mesma infinitamente!


# Exemplo 1: contagem regressiva recursiva
def contagem_regressiva(n):
    if n == 0:  # Caso base
        print("Fim!")
    else:
        print(n)
        contagem_regressiva(n - 1)  # A função chama ela mesma


# contagem_regressiva(5)


# Exemplo 2: cálculo de fatorial recursivo
# O fatorial de um número (n!) é o produto de todos os números de 1 até n.
# Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120

def fatorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva


# Testando o fatorial
# numero = int(input("Digite um número para calcular o fatorial: "))
# print(f"O fatorial de {numero} é {fatorial(numero)}")


# ======= DIFERENÇA ENTRE FUNÇÃO COMPOSTA E RECURSIVA =======
# • COMPOSTA: chama OUTRAS funções.
# • RECURSIVA: chama ELA MESMA.


# ======= EXEMPLO PRÁTICO =======
# Vamos juntar os dois tipos em um mesmo programa:
# Um programa que mostra a soma dos números de 1 até n de forma recursiva,
# e chama essa função dentro de outra (função composta).

def soma_recursiva(n):
    """Soma os números de 1 até n usando recursão"""
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)


def executar_soma():
    numero = int(input("Digite um número inteiro: "))
    resultado = soma_recursiva(numero)
    print(f"A soma de 1 até {numero} é {resultado}")

# executar_soma()


# ======= CONCLUSÃO =======
# ➜ Funções compostas: ajudam a dividir o programa em partes menores.
# ➜ Funções recursivas: resolvem problemas repetitivos chamando a si mesmas.
# ➜ Sempre defina um caso base na recursão!
# ➜ Juntas, essas funções tornam o código mais organizado e poderoso.
