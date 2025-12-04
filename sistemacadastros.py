# ===============================
# SISTEMA DE CADASTRO BÁSICO
# ===============================

import tkinter as tk
from tkinter import messagebox

# -------------------------------
# CLASSE PRINCIPAL DO SISTEMA
# -------------------------------
class Cadastro:
    """
    Esta classe é responsável por armazenar e gerenciar
    todos os cadastros realizados no sistema.
    """

    def __init__(self):
        # Lista onde todos os cadastros serão guardados
        self.lista_cadastros = []

    def adicionar(self, nome, idade, email):
        """
        Adiciona um novo cadastro na lista.
        Antes disso, verifica se os campos estão preenchidos.
        """

        # Verifica se algum campo está vazio
        if nome == "" or idade == "" or email == "":
            return "Preencha todos os campos!"
        else:
            # Insere um dicionário com os dados da pessoa
            self.lista_cadastros.append({
                "nome": nome,
                "idade": idade,
                "email": email
            })
            return "Cadastro realizado com sucesso!"

    def listar(self):
        """
        Retorna uma string formatada com todos os cadastros.
        Se estiver vazia, informa que não há nada na lista.
        """

        if not self.lista_cadastros:
            return "Nenhum cadastro encontrado."

        # Texto inicial da lista
        resultado = "=== Lista de Cadastros ===\n"

        # Percorre todos os cadastros e concatena ao texto
        for pessoa in self.lista_cadastros:
            resultado += (
                f"Nome: {pessoa['nome']} | "
                f"Idade: {pessoa['idade']} | "
                f"Email: {pessoa['email']}\n"
            )

        return resultado


# -------------------------------
# INTERFACE GRÁFICA (Tkinter)
# -------------------------------

# Instância da classe principal
sistema = Cadastro()

# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("400x400")
janela.config(bg="#e6f2ff")  # Cor de fundo

# -------------------------------
# TÍTULO DA TELA
# -------------------------------
titulo = tk.Label(
    janela,
    text="Cadastro de Pessoas",
    font=("Arial", 16, "bold"),
    bg="#e6f2ff"
)
# pady = espaçamento vertical
# padx = espaçamento horizontal
titulo.pack(pady=10)

# -------------------------------
# CAMPOS DE ENTRADA
# -------------------------------

# Campo Nome
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

# Campo Idade
tk.Label(janela, text="Idade:", bg="#e6f2ff").pack()
entrada_idade = tk.Entry(janela, width=40)
entrada_idade.pack(pady=5)

# Campo Email
tk.Label(janela, text="Email:", bg="#e6f2ff").pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)


# -------------------------------
# FUNÇÕES CONECTADAS AOS BOTÕES
# -------------------------------

def cadastrar():
    """
    Pega os dados digitados nos campos, envia para o método adicionar(),
    mostra o resultado na tela e limpa os campos.
    """

    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()

    # Chama a função da classe e recebe uma mensagem
    mensagem = sistema.adicionar(nome, idade, email)

    # Exibe a mensagem em uma caixa de diálogo
    messagebox.showinfo("Resultado", mensagem)

    # Limpa os campos após o cadastro
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_email.delete(0, tk.END)


def mostrar_lista():
    """
    Exibe em uma caixa de diálogo todos os cadastros realizados.
    """

    resultado = sistema.listar()
    messagebox.showinfo("Cadastros", resultado)


# -------------------------------
# BOTÕES
# -------------------------------

# Botão cadastrar
botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar",
    bg="#4CAF50",   # Verde
    fg="white",
    width=15,
    command=cadastrar
)
botao_cadastrar.pack(pady=10)

# Botão listar cadastros
botao_listar = tk.Button(
    janela,
    text="Listar Cadastros",
    bg="#2196F3",  # Azul
    fg="white",
    width=15,
    command=mostrar_lista
)
botao_listar.pack(pady=5)

# -------------------------------
# RODAPÉ
# -------------------------------
rodape = tk.Label(
    janela,
    text="Desenvolvido em aula - Ctrl+Play",
    bg="#e6f2ff",
    fg="gray"
)
rodape.pack(side="bottom", pady=10)

# -------------------------------
# INICIAR O PROGRAMA
# -------------------------------
janela.mainloop()
