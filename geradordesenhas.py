'''Este código usa as bibliotecas random e string para gerar senhas aleatórias e seguras.
Ele pede ao usuário que digite o tamanho da senha que deseja e, em seguida, gera uma senha
aleatória com base no tamanho fornecido. A senha gerada inclui letras maiúsculas e minúsculas,
números e caracteres especiais.'''

import random
import string

def gerar_senha(tamanho_da_senha):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_segura = ''.join(random.choice(caracteres) for i in range(tamanho_da_senha))
    return senha_segura

tamanho_da_senha = int(input("Digite o tamanho da senha que você deseja: "))
print("Sua senha segura é:", gerar_senha(tamanho_da_senha))