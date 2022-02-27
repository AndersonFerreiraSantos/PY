#importando tkinter
from tempfile import tempdir
from tkinter import *
from tkinter import ttk

#Cores
Cinza = "#404040" 
Preto = "#000000" 
Vermelho = "#fc0000"
Azul = "#0800ff"
Amarelo = "#fff700"
Branco = "#ffffff"

tela = Tk()
tela.title("copiar arquivo")
tela.geometry("400x400")
tela.config(bg = Preto)

#botão copiar

b_copiar = Button(tela, text="Copiar", width=20,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)

#localização botão
b_copiar.place(x=0, y = 52)

#Necessário para finalizar o codigo
tela.mainloop()