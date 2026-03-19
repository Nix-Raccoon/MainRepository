# 🛡️ Cybersecurity Portfolio & Home Lab

Benvenuto nella mia repository dedicata ai progetti di **Cyber Security**. 
Questa cartella raccoglie i laboratori pratici, gli script e le analisi tecniche sviluppate durante il mio percorso formativo (Master EPICODE) e nel mio Home Lab personale. 

Il mio focus principale è sulle operazioni di **Blue Teaming, SOC Analysis e Incident Response**, mantenendo però una forte consapevolezza delle tattiche avversarie (Red Teaming) e delle solide basi architetturali di rete.

---

## 📂 Struttura della Repository

### [🌐 01. Networking & System Hardening](./01_Networking)
*Fondamenta di rete e sicurezza infrastrutturale.*
* **Routing & Switching:** Configurazioni di apparati di rete e VLAN (Cisco Packet Tracer).
* **Firewalling:** Creazione di policy di sicurezza su **pfSense**.
* **Scripting & Automation:** Revisione di codice Python, scripting in C e decriptazione.

### [⚔️ 02. Red Team & Vulnerability Assessment](./02_RedTeam)
*Comprendere l'attacco per migliorare la difesa (Approccio Purple Team).*
* **Information Gathering & Scanning:** OSINT, scansioni di rete con **Nmap** e Vulnerability Assessment con **Nessus**.
* **Web Application Security:** Sfruttamento vulnerabilità su ambienti test (DVWA), XSS, SQL Injection e File Upload exploit.
* **Exploitation & Post-Exploitation:** Utilizzo di **Metasploit** (es. Telnet, PostgreSQL, Icecast, Java RMI), attacchi DoS (UDP Flood) e Password Cracking (Hydra).
* **Social Engineering:** Analisi dei vettori di attacco basati sull'ingegneria sociale.

### [🛡️ 03. Blue Team & SOC Operations](./03_BlueTeam)
*Questa è la sezione core del mio portfolio, focalizzata sulla difesa, il monitoraggio e l'analisi.*
* **SIEM & Log Management:** Configurazione e monitoraggio tramite **Splunk** e **Wazuh** (calcolo dei rischi e alert).
* **Network & Endpoint Analysis:** Analisi log di Windows, esplorazione processi e ispezione profonda del traffico di rete (PCAP) tramite **Wireshark** (es. DNS, Three-Way Handshake).
* **Malware Analysis:** Analisi statica e dinamica di sample e SQL Injection.
* **System Administration:** Gestione permessi e configurazione su ambienti Linux Shell e Windows Server.

### [🛠️ 04. Progetti Vari & Automazione](./04_ProgettiVari_01_Json_Scan&Mail_Alert)
*Una raccolta in continua espansione di progetti personali, script custom e automazioni.*
* Al momento include tool operativi sviluppati in Python (come `triage_script.py` per l'automazione della scansione di file JSON e l'inoltro di alert via mail), ma la sezione verrà costantemente aggiornata con nuovi esperimenti, script e utility di sicurezza.

---

## 🛠️ Tecnologie e Strumenti Utilizzati
- **SIEM / IDS:** Splunk, Wazuh, pfSense
- **Analisi Rete:** Wireshark, Cisco Packet Tracer
- **Vulnerability & Offensive:** Nessus, Nmap, Metasploit, Burp Suite, Hydra
- **OS & Scripting:** Linux, Windows Server, Python, Bash, C

---
📫 **Contatti:** [Profilo LinkedIn](https://www.linkedin.com/in/nicolo-cali)
