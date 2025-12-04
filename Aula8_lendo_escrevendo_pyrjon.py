# -----------------------------------------------
# TEMA: LENDO, ESCREVENDO E FECHANDO ARQUIVOS EM PYTHON
# -----------------------------------------------
# Baseado no conteúdo do curso Ctrl+Play – Introdução à Informática
# -----------------------------------------------
# Em Python, podemos criar, escrever, ler e fechar arquivos de texto (.txt)
# usando a função open().
# Manipular arquivos é importante para armazenar dados e recuperá-los depois.
# -----------------------------------------------


# ======= FUNÇÃO open() =======
# A função open() abre ou cria um arquivo e pode trabalhar em diferentes "modos":
#   'w' → write (escrever): cria um novo arquivo ou apaga o conteúdo anterior
#   'a' → append (anexar): adiciona conteúdo ao final do arquivo existente
#   'r' → read (ler): abre o arquivo para leitura

# Estrutura básica:
# arquivo = open("nome_do_arquivo.txt", "modo")


# ======= ESCREVENDO EM UM ARQUIVO =======
print("=== ESCRITA DE ARQUIVO ===")

# Criando ou sobrescrevendo um arquivo:
arquivo = open("dados.txt", "w")  # modo escrita
arquivo.write("Primeira linha do arquivo.\n")
arquivo.write("Segunda linha escrita com Python.\n")
arquivo.write("Terceira linha salva com sucesso!\n")

# Após escrever, é importante FECHAR o arquivo para salvar as alterações.
arquivo.close()

print("Arquivo criado e escrito com sucesso!\n")


# ======= LENDO UM ARQUIVO =======
print("=== LEITURA DE ARQUIVO ===")

# Agora vamos abrir o mesmo arquivo para leitura.
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()  # lê todo o conteúdo do arquivo
print("Conteúdo do arquivo:\n")
print(conteudo)
arquivo.close()  # fecha o arquivo

# Podemos também ler linha por linha:
arquivo = open("dados.txt", "r")
print("\nLendo linha por linha:")
for linha in arquivo:
    print(linha.strip())  # strip() remove quebras de linha extras
arquivo.close()


# ======= ADICIONANDO MAIS CONTEÚDO =======
print("\n=== ADICIONANDO MAIS TEXTO ===")

# O modo 'a' adiciona conteúdo ao final sem apagar o que já existe.
arquivo = open("dados.txt", "a")
arquivo.write("Nova linha adicionada ao final do arquivo.\n")
arquivo.close()

print("Nova linha adicionada com sucesso!\n")


# ======= USANDO 'with open()' =======
# O 'with' é uma forma mais segura e prática de trabalhar com arquivos.
# Ele fecha o arquivo automaticamente ao final do bloco.

print("=== USANDO 'WITH OPEN()' ===")

with open("dados.txt", "a") as arquivo:
    arquivo.write("Linha adicionada usando 'with open()'.\n")

print("Arquivo atualizado com 'with open()'.\n")

# Lendo novamente o arquivo completo:
with open("dados.txt", "r") as arquivo:
    print("--- CONTEÚDO FINAL DO ARQUIVO ---")
    print(arquivo.read())


# ======= RESUMO =======
# ➜ 'w' cria um novo arquivo ou apaga o conteúdo anterior.
# ➜ 'a' adiciona conteúdo ao final do arquivo.
# ➜ 'r' lê o conteúdo de um arquivo existente.
# ➜ Sempre feche o arquivo após o uso (close()) ou use 'with open()' para fechar automaticamente.
# ➜ Trabalhar com arquivos é essencial para salvar e recuperar dados de forma permanente.
