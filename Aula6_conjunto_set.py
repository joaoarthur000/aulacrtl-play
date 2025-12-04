# ===============================================================
# 🐍 AULA – CONJUNTOS (SETS) EM PYTHON
# Curso: Ctrl+Young 1 - F2F 14
# Profª: Cinthia Oliveira
# ===============================================================

# ---------------------------------------------------------------
# 📘 O QUE É UM CONJUNTO?
# ---------------------------------------------------------------
# Um conjunto (set) é uma coleção de elementos ÚNICOS e NÃO ordenados.
# Isso significa que:
#   - Não há elementos repetidos.
#   - A ordem dos itens não é garantida.
#
# É muito útil quando queremos eliminar duplicatas ou fazer operações
# matemáticas como união, interseção e diferença.

# ---------------------------------------------------------------
# 🔹 COMO CRIAR UM CONJUNTO
# ---------------------------------------------------------------
# Podemos criar conjuntos com chaves {} ou com a função set().

frutas = {"maçã", "banana", "uva", "maçã"}
print("Conjunto de frutas:", frutas)  # "maçã" repetida será ignorada

numeros = set([1, 2, 3, 2, 1])
print("Conjunto de números:", numeros)

# ---------------------------------------------------------------
# 🔹 ADICIONAR E REMOVER ELEMENTOS
# ---------------------------------------------------------------
# Adiciona um elemento com add()
frutas.add("laranja")
print("\nApós adicionar 'laranja':", frutas)

# Remove um elemento com remove()
frutas.remove("banana")
print("Após remover 'banana':", frutas)

# Se quiser evitar erro ao remover algo que não existe, use discard()
frutas.discard("pera")

# ---------------------------------------------------------------
# 🔹 VERIFICANDO SE UM ELEMENTO EXISTE NO CONJUNTO
# ---------------------------------------------------------------
print("\n'uva' está no conjunto?", "uva" in frutas)
print("'banana' está no conjunto?", "banana" in frutas)

# ---------------------------------------------------------------
# 🔹 PERCORRENDO UM CONJUNTO COM FOR
# ---------------------------------------------------------------
print("\nListando todas as frutas:")
for fruta in frutas:
    print(fruta)

# ---------------------------------------------------------------
# 🔹 OPERAÇÕES ENTRE CONJUNTOS
# ---------------------------------------------------------------
# Vamos criar dois conjuntos de exemplo:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# União → junta todos os elementos (sem repetir)
uniao = A | B
print("\nUnião:", uniao)

# Interseção → mostra apenas os elementos em comum
intersecao = A & B
print("Interseção:", intersecao)

# Diferença → mostra o que tem em A mas não em B
diferenca = A - B
print("Diferença (A - B):", diferenca)

# Diferença simétrica → elementos que estão em apenas um dos conjuntos
dif_simetrica = A ^ B
print("Diferença Simétrica:", dif_simetrica)

# ---------------------------------------------------------------
# 🔹 FUNÇÕES ÚTEIS
# ---------------------------------------------------------------
print("\nTamanho do conjunto A:", len(A))
print("Máximo valor de A:", max(A))
print("Mínimo valor de A:", min(A))

# Limpando todos os elementos do conjunto
B.clear()
print("Conjunto B após clear():", B)

# ---------------------------------------------------------------
# 🔹 CONJUNTOS IMUTÁVEIS (FROZEN SETS)
# ---------------------------------------------------------------
# Se quisermos criar um conjunto que não pode ser alterado:
conjunto_fixo = frozenset([1, 2, 3])
print("\nConjunto imutável (frozenset):", conjunto_fixo)

# ---------------------------------------------------------------
# 💡 RESUMO RÁPIDO:
# ---------------------------------------------------------------
# ✅ Criar: conjunto = {1, 2, 3}
# ✅ Criar vazio: conjunto = set()
# ✅ Adicionar: conjunto.add(x)
# ✅ Remover: conjunto.remove(x) ou conjunto.discard(x)
# ✅ União: A | B
# ✅ Interseção: A & B
# ✅ Diferença: A - B
# ✅ Diferença simétrica: A ^ B
# ✅ Imutável: frozenset([1, 2, 3])
# ---------------------------------------------------------------
