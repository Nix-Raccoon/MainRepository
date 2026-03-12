import json
import os
import requests
import smtplib
import time
import sys
from email.message import EmailMessage
from dotenv import load_dotenv

# --- FUNZIONI DI SUPPORTO E GRAFICA ---

def print_typewriter(text, delay=0.005):
    """Stampa il testo a schermo simulando l'effetto di una macchina da scrivere."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def Banner_Start():
    """Stampa il banner iniziale."""
    print_typewriter("""
__     _______                      
\ \   / /_   _|  ___  __ _ _ __  
 \ \ / /  | |   / __|/ _` | '_ \  
  \ V /   | |   \__ \ (_| | | | | 
   \_/    |_|   |___/\__,_|_| |_| 
         >>> Developed by Nix <<<
                 
[*] Inizio scansione in corso...
""")

def Banner_End():
    """Stampa il banner finale."""
    print_typewriter("""
 ____                      _ 
|  _ \  ___  _ __   ___   | |
| | | |/ _ \| '_ \ / _ \  |_|
| |_| | (_) | | | |  __/   _ 
|____/ \___/|_| |_|\___|  (_)
                             
Thanks for using my program!
    """)

# --- MOTORE DI SCANSIONE PRINCIPALE ---

def Scan_Engine(file_path, report_file, vt_api_key, smtp_email, smtp_password):
    """Esegue il parsing dei log, interroga VirusTotal e gestisce l'alerting."""
    
    # Inizializziamo la memoria Cache locale alla funzione
    ip_cache = {} 
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    # Parsing dei Dati
                    log_data = json.loads(line.strip())
                    src_ip = log_data["src_ip"]
                    print(f"\n--- Analisi per: {src_ip} ---")
                    
                    # Controllo Cache
                    if src_ip in ip_cache:
                        print(f"⚡ [CACHE HIT] Trovato in memoria! Salto la chiamata API.")
                        malicious_votes = ip_cache[src_ip] 
                    
                    # Chiamata API per VirusTotal
                    else:
                        url = f"https://www.virustotal.com/api/v3/ip_addresses/{src_ip}"
                        headers = {"x-apikey": vt_api_key}
                        response = requests.get(url, headers=headers)
                        
                        if response.status_code == 200:
                            vt_data = response.json()
                            stats = vt_data["data"]["attributes"]["last_analysis_stats"]
                            malicious_votes = stats["malicious"]
                            
                            ip_cache[src_ip] = malicious_votes 
                            print(f"🌐 [API CALL] Risposta ricevuta e salvata in cache.")
                        else:
                            print(f"Errore API per {src_ip}: {response.status_code}")
                            continue 
                    
                    # Alerting, Reportistica e Notifiche Email
                    with open(report_file, "a") as report:
                        if malicious_votes > 0:
                            alert_msg = f"[CRITICAL] L'IP {src_ip} è MALEVOLO ({malicious_votes} rilevamenti)!\n"
                            print(f"🚨 {alert_msg.strip()}")
                            report.write(alert_msg)
                            
                            # Logica Email SMTP
                            if smtp_email and smtp_password:
                                try:
                                    msg = EmailMessage()
                                    msg.set_content(f"Dettagli dell'evento di sicurezza:\n{alert_msg}")
                                    msg['Subject'] = f"🚨 SOC ALERT: IP Malevolo Rilevato ({src_ip})"
                                    msg['From'] = smtp_email
                                    msg['To'] = smtp_email
                                    
                                    server = smtplib.SMTP('smtp.gmail.com', 587)
                                    server.starttls()
                                    server.login(smtp_email, smtp_password)
                                    server.send_message(msg)
                                    server.quit()
                                    print("📧 Alert inviato via Email con successo!")
                                except Exception as e:
                                    print(f"Errore nell'invio dell'email: {e}")
                            
                        else:
                            info_msg = f"[INFO] L'IP {src_ip} risulta sicuro ({malicious_votes} rilevamenti).\n"
                            print(f"✅ {info_msg.strip()}")
                            report.write(info_msg)

                except KeyError:
                    pass
                except json.JSONDecodeError:
                    pass
                    
    except FileNotFoundError:
        print(f"Errore: Il file {file_path} non è stato trovato.")


if __name__ == "__main__":
    # 1. Caricamento configurazioni sicure
    load_dotenv(".env")
    vt_api_key_env = os.getenv("VT_API_KEY")
    smtp_email_env = os.getenv("SMTP_EMAIL")
    smtp_password_env = os.getenv("SMTP_PASSWORD")

    if not vt_api_key_env:
        print("⚠️ ERRORE: La chiave API non è stata trovata! Controlla il file .env.")
        exit()

    file_log_path = "alerts.json"
    file_report_path = "report_triage.txt"

    # 2. Flusso di esecuzione ordinato
    Banner_Start()
    
    Scan_Engine(
        file_path=file_log_path, 
        report_file=file_report_path, 
        vt_api_key=vt_api_key_env, 
        smtp_email=smtp_email_env, 
        smtp_password=smtp_password_env
    )
    
    Banner_End()