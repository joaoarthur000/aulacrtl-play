# -----------------------------------------------
# TEMA: CRIANDO UM ARQUIVO EM PYTHON
# -----------------------------------------------
# Baseado no conteúdo do curso Ctrl+Play – Introdução à Informática
# -----------------------------------------------
# Em Python, podemos criar, abrir, escrever e ler arquivos de texto.
# Isso é feito com a função open(), que permite manipular arquivos
# armazenados no computador.
# -----------------------------------------------


# ======= A FUNÇÃO open() =======
# A função open() serve para abrir (ou criar) arquivos.
# Sua estrutura básica é:
# open("nome_do_arquivo", "modo")

# Os principais modos de abertura são:
# 'w' → escrita (write): cria um novo arquivo ou sobrescreve um existente
# 'a' → anexar (append): adiciona conteúdo no final de um arquivo existente
# 'r' → leitura (read): abre um arquivo existente apenas para ler


# ======= CRIANDO E ESCREVENDO EM UM ARQUIVO =======
# Exemplo: criando um arquivo e escrevendo dentro dele

arquivo = open("exemplo.txt", "w")  # cria o arquivo para escrita
arquivo.write("Olá, mundo!\n")
arquivo.write("Este é o meu primeiro arquivo em Python.\n")
arquivo.write("Estou aprendendo a salvar informações!\n")
arquivo.close()  # sempre feche o arquivo após usar

print("Arquivo criado e texto salvo com sucesso!")


# ======= ACRESCENTANDO MAIS INFORMAÇÕES =======
# Se quisermos adicionar mais texto sem apagar o conteúdo anterior,
# usamos o modo 'a' (append).

arquivo = open("exemplo.txt", "a")
arquivo.write("Agora adicionei mais uma linha ao arquivo.\n")
arquivo.close()

print("Novo texto adicionado ao arquivo!")


# ======= LENDO UM ARQUIVO =======
# Para ler o conteúdo de um arquivo, usamos o modo 'r' (read).

arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()  # lê todo o conteúdo do arquivo
arquivo.close()

print("\n--- CONTEÚDO DO ARQUIVO ---")
print(conteudo)


# ======= USANDO 'with open()' =======
# O Python também permite usar o comando 'with' para abrir arquivos.
# Ele fecha o arquivo automaticamente ao final do bloco.

with open("exemplo.txt", "a") as arquivo:
    arquivo.write("Linha adicionada com 'with open()'.\n")

print("Linha adicionada com sucesso usando 'with'!")


# ======= DICA: LENDO LINHA POR LINHA =======
# Podemos ler o arquivo linha por linha usando um loop for.

print("\n--- LENDO LINHA POR LINHA ---")
with open("exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove quebras de linha extras


# ======= CONCLUSÃO =======
# ➜ 'w' cria ou sobrescreve arquivos.
# ➜ 'a' adiciona conteúdo ao final.
# ➜ 'r' lê o conteúdo de um arquivo existente.
# ➜ Sempre use close() ou 'with' para fechar o arquivo corretamente.
# ➜ Manipular arquivos é essencial para salvar e recuperar informações!
