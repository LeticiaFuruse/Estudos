import tkinter as tk

def cadastrar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()

    #adicionar código para salvar os dados do cliente em um banco de dados, arquivo, etc.(ira aprecer no terminal)
    print("Cliente cadastrado:")
    print("Nome:", nome)
    print("Email:", email)

# Criando a janela
janela = tk.Tk()
janela.title("Cadastro de Cliente")



# Criando rótulos e campos de entrada para nome e e-mail
tk.Label(janela, text="Nome:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="E-mail:").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1)

# Botão para cadastrar cliente
btn_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_cliente)
btn_cadastrar.grid(row=2, column=0, columnspan=2, pady=10)

#botao salvar
btn_salvar = tk.Button(janela, text="Salvar", command=lambda: cadastrar_cliente())
btn_salvar.grid(row=2, column=1)


# Rodando o loop principal da aplicação
janela.mainloop()
