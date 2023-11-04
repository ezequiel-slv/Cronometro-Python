from tkinter import *
import tkinter

cor1 = "#0a0a0a" #Black
cor2 = "#fafcff" #White
cor3 = "#21c25c" #green
cor4 = "#eb463b" #red
cor5 = "#dedcdc" #gray
cor6 = "#3080f0" #blue

janela = Tk()
janela.title("")
janela.geometry('300x200')
janela.config(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

global tempo 
global rodar
global contador
global limitador

limitador = 59

tempo = "00:00:00"
rodar = False
contador = -5

def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        if contador <= -1:
            inicio = 'Começamdo em ' +str(contador)
            Label_tempo['text'] = inicio
            Label_tempo['font'] = 'Arial 10' 

        else:
            Label_tempo['font'] = 'Times 50 bold'

            temporaria = str(tempo)  
            h,m,s = map(int, temporaria.split(":")) 
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s>=limitador):
                contador = 0
                m+=1

            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            temporaria = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            Label_tempo['text'] = temporaria
            tempo = temporaria

        Label_tempo.after(1000,iniciar)
        contador +=1 

def start():
    global rodar 
    rodar = True
    iniciar()

def pausar():
    global rodar
    rodar = False

def reiniciar():
    global tempo
    global contador
    contador = 0
    tempo = "00:00:00"
    Label_tempo['text'] = tempo


Label_app = Label(janela, text="Cronômetro", font=('Arial 10'), bg=cor1, fg=cor2)
Label_app.place(x=20, y=5)

Label_tempo = Label(janela, text= tempo, font=('Times 50 bold'), bg=cor1, fg=cor6)
Label_tempo.place(x=20, y=25)
botao_iniciar = Button(janela, command=start, text="Iniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief= 'raised')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, command=pausar, text="Pausar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief= 'raised')
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, command=reiniciar, text="Reiniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief= 'raised')
botao_reiniciar.place(x=190, y=130)

janela.mainloop()
