# -----------------------------------------------
# TEMA: MÓDULOS NO PYTHON
# -----------------------------------------------
# Baseado no conteúdo do curso Ctrl+Play – Introdução à Informática
# -----------------------------------------------
# Em Python, um MÓDULO é um arquivo que contém código (funções, variáveis, classes)
# que pode ser importado e reutilizado em outros programas.
#
# Isso ajuda a ORGANIZAR o código e EVITAR repetição.
# -----------------------------------------------


# ======= O QUE É UM MÓDULO? =======
# Imagine que você criou várias funções úteis em um arquivo separado,
# como "meu_modulo.py". Você pode importar esse arquivo em outro programa
# e usar tudo o que estiver dentro dele.
#
# Para isso, usamos a palavra-chave: import


# ======= EXEMPLO 1: IMPORTANDO UM MÓDULO PADRÃO =======
# O Python possui diversos módulos prontos, chamados "módulos da biblioteca padrão".
# Alguns exemplos: math, random, datetime, os, sys...

import math  # módulo de funções matemáticas

# Podemos usar funções do módulo math:
print("=== USANDO O MÓDULO math ===")
print("Raiz quadrada de 16:", math.sqrt(16))
print("Potência de 2 elevado a 3:", math.pow(2, 3))
print("Valor de PI:", math.pi)
print()


# ======= EXEMPLO 2: IMPORTANDO APENAS UMA FUNÇÃO =======
# Podemos importar apenas partes de um módulo usando:
# from nome_do_modulo import nome_da_funcao

from math import sqrt, pi

print("=== IMPORTANDO APENAS ALGUMAS FUNÇÕES ===")
print("Raiz quadrada de 9:", sqrt(9))
print("PI =", pi)
print()


# ======= EXEMPLO 3: DANDO UM APELIDO (alias) AO MÓDULO =======
# Às vezes o nome do módulo é grande. Podemos dar um apelido com "as".

import random as rd

print("=== USANDO APELIDO PARA UM MÓDULO ===")
numero = rd.randint(1, 10)  # gera um número aleatório de 1 a 10
print(f"Número sorteado: {numero}")
print()


# ======= EXEMPLO 4: CRIANDO SEU PRÓPRIO MÓDULO =======
# Podemos criar nossos próprios módulos!
# Basta criar um arquivo separado, por exemplo: utilidades.py
# e colocar dentro dele funções que serão reutilizadas em outros programas.
#
# Exemplo (conteúdo do arquivo utilidades.py):
#
# def saudacao(nome):
#     return f"Olá, {nome}! Seja bem-vindo(a)!"
#
# def dobro(x):
#     return x * 2
#
# Depois, em outro arquivo Python, podemos importar e usar:
# import utilidades
#
# print(utilidades.saudacao("Cinthia"))
# print(utilidades.dobro(7))
#
# Ou importar funções específicas:
# from utilidades import saudacao
# print(saudacao("Ctrl+Play"))


# ======= EXEMPLO 5: MÓDULOS COM APELIDO E IMPORTAÇÕES ESPECÍFICAS =======
# Podemos misturar formas de importação para deixar o código mais legível.

from math import factorial as fat

print("=== MISTURANDO FORMAS DE IMPORTAÇÃO ===")
print("Fatorial de 5:", fat(5))
print()


# ======= DICA EXTRA: AJUDA SOBRE MÓDULOS =======
# Podemos descobrir o que existe dentro de um módulo usando:
# help(nome_do_modulo)

# Exemplo:
# help(math)
# (Isso mostrará todas as funções e constantes disponíveis dentro de math)


# ======= CONCLUSÃO =======
# ➜ Módulos servem para organizar e reutilizar código.
# ➜ Existem módulos prontos no Python (math, random, datetime...).
# ➜ Podemos criar nossos próprios módulos personalizados.
# ➜ A importação pode ser feita de várias formas:
#     import nome_do_modulo
#     from nome_do_modulo import nome_da_funcao
#     import nome_do_modulo as apelido
#
# ➜ Reutilizar código é um passo importante para programar de forma profissional!
