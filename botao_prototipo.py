import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('a')
janela.state('zoomed')#Tela cheia

janela.columnconfigure(1,minsize=-150)
janela.rowconfigure(0,minsize=40)

mensagem1 = tk.Label(bg='#C0C0C0',height=6,width=230)
mensagem1.grid(row=0,columnspan=10,sticky='NSEW')

colunacor = tk.Label(bg='#C0C0C0',height=6,width=230)
colunacor.grid(row=1,columnspan=10)

botao = tk.Button(text='Login',width=15,height=3)
botao.grid(row=1,column=4)
botao1 = tk.Button(text='Catalogo',width=15,height=3)
botao1.grid(row=1,column=5)
botao2 = tk.Button(text='Carrinho',width=15,height=3)
botao2.grid(row=1,column=6)

janela.mainloop()