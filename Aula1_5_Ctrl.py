'''
PROGRAMAÇÃO PYTHON

- Algorítmo (passo-a-passo):
Sequência lógica para solucionar um problema ou executar uma tarefa

- Lógica de Programação
Linguagem da máquina; é como as máquinas enviam e recebem informação

- Linguagem de Programação
"Idioma" das máquinas. É como criamos nossos programas e sistemas.
Exemplos: Python, JavaScript, C++, C#, Java, PHP, React

- Variável
Espaço na memória onde armazenamos informações dentro sistema
    Tipos de variável:
        Inteiro - (1 - 2 - 3 - 4...)
        Decimal/Float - (1,64 - 4,50 - 12,10 - 42,35)
        String - Textos
        Boolean - True/False (Verdadeiro/Falso)
'''

# COMANDOS BÁSICOS DE PYTHON

# ARITMÉTICA BÁSICA
print("COMANDOS DE ARITMÉTICA BÁSICA:")
print("Adição: 10 + 10")
print(10 + 10)

print("\nSubtração: 15 - 10")
print(15 - 10)

print("\nDivisão: 20 / 10")
print(20 / 10)

print("\nMultiplicação: 10 * 2")
print(10 * 2)

print("\nPotencia: 2 ** 3")
print(2 ** 3)


# VARIÁVEIS - TYPE
#TYPE() - MOSTRAR O TIPO DA INFORMAÇÃO
print("\nTIPO DE VARIAVEIS COM A FUNÇÃO type():")
print(type(1.5)) # Decimal/Float
print(type(52)) # Inteiro
print(type("Cinthia")) # String
print(type(True)) # Blooleano


# VARIÁVEIS SÃO ONDE ARMAZENAMOS OS DADOS NO SISTEMAS
print("\nARMAZENANDO DIFERENTES TIPOS DE VARIÁVEIS:")
numero = 110 # Armazenei um número inteiro
print(numero)

numero = numero + numero # Calculei e substitui o valor da variável
print(numero)

nome = "Cinthia Oliveira" # String - armazenar texto
print("\nPrazer! Eu sou " + nome) # Concatenação - Junta informações
print(f"Meu nome é {nome}\n") # Formatação

# NOME DE VARIÁVEL
# Iniciar sempre com letra minuscula
# Não pode ter caracter especial, com exeção do underline (“_”)
# Não pode ter espaço

#STRINGS
print("\nIMPRIMINDO STRING:")
string1 = "Olá, bom dia!"
string2 = "Seja bem-vindo(a)"
string3 = "Aqui é a Ctrl+Play e você aprenderá Programação e Robótica."
print(string1)
print(string2)
print(string3)

string4 = "teste"
print(string4)
print("teste")

# MÉTODOS DE STRINGS
print("\nMÉTODOS STRINGS:")
curso = "Curso de Programação e Robótica"
print(curso.upper()) # UPPER - Maiúsculo
print(curso.lower()) # LOWER - Minúsculo

materia = curso.split() # SPLIT - divide a string em "blocos"
print(materia[2])

# CONTA A QUANTIDADE DE CARACTER DENTRO DA STRING
print(f"\nA função len() contou {len(curso)} caracteres na variavel CURSO")
print(f"A função len() contou {len(materia)} caracteres na variavel MATERIA")

# \n - SALTA LINHA
print("\nSaltando \nLinha\n")

# \t - Adiciona espaço no texto
print("Acrescentando\tespaço\tno\t\tTexto.\n")


# INDEXAÇÃO/IMUTABILIDADE DE STRING - ACESSANDO PARTES ESPECÍFICAS DA STRING
print("\nINDEXAÇÃO - STRING:")
empresa = "CTRL + PLAY "
print(empresa[0]) # Pega o valor da posição determinada
print(empresa[1])
print(empresa[2])
print(empresa[3])

# REPETIÇÃO DE VARIÁVEL
print("\nReprtição de variável:")
print(empresa*5+"\n") #executar a repetição da variável

print("\nImprimindo partes específicas da string:")
# Imprime o valor da variavel a partir do caracter especificado
print(empresa[5:])
print(empresa[:5])

# Imprime o intervalo de uma string de acordo com as posições definidas
print(empresa[3:9])

# Usando numero negativos para retroceder
print(empresa[-3])

# Impimindo o texto com exceção dos ultimos caracteres
print(empresa[:-2])

# Impime o texto "excluindo" uma letra a cada dois caracteres
print(empresa[::2])

# Utilize o find() para encontrar caracteres dentro de uma string
'''
Find() retorna a posição do caractere que procura. 
Caso o caractere não esteja na string, será retornado a posição “-1”
'''
print("\nLocalizando caractere na string:")
email = "cinthiab.oliveira@outlook.com"
print(email.find("@"))
print(email.find("y"))

# Função count() verifica a quantidade de caracteres específicos em uma string
print("\nConta a quantidade de um caractere específico na string:")
print(email.count("a"))

# CONVERTENDO VARIAVEIS PARA STRING - STR()
print("\nCONVERTENDO TIPO DE VARIVEL PARA STRING - FUNÇÃO STR()")
num_idade=24
print(type(num_idade))
num_idade = str(num_idade)
print(type(num_idade))
print(f"Eu tenho {num_idade} anos.\n")

# ENTRADA DE DADOS - input()
''' ##TIRAR O COMENTARIO DAS ASPAS SIMPLES PARA TESTAR
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("\nMeu nome é " + nome + "e tenho " + idade + "anos.")
'''

# VETOR/LISTA - conjunto de dados ordenados com a posição inicial equivalente a 0 (zero)
convidado = ["Cinthia", "Frederico", "Arthur", "Matheus"]
print(convidado) # Exibe a lista inteira
print("A festa é da " + convidado[0]) # Exibe a posição selecionada

# EXIBINDO LISTA EM ORDEM CRESCENTE E DECRESCENTE
print("\n\nLista em ordem crescente: \n")
print(convidado[0])
print(convidado[1])
print(convidado[2])
print(convidado[3])

print("\n\nLista em ordem decrescente: \n")
print(convidado[-1])
print(convidado[-2])
print(convidado[-3])
print(convidado[-4])

# SUBSTITUIR DADO NA LIST
convidado[0] = "Oliver"
print(f"\nSubstituindo dado da lista:\n{convidado}")

# ADICIONANDO NOVO ITEM NO FINAL DA LISTA - append()
convidado.append("Ana Beatriz")
print(f"\nAdicionando novo item ao final da lista: \n{convidado}")

# INSERINDO NOVO ITEM EM QUALQUER POSIÇÃO DA LISTA - insert()
convidado.insert(3, "Maria")
convidado.insert(0, "João")
print(f"\nInserindo novo item numa posição pré definida: \n{convidado}")

# REMOVENDO ITEM DA LISTA - del
del convidado[0]
print(f"\nRemovendo dado da lista:\n{convidado}")

# REMOVENDO ITEM ESPECÍFICO - pop()
convidadoPop = convidado.pop(3)
print(f"\nRemovendo dado específico da lista com POP():\n{convidadoPop}")

# REMOVENDO ITEM DA LISTA UM A UM - pop()
convidadoRemovido = convidado.pop()
print(f"\nRemovendo item uma a um:\n{convidadoRemovido}")

# ARMAZENANDO VARIAVEL REMOVIDA DA LISTA - remove()
itinerario = ["Ilha Bela", "Praia Grande", "Mongagua", "Cachoeirinha", "Aguas Cláras","Bela Vista","Santos","Conchas"]
viajante = (itinerario[2])
itinerario.remove(viajante)
print(f"\nDado removido da lista: {viajante}")

# LISTA EM ORDEM ALFABÉTICA
itinerario.sort()
print(f"\nLista em ordem alfabética: \n{itinerario}")

# LISTA EM ORDEM INVERSA
itinerario.sort(reverse=True)
print(f"\nLista em ordem alfabética: \n{itinerario}")

# ALTERANDO A ORDEM DOS DADOS EM ALTERAR A ESTRUTURA DA VARIÁVEL:
print("\nOrdem original da lista:")
print(itinerario)
print(f"\nOrdem alfabética sem alterar a estrutura:\n{sorted(itinerario)}")
print(f"\nOrdem inversa sem alterar a estrutura:\n{sorted(itinerario, reverse=True)}")


# METODO REVERSE() INVERTE A ORDEM DA LISTA
feira = ["maça","uva","banana","abacaxi"]
print("\nOrdem original da lista:")
print(feira)

feira.reverse()
print("\nOrdem inversa da lista:")
print(feira)

#EXIBI TAMANHO DA LISTA - len()
print(f"Tamanho da lista Feira: \n{len(feira)}")

# CRIA LISTA DE NÚMEROS
list_numero = list(range(1,11))
print(f"\nLista números: \n{list_numero}")

# MENOR VALOR
print(f"\nMenor valor: {min(list_numero)}")

# MAIOR VALOR
print(f"\nMenor valor: {max(list_numero)}")

# EXIBIR PARTE ESPECÍFICA DA LISTA
print(f"Exibindo parte específica da lista: \n{list_numero[3:9]}")

# COPIAR LISTA
list_numero2 = list_numero[:]
print(f"\nLista 2 Copiada: \n{list_numero2}")


# CRIANDO MATRIZ
# Criando uma matriz 3x3
matriz_numero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"\nCriando Matriz Número: \n{matriz_numero}")

# Criando uma matriz 3x3 com nomes
matriz_nome = [
    ["Ana", "Bruno", "Carla"],
    ["Daniel", "Eva", "Felipe"],
    ["Gustavo", "Helena", "Igor"]
]

print(f"\nCriando Matriz Nome: \n{matriz_nome}")


'''
| Operador | Significado      | Exemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `==`     | Igual a          | `5 == 5` | `True`    |
| `!=`     | Diferente de     | `5 != 3` | `True`    |
| `>`      | Maior que        | `7 > 4`  | `True`    |
| `<`      | Menor que        | `2 < 5`  | `True`    |
| `>=`     | Maior ou igual a | `8 >= 8` | `True`    |
| `<=`     | Menor ou igual a | `3 <= 6` | `True`    |

'''
print("\nComparando Valores com Operadores Lógicos:")
a = 10
b = 5

print(a == b)   # False - 10 não é igual a 5
print(a != b)   # True  - 10 é diferente de 5
print(a > b)    # True  - 10 é maior que 5
print(a < b)    # False - 10 não é menor que 5
print(a >= 10)  # True  - 10 é maior ou igual a 10
print(b <= 5)   # True  - 5 é menor ou igual a 5


print("\nExemplo com números:")
x = 5
print(1 < x < 10)    # True - 5 está entre 1 e 10
print(1 < x <= 5)    # True - 5 é menor ou igual a 5
print(5 < x < 10)    # False - 5 não é menor que 5

print("\nExemplo com igualdade e diferença:")
a = 3
b = 3
c = 5

print(a == b != c)   # True - a é igual a b, e b é diferente de c
print(a == b == c)   # False - c é diferente

print("\nExemplo com maior/menor em cadeia:")
idade = 15
print(10 <= idade <= 17)  # True - idade está entre 10 e 17
print(idade > 18 <= 30)   # False - 15 não é maior que 18

print("\nExemplo com múltiplas condições:")
nota = 8
print(7 <= nota <= 10)  # True → nota está dentro da faixa de aprovação

'''
ESTRUTURA CONDICIONAL EM PYTHON

A estrutura condicional serve para tomar decisões no código 
— ou seja, executar ações diferentes dependendo de uma condição 
(se algo for verdadeiro ou falso).

if condição:
    # se for verdadeiro
else:
    # se for falso
    
if → verifica uma condição
elif → testa outra condição se a anterior for falsa
else → executa caso nenhuma condição anterior seja verdadeira

- No fim das verificações da condição, para indicar que elas 
já terminaram, deve-se usar dois pontos (:);
- Os códigos que serão executados caso as condições sejam 
verdadeiras devem ser indentados (com um recuo maior).
'''

print("\nEstrutura Condicional em Python:")
idade = 18


# → Estrutura condicional simples:
# A estrutura condicional simples faz executar um ou vários comandos
# SE a condição for verdadeira. Se a condição for falsa, a estrutura
# é finalizada sem executar os comandos.


if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


print("\nEstrutura ELIF (SENÃO SE):")
nota = 7

# → Estrutura condicional composta
# A estrutura condicional composta segue a mesma lógica da estrutura condicional simples:
# A diferença que existe na estrutura composta é que ela permite uma nova bifurcação,
#  uma nova alternativa dentro do seu código, que é executar comandos se
#  a condição for verificada como falsa.

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
else:
    print("Precisa melhorar.")


'''
Laços de Repetição (Loops)
Os laços de repetição servem para executar um 
bloco de código várias vezes, sem precisar repetir 
os comandos manualmente.

-> for — usado quando sabemos quantas vezes repetir
-> while — usado quando não sabemos quantas vezes repetir
'''

# For
# A estrutura for atua como um iterador em Python, isto é,
# um objeto que percorre itens que estão em uma sequência
# e retorna os dados desses itens de maneira sucessiva, um elemento de cada vez.

print("\n Laço FOR:")
for i in range(5):
    print("Repetição", i)


# While
# A instrução while executa repetidamente um trecho de código
# enquanto uma condição for verdadeira.

print("\n Laço WHILE:")
contador = 0
while contador < 5:
    print("Contando:", contador)
    contador += 1

# Controlando Loops com Break, Continue e Pass
# break: parar um loop;
# continue: ir para o próximo loop;
# pass: não fazer nada.

'''
break — parar um loop antes do final
O comando break interrompe o loop imediatamente, 
mesmo que a condição ainda seja verdadeira.
'''

for numero in range(1, 10):
    if numero == 5:
        print("\nParando o loop no número 5.")
        break
    print(numero)


'''
continue — ir para o próximo ciclo do loop
O continue pula o restante do código naquela 
iteração e volta para o início do loop.
'''

for numero in range(1, 6):
    if numero == 3:
        print("\nPulando o número 3.")
        continue
    print(numero)


'''
pass — não fazer nada
O pass é usado quando você precisa manter a 
estrutura do código, mas ainda não quer executar nada.
'''
for numero in range(1, 4):
    if numero == 2:
        pass  # ainda não decidi o que fazer aqui
    else:
        print(f"\nNúmero: {numero}")

