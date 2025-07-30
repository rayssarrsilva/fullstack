from diagnostico import (
    verificar_funcionamento_impressora,
    verificar_impressao,
    verificar_visor
) #boas praticas de import 

def main():
    print("Iniciando diagnostico de funcionamento da impressora...")
    verificar_funcionamento_impressora()

    print("Iniciando diagnostico de papeis na impressora...")
    verificar_impressao()

    print("Iniciando diagnostico de funcionamento do visor da impressora...")
    verificar_visor()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro inesperado: {e}")

#python -m desafio.principal (trata a pasta desafio como modulo)