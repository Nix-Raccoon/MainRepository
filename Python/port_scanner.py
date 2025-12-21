import socket
import sys
import time
import concurrent.futures
from datetime import datetime

# CONFIGURAZIONE TURBO
TIMEOUT = 0.5   # Va bene per internet, per localhost potresti scendere a 0.1
MAX_THREADS = 500 # Alzato a 500 per smaltire la coda più in fretta

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT) 
        result = s.connect_ex((target, port))
        s.close()
        if result == 0:
            return port
    except:
        return None
    return None

def update_progress(current, total):
    """Crea una barra di caricamento testuale"""
    percent = 100 * (current / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    # \r riporta il cursore a inizio riga senza andare a capo
    sys.stdout.write(f"\r|{bar}| {percent:.2f}% Completo")
    sys.stdout.flush()

def execute_scan():
    slow_print('\n' + '-' * 50 + '\n')
    target_input = input('Inserisci l\'indirizzo IP target: ')
    
    try:
        target_ip = socket.gethostbyname(target_input)
    except socket.gaierror:
        slow_print("Errore: Impossibile risolvere l'hostname.")
        return

    try:
        min_port = int(input('Inserisci il valore minimo di porta: '))
        max_port = int(input('Inserisci il valore massimo di porta: '))
    except ValueError:
        slow_print("Errore: Inserisci solo numeri interi.")
        return

    slow_print('\n' + '-' * 50 + '\n')
    slow_print(f"Target: {target_ip} | Threads: {MAX_THREADS} | Timeout: {TIMEOUT}s")
    slow_print(f"Inizio scansione: {datetime.now()}")
    slow_print('\n' + '-' * 50 + '\n')

    open_ports = []
    ports = list(range(min_port, max_port + 1)) # Convertiamo in lista per sapere la lunghezza totale
    total_ports = len(ports)
    completed_ports = 0

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            future_to_port = {executor.submit(scan_port, target_ip, port): port for port in ports}
            
            for future in concurrent.futures.as_completed(future_to_port):
                port_result = future.result()
                
                # Aggiorniamo il progresso INDIPENDENTEMENTE dal risultato
                completed_ports += 1
                if completed_ports % 100 == 0 or completed_ports == total_ports: # Aggiorna ogni 100 porte per non rallentare troppo
                     update_progress(completed_ports, total_ports)

                if port_result is not None:
                    open_ports.append(port_result)

        print() # Va a capo dopo la barra di caricamento
        print_table(open_ports)

    except KeyboardInterrupt:
        slow_print("\n\nUscita forzata dal programma.") # Uso print normale per uscire subito
        sys.exit()
    except Exception as e:
        slow_print(f"\nSi è verificato un errore: {e}")

    slow_print('\n' + '-' * 50 + '\n')
    slow_print(f"Scansione completata. TOT porte aperte trovate: {len(open_ports)}")

def print_table(open_ports):
    if not open_ports:
        slow_print("\nNessuna porta aperta trovata.")
        return
    
    open_ports.sort()
    slow_print("\n" + "_" * 24)
    slow_print(f"| {'PORTA':<10} | {'STATO':<7} |")
    slow_print("|" + "_" * 12 + "|" + "_" * 9 + "|")
    for port in open_ports:
        slow_print(f"| {port:<10} | {'APERTA':<7} |")
    slow_print("|" + "_" * 12 + "|" + "_" * 9 + "|")    

def exit_routine():
    slow_print('\n' + '-' * 50 + '\n')
    exit_input = input('Vuoi terminare il programma? Y/N: ').upper()
    if exit_input == 'Y':
        sys.exit()

def slow_print(text, speed=0.005): # Velocizzato di default
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Se il testo è lunghissimo saltiamo l'effetto sleep per non annoiare
        if len(text) < 200: 
            time.sleep(speed)
    print()

def print_banner():
    art = r"""
    .__   __.  __  ___   ___
    |  \ |  | |  | \  \ /  /
    |   \|  | |  |  \  V  / 
    |  . `  | |  |   >   <  
    |  |\   | |  |  /  .  \ 
    |__| \__| |__| /__/ \__\
       
          Port Scanner
    """
    slow_print(art)

if __name__ == "__main__":
    print_banner()
    while True:
        execute_scan() 
        exit_routine()   