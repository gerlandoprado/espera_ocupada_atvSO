import threading
import time

bloqueio = False  # Variável compartilhada para exclusão mútua
file = "arquivo.txt"  # Arquivo compartilhado

# Função do processo que escreve no arquivo
def escreve():

    global bloqueio  # Declaração da variável bloqueio como global

    while True:
        while bloqueio:
            # Espera ocupada
            print("Espera: Escreve")
            time.sleep(1)
        
        # Seção crítica
        bloqueio = True  # Bloqueia o acesso de outros processos
        with open(file, "a") as f:
            f.write(f"Processo de escrita escreveu no arquivo\n")
        
        time.sleep(1)
        print("Escreveu")

        bloqueio = False  # Libera o acesso para outros processos
        
        
        # Seção não crítica
        # ...

# Função do processo que lê o arquivo
def leitura():
    
    global bloqueio  # Declaração da variável bloqueio como global

    while True:
        while bloqueio:
            # Espera ocupada
            print("Espera: Leitura")
            time.sleep(1)
        
        # Seção crítica
        bloqueio = True  # Bloqueia o acesso de outros processos
        with open(file, "r") as f:
            content = f.read()
            print(f"Processo de leitura leu o arquivo: {content}")

        time.sleep(1)

        bloqueio = False  # Libera o acesso para outros processos
        
        # Seção não crítica
        # ...

# Criação das threads para os processos de escrita e leitura
thread_escreve = threading.Thread(target=escreve)
thread_ler = threading.Thread(target=leitura)

# Inicia a execução das threads
thread_escreve.start()
thread_ler.start()

# Aguarda o término das threads
thread_escreve.join()
thread_ler.join()