from tkinter import * 
from tkinter.ttk import * 
import tkinter as tk

# Width – Largura do widget;
# Height – Altura do widget;
# Text – Texto a ser exibido no widget;
# Font – Família da fonte do texto;
# Fg – Cor do texto do widget;
# Bg – Cor de fundo do widget;
# Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).



#criação da janela
janela = Tk()
janela.geometry('300x180') 
janela.title('Botoes') #nome da janela

# ESTILIZAÇÃO DE TODOS OS BOTOES 
style = Style() 

# Irá adicionar estilo a todos os botões disponíveis
# mesmo que não estejamos passando estilo
# para cada widget de botão. 

style.configure('TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'red')

# botão 1 
btn1 = Button(janela, text = 'Sair !',  style = 'TButton', command = janela.destroy) 

btn1.grid(row = 0, column = 3, padx = 100) 

# botão 2 
btn2 = Button(janela, text = 'Clique aqui !', command = None) 
btn2.grid(row = 1, column = 3, pady = 10, padx = 100) 


# janela fechar ao clicar no x 
janela.mainloop()