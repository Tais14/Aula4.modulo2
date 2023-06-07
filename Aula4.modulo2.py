from tkinter import *

def clique():
    texto.configure(text="Ligado")

janela = Tk()
janela.title("Minha janela")
#janela.iconbitmap("camimho/para/o/arquivo.ico")

janela.geometry("400x300")  #Largura x Altura
janela.resizable(True, True)  #permitir redimensionamento(true) 

texto = Label(janela, text = "Desligado")
texto.pack()

botao = Button(janela, text = "Ligar" , command=clique)
botao.pack()
janela.mainloop()


