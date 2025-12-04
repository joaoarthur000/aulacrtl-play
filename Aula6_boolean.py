# ============================================
# 📘 CAPÍTULO: BOOLEAN (TIPO LÓGICO)
# Curso: Ctrl+Young 1 - F2F 14
# Professora: Cinthia Oliveira
# ============================================

# O tipo Boolean (ou lógico) é usado para representar apenas dois valores:
# True (Verdadeiro) ou False (Falso)
# Ele é muito usado em comparações e estruturas condicionais.

# Exemplo básico:
print(True)
print(False)
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# ============================================
# 🔹 COMPARAÇÕES RETORNAM VALORES BOOLEANOS
# ============================================

# Operadores de comparação:
# ==  → Igual
# !=  → Diferente
# >   → Maior que
# <   → Menor que
# >=  → Maior ou igual
# <=  → Menor ou igual

a = 10
b = 5

print(a == b)   # False - 10 não é igual a 5
print(a != b)   # True  - 10 é diferente de 5
print(a > b)    # True  - 10 é maior que 5
print(a < b)    # False - 10 não é menor que 5
print(a >= 10)  # True  - 10 é maior ou igual a 10
print(b <= 5)   # True  - 5 é menor ou igual a 5


# ============================================
# 🔹 OPERADORES LÓGICOS
# ============================================
# São usados para combinar expressões booleanas.

# and → verdadeiro se as duas condições forem verdadeiras
# or  → verdadeiro se pelo menos uma condição for verdadeira
# not → inverte o valor lógico (True ↔ False)

idade = 16
tem_autorizacao = True

# Exemplo com "and"
print(idade >= 18 and tem_autorizacao)  # False, pois idade não é >= 18

# Exemplo com "or"
print(idade >= 18 or tem_autorizacao)   # True, pois há autorização

# Exemplo com "not"
print(not tem_autorizacao)  # False, pois o valor é invertido


# ============================================
# 🔹 USANDO BOOLEAN EM CONDIÇÕES (IF)
# ============================================

chovendo = True

if chovendo:
    print("Pegue um guarda-chuva!")
else:
    print("Dia ensolarado, aproveite!")

# Outro exemplo:
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir ainda.")


# ============================================
# 🔹 CONVERSÃO PARA BOOLEAN
# ============================================
# Em Python, alguns valores são considerados "falsos" automaticamente:
# False, 0, "", [], {}, None
# Todo o resto é considerado "verdadeiro".

print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool("Oi"))    # True
print(bool(42))      # True

# Isso é muito útil em estruturas condicionais:
mensagem = ""

if mensagem:
    print("Mensagem recebida!")
else:
    print("Nenhuma mensagem ainda...")


# Em Python, None é um tipo especial (NoneType) usado para indicar que
# não existe um valor válido em uma variável ou
# que uma função não retornou nada.

# Em resumo:
# None significa “sem valor”, “vazio” ou “não definido”.

# ============================================
# 🔹 EXERCÍCIO RÁPIDO
# ============================================
# 1. Crie um programa que pergunte a idade do usuário.
# 2. Use uma expressão booleana para verificar se ele é maior de idade.
# 3. Exiba “Acesso permitido” ou “Acesso negado”.

# Exemplo:
# idade_usuario = int(input("Digite sua idade: "))
# maior_de_idade = idade_usuario >= 18
# print("Acesso permitido:", maior_de_idade)

# ============================================
# Fim do Capítulo - Boolean
# ============================================
