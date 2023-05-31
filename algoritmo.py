import threading
import time
import os

bloqueio = False

def escreve():

    global bloqueio

    while True:
        while bloqueio:
            # Espera ocupada
            time.sleep(1)

        bloqueio = True 

        texto = input("Escreva: ")
        with open(arquivo, "a") as f:
            f.write(f"> {texto}\n")

        bloqueio = False
        time.sleep(1)


def leitura():

    global bloqueio

    while True:
        while bloqueio:
            # Espera ocupada
            time.sleep(1)

        bloqueio = True

        os.system('cls')
        with open(arquivo, "r") as f:
            conteudo = f.read()
            print(f"Lista atual: \n{conteudo}")

        bloqueio = False
        time.sleep(1)


print("\nCriando uma lista...")
arquivo = input("Digite o nome da sua lista sem espaços e acentos: ")
arquivo = f"{arquivo}.txt"

thread_escreve = threading.Thread(target=escreve)
thread_ler = threading.Thread(target=leitura)

thread_escreve.start()
thread_ler.start()

thread_escreve.join()
thread_ler.join()