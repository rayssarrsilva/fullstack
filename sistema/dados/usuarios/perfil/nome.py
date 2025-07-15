from dados.usuarios.conta.email import pegar_email

def pegar_nome():
    return "Rayssa"

if __name__ == "__main__":
    nome = pegar_nome()
    email = pegar_email()
    print(boas_vindas(nome))
    print(f"Email vindo de nome.py: {email}")

