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
janela.title("Definição do Tamanho da Janela")

# Definindo o tamanho da janela
largura = 600
altura = 400
janela.geometry(f"{largura}x{altura}")



# Criando rótulos e campos de entrada para nome e e-mail
tk.Label(janela, text="Nome:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(janela, width=50)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="E-mail:").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(janela, width=50)
entry_email.grid(row=1, column=1)

# Botão para cadastrar cliente
btn_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_cliente, width=30 )

 
btn_cadastrar.grid(row=2, column=0, columnspan=2, pady=20)

#botao salvar
btn_salvar = tk.Button(janela, text="Salvar", command=lambda: cadastrar_cliente(), width=30)
btn_salvar.grid(row=2, column=1, padx=20)

# Rodando o loop principal da aplicação
janela.mainloop()
