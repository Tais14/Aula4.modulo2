import tkinter as tk

def fazer_login():
    nome = entry_nome.get()
    login = entry_login.get()
    senha = entry_senha.get()

    # Verifica as credenciais
    if login == "usuario" and senha == "senha123":
        label_resultado["text"] = f"Bem-vindo, {nome}! Login realizado com sucesso!"
    else:
        label_resultado["text"] = "Credenciais inválidas. Tente novamente."

# Cria a janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry()

# Cria os widgets
label_nome = tk.Label(janela, text="Nome:")
label_login = tk.Label(janela, text="Login:")
label_senha = tk.Label(janela, text="Senha:")
entry_nome = tk.Entry(janela)
entry_login = tk.Entry(janela)
entry_senha = tk.Entry(janela, show="*")
button_login = tk.Button(janela, text="Login", command=fazer_login)
label_resultado = tk.Label(janela, text="")

# Posiciona os widgets usando o grid
label_nome.grid(row=0, column=0, sticky=tk.E)
label_login.grid(row=1, column=0, sticky=tk.E)
label_senha.grid(row=2, column=0, sticky=tk.E)
entry_nome.grid(row=0, column=1)
entry_login.grid(row=1, column=1)
entry_senha.grid(row=2, column=1)
button_login.grid(row=3, columnspan=2, pady=10)
label_resultado.grid(row=4, columnspan=2)

# Inicia o loop principal da janela
janela.mainloop()