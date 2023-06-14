#Este código usa o módulo random para gerar uma senha aleatória de 12 caracteres que consiste em letras maiúsculas e minúsculas e dígitos. O Tkinter é usado para criar uma interface gráfica simples com um botão “Gerar Senha” e um rótulo “Senha” que exibe a senha gerada.
import random
import string
import tkinter as tk

def gerar_senha():
    senha = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    senha_label['text'] = f'Senha: {senha}'

janela = tk.Tk()
janela.geometry('300x200')
janela.title('Gerador de Senhas - ADALBERTO')

gerar_button = tk.Button(janela, text='Aperte aqui para Gerar Senha', command=gerar_senha, bg='blue')
gerar_button.pack()

senha_label = tk.Label(janela, text='Senha:')
senha_label.pack()