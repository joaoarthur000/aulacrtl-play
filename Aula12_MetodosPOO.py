"""
TEMA: Programação Orientada a Objetos (POO)
--------------------------------------------

Tópicos da aula:
1. Método Inicializador (__init__)
2. Métodos Getters e Setters
3. Métodos Especiais

Vamos entender como cada um funciona e ver exemplos práticos!
"""

# ================================================================
# 1️⃣ MÉTODO INICIALIZADOR (__init__)
# ================================================================

"""
O método inicializador é chamado automaticamente sempre que um novo
objeto da classe é criado. Ele serve para definir os valores iniciais
dos atributos do objeto.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    # atributo de instância
        self.idade = idade

# Criando um objeto (instância da classe Pessoa)
pessoa1 = Pessoa("Maria", 20)

print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
print()  # linha em branco para separar a saída

# ================================================================
# 2️⃣ MÉTODOS GETTERS E SETTERS
# ================================================================

"""
Os métodos **getters** e **setters** são usados para **controlar o acesso**
aos atributos de um objeto.

- Getter: serve para OBTER o valor de um atributo.
- Setter: serve para DEFINIR (ou alterar) o valor de um atributo.
Isso é útil para proteger dados e evitar alterações incorretas.
"""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular    # Atributo privado (note os dois "_")
        self.__saldo = saldo        # Atributo privado

    # Getter do saldo
    def get_saldo(self):
        return self.__saldo

    # Setter do saldo
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Saldo não pode ser negativo!")

    # Método comum
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo!")

# Criando uma conta
conta1 = ContaBancaria("João", 1000)

# Usando os getters e setters
print("Saldo inicial:", conta1.get_saldo())
conta1.depositar(500)
print("Saldo após depósito:", conta1.get_saldo())

# Tentando alterar o saldo com um valor inválido
conta1.set_saldo(-100)
print("Saldo final:", conta1.get_saldo())
print()

# ================================================================
# 3️⃣ MÉTODOS ESPECIAIS
# ================================================================

"""
Os **métodos especiais** (também chamados de *métodos mágicos*) são
aqueles que começam e terminam com dois underlines "__".  
Exemplos: __init__, __str__, __len__, __add__, etc.

Eles permitem personalizar o comportamento dos objetos em situações
específicas. Vamos ver dois exemplos:
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Método especial __str__ → define o que será mostrado quando usarmos print(objeto)
    def __str__(self):
        return f"Produto: {self.nome} - Preço: R${self.preco:.2f}"

    # Método especial __add__ → permite somar produtos (exemplo: soma dos preços)
    def __add__(self, outro_produto):
        return self.preco + outro_produto.preco

# Criando dois produtos
p1 = Produto("Mouse", 50.00)
p2 = Produto("Teclado", 120.00)

# Exibindo informações com __str__
print(p1)
print(p2)

# Usando o método especial __add__
total = p1 + p2
print(f"Soma dos preços: R${total:.2f}")
print()

# ================================================================
# 🧩 DESAFIO PARA O ALUNO
# ================================================================
"""
Crie uma classe chamada Aluno com os seguintes requisitos:

- Atributos: nome, nota.
- Método inicializador (__init__) que receba os valores ao criar o objeto.
- Métodos getters e setters para a nota.
- Um método especial __str__ para mostrar o nome e a nota do aluno.
Depois, crie dois alunos e exiba suas informações no terminal.
"""
