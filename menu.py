from functools import partial
import tkinter as tk   
from tkinter import ttk
from tkinter.messagebox import showinfo
from root import verifica_cpf
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

    return None

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

def cmd(box_cpf,mascara):
    box_cpf.config(text = gerar_cpf_mascara(mascara))

def menu():
    global root
    root = tk.Tk()

    root.title("Verificador de CPF")    

    root.geometry(f"{largura_janela}x{altura_janela}")

    botao_verificar = tk.Button(root, text="Verificar CPF valido", command=clique_verificar)
    botao_verificar.pack()


    botao_gerar_cpf= tk.Button(root,text="Gerar CPF",command=clique_gerar_cpf)
    botao_gerar_cpf.pack()

    
    botao_mascara= tk.Button(root,text="Acrescentar mascara",command=clique_mascara)
    botao_mascara.pack()

    botao_dv = tk.Button(root, text= "Acrescentar digito Verificador", command=clique_dv)
    botao_dv.pack()

    root.mainloop()

def verifica_cpf():

    global root
    root = tk.Tk()

    root.title("Verificador de CPF")

    root.geometry(f"{largura_janela}x{altura_janela}")

    cpf = tk.StringVar()

    caixa_texto = tk.Entry(root, textvariable=cpf)
    caixa_texto.pack()  

    botao = tk.Button(root, text='Verificar CPF', command= partial(botao_verificador_cpf, cpf))
    botao.pack()

    root.mainloop()

def gerar_cpf():
    global root
    root = tk.Tk()

    root.title("Verificador de CPF")

    root.geometry(f"{largura_janela}x{altura_janela}")
 
    mascara = tk.BooleanVar()

    check_mascara = tk.Checkbutton(root, text="Gerar mascara", variable= mascara, onvalue= True, offvalue= False)
    check_mascara.pack()

    box_cpf = tk.Label(root, bg= "white", width= 30,text="")
    box_cpf.pack()

    botao_gerar_cpf = tk.Button(root, text= "Gerar CPF", command= partial(cmd,box_cpf,mascara))
    botao_gerar_cpf.pack()

    
    root.mainloop()

def verificar_dv():
    global root
    root = tk.Tk()

    root.title("Verificador de CPF")
    root.geometry(f"{largura_janela}x{altura_janela}")

    root.mainloop()

if __name__ == "__main__":
    menu() 