import tkinter as tk
from tkinter import messagebox

def popup():
    messagebox.showinfo("Janela Pop-up", "Olá! Esta é uma janela pop-up.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo de Pop-up")

# Botão para exibir a janela pop-up
btn_popup = tk.Button(janela, text="Clique Aqui", command=popup)
btn_popup.pack(pady=20)

# Rodando o loop principal da aplicação
janela.mainloop()
