# ============================================
# 📘 CAPÍTULO: FUNÇÕES EM PYTHON
# Curso: Ctrl+Young 1 - F2F 14
# Professora: Cinthia Oliveira
# ============================================

# 🔹 O que é uma função?
# Uma função é um bloco de código que executa uma tarefa específica.
# Ela serve para organizar, reutilizar e deixar o código mais limpo.

# Estrutura básica:
# def nome_da_funcao():
#   # bloco de código
#   instruções...

# Exemplo simples:
def saudacao():
    print("Olá, seja bem-vindo(a) à Ctrl+Play!")

# Chamando (executando) a função:
saudacao()


# ============================================
# 🔹 FUNÇÕES COM PARÂMETROS
# ============================================
# Parâmetros permitem enviar informações para dentro da função.


def apresentar_aluno(nome, idade):
    print(f"O aluno {nome} tem {idade} anos.")

apresentar_aluno("Cinthia",24)
apresentar_aluno("Arthur", 12)


# ============================================
# 🔹 FUNÇÕES COM RETORNO (return)
# ============================================
# Uma função pode "devolver" um resultado com a palavra-chave return.
# Isso permite usar o valor retornado em outras partes do código.

def somar(a, b):
    resultado = a + b
    return resultado

# Usando o retorno da função:
soma = somar(5, 7)
print(f"O resultado da soma é: {soma}")


# ============================================
# 🔹 RETURN x PRINT
# ============================================
# - print() apenas exibe algo na tela
# - return envia o valor de volta para quem chamou a função

def multiplicar(a, b):
    return a * b

produto = multiplicar(3, 4)
print(f"Produto: {produto}")


# ============================================
# 🔹 FUNÇÃO COM VALOR PADRÃO (DEFAULT)
# ============================================
# É possível definir valores padrão para os parâmetros.
# Se o usuário não informar, o valor padrão será usado.

def boas_vindas(nome="aluno"):
    print(f"Bem-vindo(a), {nome}!")

boas_vindas("Cinthia")
boas_vindas()  # usa o valor padrão "aluno"


# ============================================
# 🔹 FUNÇÃO COM MÚLTIPLOS PARÂMETROS (*args)
# ============================================
# Quando não sabemos quantos argumentos serão passados,
# usamos *args para receber vários valores.

def listar_itens(*itens):
    print("Itens recebidos:")
    for item in itens:
        print("-", item)

listar_itens("Robô", "Arduino", "Sensor Ultrassônico", "Micro:bit")


# ============================================
# 🔹 FUNÇÃO COM PARÂMETROS NOMEADOS (**kwargs)
# ============================================
# **kwargs permite receber vários pares "chave=valor".

def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Arthur", idade=12, curso="Robótica")


# ============================================
# 🔹 FUNÇÕES ANINHADAS (Função dentro de outra)
# ============================================
# É possível criar funções dentro de outras funções.

def calculadora(a, b):
    def somar():
        return a + b
    def subtrair():
        return a - b
    return somar(), subtrair()

resultado_soma, resultado_sub = calculadora(10, 5)
print(f"Soma: {resultado_soma}, Subtração: {resultado_sub}")


# ============================================
# 🔹 ESCOPO DE VARIÁVEIS
# ============================================
# Variáveis podem ser:
# - Locais: criadas dentro da função e só existem lá
# - Globais: criadas fora da função e visíveis em todo o código

mensagem_global = "Ctrl+Play é demais!"

def mostrar_mensagem():
    mensagem_local = "Aprendendo Funções em Python!"
    print(mensagem_local)
    print(mensagem_global)

mostrar_mensagem()
# print(mensagem_local)  # ❌ erro, pois é uma variável local


# ============================================
# 🔹 DOCUMENTANDO FUNÇÕES (DOCSTRING)
# ============================================
# É uma boa prática descrever o que a função faz.

def dividir(a, b):
    """
    Função que divide dois números e retorna o resultado.
    Parâmetros:
        a (float): dividendo
        b (float): divisor
    Retorna:
        float: resultado da divisão
    """
    return a / b

print(dividir(10, 2))


# ============================================
# 🔹 EXEMPLO PRÁTICO: CALCULADORA SIMPLES
# ============================================

def calculadora_simples(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    else:
        return "Operação inválida!"

print(calculadora_simples(10, 5, "+"))
print(calculadora_simples(10, 5, "*"))
print(calculadora_simples(10, 5, "/"))
print(calculadora_simples(10, 5, "-"))
print(calculadora_simples(10, 5, "%"))  # operação inválida


# ============================================
# 🔹 CONCLUSÃO
# ============================================
# As funções tornam o código mais organizado, reutilizável e fácil de entender.
# Elas são a base da programação estruturada e da programação modular.
# ============================================
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")