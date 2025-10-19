import tkinter as tk
from tkinter import messagebox

# 1. Função para processar as respostas e as classificações
def verificar_resultado():
    respostas_positivas = sum(var.get() == 1 for var in respostas)
    
    if respostas_positivas == 2:
        classificacao = "Suspeita"
    elif 3 <= respostas_positivas <= 4:
        classificacao = "Cúmplice"
    elif respostas_positivas == 5:
        classificacao = "Assassino"
    else:
        classificacao = "Inocente"
    
    messagebox.showinfo("Resultado", f"Classificação: {classificacao}")

# 2. Configuração da janela principal, interface
janela = tk.Tk()
janela.title("Interrogatório - Caso Criminal")
janela.geometry("450x420")
janela.config(bg="#0b3d0b")  # verde escuro de fundo

# Cores principais
cor_fundo = "#0b3d0b"      # verde escuro
cor_texto = "white"        # texto branco
cor_botao = "#145214"      # verde médio
cor_hover = "#1e7a1e"      # verde mais claro no hover

titulo = tk.Label(janela, text="Responda as Perguntas Abaixo:", 
                  font=("Arial", 15, "bold"), bg=cor_fundo, fg=cor_texto)
titulo.pack(pady=15)

# Lista de perguntas
perguntas = [
    "Telefonou para a Vítima?",
    "Esteve no Local do Crime?",
    "Mora Perto da Vítima?",
    "Devia para a Vítima?",
    "Já Trabalhou com a Vítima?"
]

respostas = []

# 3. Criação dos botões de opção:
for pergunta in perguntas:
    frame = tk.Frame(janela, bg=cor_fundo)
    frame.pack(anchor="w", padx=25, pady=8)
    
    label = tk.Label(frame, text=pergunta, font=("Arial", 12, "bold"), bg=cor_fundo, fg=cor_texto)
    label.pack(side="left", padx=5)
    
    var = tk.IntVar()
    respostas.append(var)
    
    tk.Radiobutton(frame, text="Sim", variable=var, value=1, 
                   bg=cor_fundo, fg=cor_texto, selectcolor="#1b5e20",
                   activebackground=cor_fundo, activeforeground=cor_texto).pack(side="left", padx=10)
    tk.Radiobutton(frame, text="Não", variable=var, value=0, 
                   bg=cor_fundo, fg=cor_texto, selectcolor="#1b5e20",
                   activebackground=cor_fundo, activeforeground=cor_texto).pack(side="left")

# 4. Botão com efeito hover
def on_enter(e):
    botao.config(bg=cor_hover)

def on_leave(e):
    botao.config(bg=cor_botao)

botao = tk.Button(janela, text="Verificar Classificação", command=verificar_resultado,
                  bg=cor_botao, fg=cor_texto, font=("Arial", 12, "bold"), width=25, relief="raised", bd=3)
botao.pack(pady=25)

botao.bind("<Enter>", on_enter)
botao.bind("<Leave>", on_leave)

janela.mainloop()
