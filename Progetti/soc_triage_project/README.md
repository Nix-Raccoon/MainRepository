# 🛡️ SOC Triage Automation

**Developed by Nix**

Un tool in Python progettato per automatizzare il triage di primo livello in un Security Operations Center (SOC). Lo script analizza file di log in formato JSON, estrae gli indirizzi IP sospetti e li verifica interrogando l'API di VirusTotal. Se viene rilevata una minaccia, il sistema genera un report locale e invia un alert in tempo reale via email.

## ✨ Funzionalità Principali

* **Parsing Sicuro:** Legge log NDJSON in modalità streaming, gestendo automaticamente eventuali errori di formattazione o dati mancanti.
* **Threat Intelligence:** Integrazione con l'API v3 di VirusTotal per ottenere il *Threat Score* degli indirizzi IP.
* **Caching in-memory:** Ottimizza le chiamate API salvando i risultati localmente. Se un IP si ripete nel file di log, lo script attinge alla cache azzerando i tempi di latenza.
* **Alerting Real-Time:** Invio automatico di notifiche via email (tramite protocollo SMTP crittografato) per ogni indicatore critico rilevato.
* **Secure Coding:** Utilizzo delle variabili d'ambiente (`.env`) per proteggere credenziali e chiavi API.

## ⚙️ Prerequisiti

Per far funzionare questo script, hai bisogno di:
1.  **Python 3.x** installato sul tuo sistema.
2.  Una **API Key gratuita di VirusTotal** (registrandoti sul loro sito).
3.  Un **Account Gmail** con la "Password per le app" configurata per l'invio delle email.

## 🚀 Installazione e Configurazione

1. **Clona la repository:**
git clone https://github.com/Nix-Raccoon/MainRepository.git
cd MainRepository/Progetti/soc_triage_project

3. Installa le librerie necessarie:**
pip install requests python-dotenv

3. Configura le variabili d'ambiente:
Crea un file chiamato esattamente .env nella cartella principale del progetto e compila i campi con i tuoi dati reali, seguendo la struttura del file .env.example incluso:

Snippet di codice
VT_API_KEY=la_tua_chiave_virustotal_qui
SMTP_EMAIL=la_tua_email@gmail.com
SMTP_PASSWORD=la_tua_password_per_le_app_di_16_caratteri
Prepara i log da analizzare:
Inserisci i log di rete che vuoi scansionare all'interno del file alerts.json, assicurandoti che abbiano il campo "src_ip".

💻 Utilizzo
Una volta configurato il file .env, puoi avviare il motore di scansione eseguendo:

Bash
python triage_script.py
Il programma mostrerà un banner nel terminale e inizierà ad analizzare gli IP, aggiornando in tempo reale il file report_triage.txt e inviando un'email in caso di riscontri critici.
