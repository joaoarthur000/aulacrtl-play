"""
TEMA: Programação Orientada a Objetos (POO)
--------------------------------------------

A Programação Orientada a Objetos (POO) é um paradigma de programação
baseado na criação de **classes** que representam **objetos** do mundo real.
Esses objetos possuem **atributos** (características) e **métodos** (ações).

Conceitos principais:
- Classe: é o modelo ou molde que define como os objetos serão criados.
- Objeto: é uma instância (ou cópia) de uma classe.
- Atributo: é uma variável que guarda informações sobre o objeto.
- Método: é uma função que define um comportamento do objeto.
"""

# Exemplo prático: Classe "Carro"
# -------------------------------

class Carro:
    """
    Classe que representa um carro.
    """

    # ATRIBUTOS
    # São as características que cada carro terá.
    def __init__(self, marca, modelo, cor):
        self.marca = marca      # Atributo de instância
        self.modelo = modelo
        self.cor = cor
        self.ligado = False     # Estado inicial do carro

    # MÉTODOS
    # São as ações ou comportamentos do carro.

    def ligar(self):
        """Liga o carro."""
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} está ligado.")
        else:
            print(f"O {self.modelo} já está ligado!")

    def desligar(self):
        """Desliga o carro."""
        if self.ligado:
            self.ligado = False
            print(f"O {self.modelo} foi desligado.")
        else:
            print(f"O {self.modelo} já está desligado!")

    def acelerar(self):
        """Faz o carro acelerar."""
        if self.ligado:
            print(f"O {self.modelo} está acelerando! 💨")
        else:
            print(f"Você precisa ligar o {self.modelo} antes de acelerar.")

# Criando objetos (instâncias da classe)
# --------------------------------------

carro1 = Carro("Toyota", "Corolla", "Prata")
carro2 = Carro("Fiat", "Uno", "Vermelho")

# Acessando atributos
print("Marca:", carro1.marca)
print("Modelo:", carro1.modelo)
print("Cor:", carro1.cor)
print()

# Chamando métodos
carro1.ligar()
carro1.acelerar()
carro1.desligar()
print()

carro2.acelerar()  # Tentando acelerar com o carro desligado
carro2.ligar()
carro2.acelerar()
