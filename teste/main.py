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

janela = Tk()
janela.title("Cal cú")

#Valor de largura e comprimento
janela.geometry("235x318")

#Alterar cor background
janela.config(bg=Preto)

#frame do display, definindo tamanho
frame_display = Frame(janela, width=235, height=50, bg=Cinza)
frame_display.grid(row=0, column=0)

#frame de botões
frame_teclado = Frame(janela, width=235, height=268, bg=Vermelho)
frame_teclado.grid(row=1, column=0)

janela.iconbitmap("img/cara.ico")
valores = ''


temp = 0

#Back - function 

def calc(event):
    global valores
    valores = valores + str(event)

    display.set(valores)

def calcular():
    global temp
    resultado = eval(valores)
    
    if temp == 0:
        display.set("Valor é: " +str(resultado) )
        temp = temp +1
    elif temp == 1:
        display.set(str(resultado) +" to cansada")
        temp = temp +1
    elif temp == 2:
        display.set(str(resultado) +" Não quero mais")
        temp = temp +1
    elif temp == 3:
        display.set(str(resultado) +" para pf")
        temp = temp +1
    elif temp == 4:
        display.set(str(resultado) +" serio?")
        temp = temp +1
    elif temp == 5:
        display.set(str(resultado) +" vai se ferrar")
        temp = temp +1
    elif temp == 6:
        display.set("foda-se, to de ferias")
        temp = temp +1
    elif temp == 6:
        display.set("Ja falei...")
        temp = temp +1
    elif temp == 10:
        display.set("Q chato!!!!!!!!!")
        temp = temp +1
    else:
        display.set("Ferias!!!!")
        temp = temp +1

def clear():
    global valores
    valores = ""
    display.set("")


    

#Criando label

display = StringVar()
app_label = Label(frame_display, textvariable=display, width= 16, height = 2, padx= 7, relief=FLAT, anchor="e", font=('Ivy 17 bold'), justify=RIGHT, bg= Preto, fg= Vermelho )
app_label.place(x = 0, y= 0)


#Botões
b_C = Button(frame_teclado,command = clear, text="C", width=11,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_C.place(x=0, y = 0)

b_por = Button(frame_teclado, command = lambda: calc('%'), text="%", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_por.place(x=118, y = 0)

b_div = Button(frame_teclado, command = lambda: calc('/'),  text="/", width=5,  height=2, bg=Amarelo, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_div.place(x=177, y = 0)



b_7 = Button(frame_teclado, command = lambda: calc('7'), text="7", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_7.place(x=0, y = 52)

b_8 = Button(frame_teclado, command = lambda: calc('8'), text="8", width=5,  height=2, bg=Azul,fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_8.place(x=60, y = 52)

b_9 = Button(frame_teclado,command = lambda: calc('9'), text="9", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_9.place(x=118, y = 52)

b_ast = Button(frame_teclado, command = lambda: calc('*'), text="*", width=5,  height=2, bg=Amarelo, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_ast.place(x=177, y = 52)



b_4 = Button(frame_teclado, command = lambda: calc('5'), text="4", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_4.place(x=0, y = 104)

b_5 = Button(frame_teclado, command = lambda: calc('5'), text="5", width=5,  height=2, bg=Azul,fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_5.place(x=60, y = 104)

b_6 = Button(frame_teclado, command = lambda: calc('6'), text="6", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_6.place(x=118, y = 104)

b_sub = Button(frame_teclado, command = lambda: calc('-'), text="-", width=5,  height=2, bg=Amarelo, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_sub.place(x=177, y = 104)



b_1 = Button(frame_teclado, command = lambda: calc('1'),  text="1", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_1.place(x=0, y = 156)

b_2 = Button(frame_teclado,command = lambda: calc('2'),  text="2", width=5,  height=2, bg=Azul,fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_2.place(x=60, y = 156)

b_3 = Button(frame_teclado, command = lambda: calc('3'),  text="3", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_3.place(x=118, y = 156)

b_som = Button(frame_teclado, command = lambda: calc('+'), text="+", width=5,  height=2, bg=Amarelo, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_som.place(x=177, y = 156)

b_0 = Button(frame_teclado, command = lambda: calc('0'), text="0", width=11,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_0.place(x=0, y = 208)

b_pont = Button(frame_teclado, command = lambda: calc('.'),  text=".", width=5,  height=2, bg=Azul, fg= Branco, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_pont.place(x=118, y = 208)

b_ig = Button(frame_teclado, command = calcular, text="=", width=5,  height=2, bg=Amarelo, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
b_ig.place(x=177, y = 208)



janela.mainloop()

