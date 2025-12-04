# ===============================================================
# 🐍 AULA – TUPLAS EM PYTHON
# Curso: Ctrl+Young 1 - F2F 14
# Profª: Cinthia Oliveira
# ===============================================================

# ---------------------------------------------------------------
# 📘 O QUE É UMA TUPLA?
# ---------------------------------------------------------------
# Uma tupla é uma estrutura de dados parecida com uma lista,
# porém com uma diferença importante:
# 🔒 Os valores de uma tupla NÃO podem ser alterados (imutáveis).
#
# Ou seja, depois de criada, você não pode:
#   - Adicionar novos elementos
#   - Remover elementos
#   - Alterar valores existentes
#
# Tuplas são muito úteis quando queremos armazenar dados
# que não devem ser modificados durante a execução do programa.

# ---------------------------------------------------------------
# 🔹 COMO CRIAR UMA TUPLA
# ---------------------------------------------------------------
# Usamos parênteses () para criar uma tupla.

numeros = (10, 20, 30, 40)
print("Tupla de números:", numeros)


nomes = ("Cinthia", "Arthur", "Oliver", "Ana")
print("Tupla de nomes:", nomes)

# Assim como nas listas, os índices começam do 0.
print("\nPrimeiro nome:", nomes[0])
print("Último nome:", nomes[-1])

print("\nListando todos os nomes da tupla:")
for nome in nomes:
    print(nome)

print("\nTamanho da tupla:", len(nomes))  # len() -> quantidade de itens
print("Maior número:", max(numeros))     # max() -> maior valor
print("Menor número:", min(numeros))     # min() -> menor valor
print("Soma dos números:", sum(numeros)) # sum() -> soma dos valores

# Podemos transformar uma tupla em lista se quisermos modificar os dados.
lista_nomes = list(nomes)
print("\nConvertendo tupla em lista:", lista_nomes)

# Agora é possível alterar:
lista_nomes.append("Beatriz")
print("Lista alterada:", lista_nomes)

# ---------------------------------------------------------------
# 🔹 CONVERTENDO LISTA DE VOLTA EM TUPLA
# ---------------------------------------------------------------
tupla_nova = tuple(lista_nomes)
print("\nConvertendo lista de volta em tupla:", tupla_nova)

# ---------------------------------------------------------------
# 🔹 TUPLAS COM UM ÚNICO ELEMENTO
# ---------------------------------------------------------------
# Importante: para criar uma tupla com um só item, use uma vírgula no final.
tupla_unica = ("Python",)
print("\nTupla com um elemento:", tupla_unica)
print("Tipo da variável:", type(tupla_unica))

# ---------------------------------------------------------------
# 🔹 DESEMPACOTAMENTO DE TUPLAS
# ---------------------------------------------------------------
# É possível "desmontar" uma tupla em variáveis individuais.
coordenadas = (10, 20, 30)
x, y, z = coordenadas

print("\nDesempacotando tupla:")
print(f"x = {x}, y = {y}, z = {z}")

# ---------------------------------------------------------------
# 🔹 TUPLAS DENTRO DE OUTRAS TUPLAS (ANINHADAS)
# ---------------------------------------------------------------
alunos = (
    ("Arthur", 10),
    ("Beatriz", 8),
    ("Oliver", 9)
)

print("\nTupla com tuplas:")
print(alunos)

print("Primeiro aluno:", alunos[0][0])  # Acessa o nome "Arthur"
print("Nota do segundo aluno:", alunos[1][1])  # Acessa a nota 8

# ---------------------------------------------------------------
# 💡 RESUMO RÁPIDO:
# ---------------------------------------------------------------
# ✅ Criar: tupla = (1, 2, 3)
# ✅ Acessar: tupla[0]
# ✅ Imutável: não pode alterar valores
# ✅ Converter para lista: list(tupla)
# ✅ Converter para tupla: tuple(lista)
# ✅ Pode armazenar tipos mistos: ("Texto", 42, True)
# ---------------------------------------------------------------
