# -----------------------------------------------
# TEMA: ESCREVENDO PACOTES NO PYTHON
# -----------------------------------------------
# Baseado no conteúdo do curso Ctrl+Play – Introdução à Informática
# -----------------------------------------------
# Quando criamos vários módulos (.py) relacionados, podemos reuni-los
# dentro de uma PASTA para formar um PACOTE.
#
# ➜ MÓDULO: arquivo Python (.py) que contém funções, classes, etc.
# ➜ PACOTE: uma pasta que agrupa vários módulos.
#
# Os pacotes tornam os projetos mais organizados e facilitam a reutilização do código.
# -----------------------------------------------


# ======= COMO CRIAR UM PACOTE =======
# Estrutura de exemplo de um projeto com pacote:
#
# meu_pacote/
# ├── __init__.py
# ├── calculos.py
# └── mensagens.py
#
# • A pasta "meu_pacote" é o PACOTE.
# • O arquivo "__init__.py" indica ao Python que essa pasta é um pacote.
# • Dentro da pasta, colocamos módulos (.py) com funções específicas.


# ======= EXEMPLO 1: CONTEÚDO DO ARQUIVO calculos.py =======
# def somar(a, b):
#     return a + b
#
# def subtrair(a, b):
#     return a - b
#
# def multiplicar(a, b):
#     return a * b
#
# def dividir(a, b):
#     if b == 0:
#         return "Erro: divisão por zero!"
#     return a / b


# ======= EXEMPLO 2: CONTEÚDO DO ARQUIVO mensagens.py =======
# def saudacao(nome):
#     return f"Olá, {nome}! Seja bem-vindo(a) ao Python!"
#
# def despedida(nome):
#     return f"Tchau, {nome}! Até a próxima aula!"


# ======= EXEMPLO 3: CONTEÚDO DO ARQUIVO __init__.py =======
# O arquivo __init__.py pode estar vazio ou conter importações automáticas.
#
# Exemplo:
# from .calculos import somar, subtrair, multiplicar, dividir
# from .mensagens import saudacao, despedida


# ======= EXEMPLO 4: USANDO O PACOTE EM OUTRO ARQUIVO =======
# No arquivo principal (main.py, por exemplo), podemos importar o pacote:

# import meu_pacote.calculos
# import meu_pacote.mensagens
#
# print(meu_pacote.calculos.somar(10, 5))
# print(meu_pacote.mensagens.saudacao("Cinthia"))


# ======= EXEMPLO 5: IMPORTANDO FUNÇÕES ESPECÍFICAS =======
# Podemos importar funções diretamente de dentro do pacote:
# from meu_pacote.calculos import multiplicar, dividir
# from meu_pacote.mensagens import saudacao
#
# print(multiplicar(3, 7))
# print(dividir(12, 3))
# print(saudacao("Aluno Ctrl+Play"))


# ======= EXEMPLO 6: DANDO APELIDOS (ALIAS) =======
# Podemos usar "as" para criar apelidos para pacotes ou funções:
# import meu_pacote.calculos as calc
#
# print(calc.subtrair(20, 8))


# ======= EXEMPLO 7: ORGANIZANDO SUBPACOTES =======
# Podemos criar pacotes dentro de pacotes (subpacotes), por exemplo:
#
# projeto/
# ├── utilidades/
# │   ├── __init__.py
# │   ├── calculos.py
# │   └── textos/
# │       ├── __init__.py
# │       └── mensagens.py
# └── main.py
#
# Dessa forma, mantemos cada parte do código bem organizada.


# ======= DICA: COMO IMPORTAR DE SUBPACOTES =======
# from utilidades.textos.mensagens import saudacao
# print(saudacao("Cinthia"))


# ======= CONCLUSÃO =======
# ➜ Pacotes ajudam a organizar projetos grandes.
# ➜ Devem conter o arquivo __init__.py (mesmo vazio).
# ➜ É possível criar subpacotes para dividir melhor o código.
# ➜ Podemos importar o pacote inteiro ou apenas partes dele.
# ➜ Usar pacotes é uma prática essencial em projetos profissionais!

# -----------------------------------------------
# EXERCÍCIO SUGERIDO:
# 1️⃣ Crie um pacote chamado "minhas_funcoes"
# 2️⃣ Adicione dois módulos: "matematica.py" e "textos.py"
# 3️⃣ No módulo matematica.py, crie funções de soma e multiplicação
# 4️⃣ No módulo textos.py, crie uma função de saudação
# 5️⃣ Importe o pacote no arquivo principal e teste as funções!
# -----------------------------------------------
