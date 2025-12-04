# ============================================
# 📘 CAPÍTULO: DICIONÁRIOS EM PYTHON (dict)
# Curso: Ctrl+Young 1 - F2F 14
# Professora: Cinthia Oliveira
# ============================================

# 🔹 O que é um DICIONÁRIO?
# Um dicionário (dict) é uma estrutura de dados que armazena informações em PARES:
#   → "chave" : "valor"
# Cada chave é única e serve para acessar seu respectivo valor.

# Exemplo simples:
aluno = {
    "nome": "Cinthia",
    "idade": 24,
    "curso": "Programação e Robótica"
}

print(aluno)
print(type(aluno))  # <class 'dict'>


# ============================================
# 🔹 ACESSANDO VALORES NO DICIONÁRIO
# ============================================

# Acessar um valor usando sua chave:
print(aluno["nome"])   # Exibe: Cinthia
print(aluno["idade"])  # Exibe: 24

# Forma alternativa e segura com o método get()
# (Evita erro se a chave não existir)
print(aluno.get("curso"))  # Exibe: Programação e Robótica
print(aluno.get("nota", "Chave não encontrada"))


# ============================================
# 🔹 ADICIONANDO E ALTERANDO VALORES
# ============================================

# Adicionar nova chave e valor:
aluno["nota"] = 9.5
print(aluno)

# Alterar valor existente:
aluno["idade"] = 25
print(f"Idade atualizada: {aluno['idade']}")


# ============================================
# 🔹 REMOVENDO ITENS DO DICIONÁRIO
# ============================================

# Remover uma chave específica com del:
del aluno["curso"]
print(aluno)

# Remover e retornar um valor usando pop():
nota_removida = aluno.pop("nota")
print(f"Nota removida: {nota_removida}")

# Limpar todo o dicionário:
aluno.clear()
print(f"Dicionário limpo: {aluno}")


# ============================================
# 🔹 DICIONÁRIO COM LISTAS E OUTROS DICIONÁRIOS
# ============================================

# Um dicionário pode conter listas ou até outros dicionários!
aluno = {
    "nome": "Arthur",
    "idade": 12,
    "materias": ["Robótica", "Programação", "Matemática"],
    "endereco": {
        "cidade": "São Paulo",
        "bairro": "Centro"
    }
}

# Acessando dados dentro de listas e dicionários:
print(aluno["materias"][0])        # Robótica
print(aluno["endereco"]["cidade"]) # São Paulo


# ============================================
# 🔹 PERCORRENDO UM DICIONÁRIO (loop for)
# ============================================

# Percorrendo apenas as chaves:
for chave in aluno:
    print(chave)

# Percorrendo chaves e valores:
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Percorrendo apenas os valores:
for valor in aluno.values():
    print(valor)

# Percorrendo apenas as chaves:
for chave in aluno.keys():
    print(chave)


# ============================================
# 🔹 FUNÇÕES ÚTEIS COM DICIONÁRIOS
# ============================================

# len() → Conta quantos pares existem
print(f"Total de informações no dicionário: {len(aluno)}")

# in → Verifica se uma chave existe
print("idade" in aluno)   # True
print("nota" in aluno)    # False


# ============================================
# 🔹 EXEMPLO PRÁTICO: CADASTRO DE ALUNOS
# ============================================

# Criando uma lista de dicionários:
alunos = [
    {"nome": "Bruna", "idade": 13, "nota": 9.2},
    {"nome": "Lucas", "idade": 12, "nota": 8.7},
    {"nome": "Isabela", "idade": 11, "nota": 9.0}
]

# Exibindo informações de todos os alunos:
for aluno in alunos:
    print(f"{aluno['nome']} tem {aluno['idade']} anos e tirou nota {aluno['nota']}.")

# Média das notas:
soma_notas = 0
for aluno in alunos:
    soma_notas += aluno["nota"]

media = soma_notas / len(alunos)
print(f"Média da turma: {media:.2f}")

# ============================================
# 🔹 CONCLUSÃO
# ============================================
# Dicionários são extremamente úteis para organizar dados nomeados.
# Eles são muito usados em APIs, bancos de dados e programas que manipulam informações.
# ============================================
