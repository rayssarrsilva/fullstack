#entrada de dados do sistema de Diagnóstico de Impressora com Falha
import logging

logging.basicConfig(level=logging.DEBUG)

def verificar_funcionamento_impressora():
    while True:
        try:
            impressora_ligada = str(input("A impressora está ligada (sim/nao)? ")).strip()
            print(f"DEBUG: valor inserido na entrada da funcao 'verificar_funcionamento_impressora': {impressora_ligada}")
            if impressora_ligada.lower() == "sim":
                logging.debug(f"entrando no bloco impressora_ligada.lower() == sim")
                print("A impressora está funcionando")
                break
            elif impressora_ligada.lower() == "nao":
                logging.debug(f"entrando no bloco impressora_ligada.lower() == nao")
                print("Impressora desligada. Verifique o cabo de energia")
                break
            else:
                raise ValueError
        except ValueError as e:
            logging.debug(f"erro encontrado {e}")
            logging.error("Você deve digitar sim ou nao")

def verificar_impressao():
    while True:
        try:
            papel_suficiente = input("Há papel suficiente na impresssora(sim/nao)? ").strip()
            print(f"DEBUG: valor inserido na entrada da funcao 'verificar_impressao': {papel_suficiente}")
            if papel_suficiente.lower(): #verifica se foi inserido algo (todo retorno de input é str)
                if papel_suficiente == "nao":
                    logging.debug(f"entrando no papel_suficiente == nao")
                    print("Coloque mais papel na impressora, para realizar impressões")
                    break
                elif papel_suficiente == "sim":
                    logging.debug(f"entrando no bloco papel_suficiente == sim")
                    print("A impressora está pronta para imprimir")
                    break
            else:
                raise ValueError
        except ValueError as e :
            logging.debug(f"erro encontrado {e}")
            logging.error("Você deve digitar sim ou nao")
    print("quantidade de papeis verificada")

def verificar_visor():
    while True:
        try:
            visor_erro = str(input("O visor mostra erro (sim/nao)? ")).strip()
            logging.debug(f"valor inserido na entrada da funcao 'verificar_visor': {visor_erro}")
            if visor_erro.lower() in ["sim", "nao"]:
                if visor_erro == "sim":
                    logging.debug(f"entrando no bloco visor_erro == sim")
                    print("Há erro no visor. O chamado tecnico foi efetivado para o concerto do visor, aguarde....")
                elif visor_erro == "nao":
                    logging.debug(f"entrando no bloco visor_erro == nao")
                    print("O visor da impressora está funcionando corretamente")
                break
            else:
                raise ValueError
        except ValueError as e:
            logging.debug(f"erro encontrado {e}")
            logging.error("Você deve digitar sim ou nao")

if __name__ == "__main__": ## Só roda se executar direto, não ao importar
    verificar_visor()
    verificar_funcionamento_impressora()
    verificar_impressao()
