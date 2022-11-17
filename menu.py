from functools import partial
import tkinter as tk   
from tkinter import ttk
from tkinter.messagebox import showinfo
from verificador_cpf import *

largura_janela = 426
altura_janela = 240

def clique_dv():
    global root
    root.destroy()
    verificar_dv()

def clique_verificar():
    global root
    root.destroy()
    verifica_cpf()


def clique_gerar_cpf():
    root.destroy()
    gerar_cpf()

def clique_mascara():
    root.destroy()
    colocar_mascara()


def clique_voltar_menu():
    root.destroy()
    menu()

def botao_verificador_cpf(cpf):
    cpf = cpf.get()
    if valida_cpf(cpf) == True:
        showinfo(
            title= "Verificador de CPF",
            message=f"CPF {adicionar_mascara(cpf)} Valido"
        )
    else: 
        showinfo(title="Verificador de CPF", message="CPF Invalido")

def gerar_cpf_mascara(mascara):
    if mascara.get() == True:
        cpf = gerador_cpf_aleatorio()
        cpf = adicionar_mascara(cpf=cpf)
        return cpf
    else :
        cpf = gerador_cpf_aleatorio()
        return cpf

def retorno_cpf_mascara(box_mascara, cpf):
    box_mascara.config(text= adicionar_mascara(cpf.get()))


def cmd(box_cpf,mascara):
    box_cpf.config(text = gerar_cpf_mascara(mascara))

def menu():
    global root
    root = tk.Tk()

    root.title("Verificador de CPF")    
    root.resizable(0,0)
    root.geometry(f"{largura_janela}x{altura_janela}")

    botao_verificar = tk.Button(root, text="Verificar CPF valido", command=clique_verificar)
    botao_verificar.place(x=50, y =50)

    botao_gerar_cpf= tk.Button(root,text="Gerar CPF",command=clique_gerar_cpf)
    botao_gerar_cpf.place(x=75,y=150)

    
    botao_mascara= tk.Button(root,text="Acrescentar mascara",command=clique_mascara)
    botao_mascara.place(x=226,y=    50)

    botao_dv = tk.Button(root, text= "Acrescentar digito Verificador", command=clique_dv)
    botao_dv.place(x=206,y=150)

    root.mainloop()

def verifica_cpf():

    global root
    root = tk.Tk()

    root.title("Verificador de CPF")
    root.resizable(0,0)
    root.geometry(f"{largura_janela}x{altura_janela}")

    cpf = tk.StringVar()

    caixa_texto = tk.Entry(root, textvariable=cpf)
    caixa_texto.place(x=138,y=50)  

    botao = tk.Button(root, text='Verificar CPF', command= partial(botao_verificador_cpf, cpf))
    botao.place(x=163,y=80)

    botao_voltar = tk.Button(root, text= "Voltar", command= clique_voltar_menu )
    botao_voltar.place(x=183,y=200)
    root.mainloop()

def gerar_cpf():
    global root
    root = tk.Tk()
    root.resizable(0,0)
    root.title("Verificador de CPF")

    root.geometry(f"{largura_janela}x{altura_janela}")
 
    mascara = tk.BooleanVar()

    check_mascara = tk.Checkbutton(root, text="Gerar mascara", variable= mascara, onvalue= True, offvalue= False)
    check_mascara.place(x=153,y=80)

    box_cpf = tk.Label(root, bg= "white", width= 30,text="")
    box_cpf.place(x=108,y=50)

    botao_gerar_cpf = tk.Button(root, text= "Gerar CPF", command= partial(cmd,box_cpf,mascara))
    botao_gerar_cpf.place(x=168,y=110)

    botao_voltar = tk.Button(root, text= "Voltar", command= clique_voltar_menu )
    botao_voltar.place(x=183,y=200)

    
    root.mainloop()

def verificar_dv():
    global root
    root = tk.Tk()
    root.resizable(0,0)
    root.title("Verificador de CPF")
    root.geometry(f"{largura_janela}x{altura_janela}")
    botao_voltar = tk.Button(root, text= "Voltar", command= clique_voltar_menu )
    botao_voltar.place(x=183,y=200)

    root.mainloop()

def colocar_mascara():
    global root
    root = tk.Tk()
    root.resizable(0,0)
    root.title("Verificador de CPF")
    root.geometry(f"{largura_janela}x{altura_janela}")
    botao_voltar = tk.Button(root, text= "Voltar", command= clique_voltar_menu )
    botao_voltar.place(x=183,y=200)

    cpf = tk.StringVar()

    caixa_texto = tk.Entry(root, textvariable=cpf)
    caixa_texto.place(x=138,  y=50) 

    box_mascara = tk.Label(root, bg="white", width=30,text="")
    box_mascara.place(x=108,y=80)

    botao_mascara = tk.Button(root, text= "Acrescentar Mascara", command= partial(retorno_cpf_mascara,box_mascara,cpf)) 
    botao_mascara.place(x=135,y=110)

if __name__ == "__main__":
    menu() 