def boas_vindas(nome):
    return f"Olá, {nome}! Tudo bem com você?"

if __name__ == "__main__": #python -m helpers.saudacao (garante que o código só será executado se o arquivo for rodado diretamente)
    nome = "Rayssa"
    print(boas_vindas(nome))
