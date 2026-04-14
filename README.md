# 🕵️ Net-Sniffer Pro

> **Analyseur de trafic réseau en temps réel**  
> Un outil de monitoring passif permettant de capturer, filtrer et analyser les paquets circulant sur une interface réseau.  
> Python 3 · Scapy · Analyse Multi-protocoles (TCP/UDP/ICMP)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-557C94?logo=kalilinux&logoColor=white)
![Category](https://img.shields.io/badge/Category-Network%20Analysis-blue)

---

## 📋 Présentation

**Net-Sniffer Pro** est un outil de surveillance réseau passif. Contrairement aux scanners actifs, il n'envoie aucun paquet sur le réseau mais *écoute* les données qui transitent par l'interface de la machine.

Il est essentiel pour :
- Comprendre les flux de communication
- Diagnostiquer des problèmes réseau
- Détecter des activités suspectes (ex : exfiltration de données, requêtes DNS inhabituelles)

---

## 🚀 Fonctionnalités

- **Capture en temps réel** : Analyse instantanée des paquets entrants et sortants  
- **Identification des protocoles** : Distinction visuelle des flux **TCP**, **UDP** et **ICMP**  
- **Analyse d'adressage** : Affichage clair des couples IP Source → IP Destination  
- **Filtrage par interface** : Support des interfaces (`eth0`, `wlan0`, `lo`)  
- **Léger et extensible** : Basé sur **Scapy** pour une analyse fine des couches OSI  

---

## ⚙️ Installation & Prérequis

### 🔧 Prérequis

Le script nécessite la bibliothèque **Scapy** :

```bash
pip install scapy
```

### 📦 Installation du projet

```bash
git clone https://github.com/Maxime288/Net-Sniffer-Pro.git
cd Net-Sniffer-Pro
chmod +x net_sniffer.py
```

---

## 🚀 Utilisation

> ⚠️ **Important**  
> La capture de paquets nécessite un accès direct à l'interface réseau (*raw sockets*).  
> Vous devez exécuter le script avec des privilèges **root/sudo**.

### 📌 Syntaxe de base

```bash
sudo python3 net_sniffer.py -i <INTERFACE>
```

### 🧰 Options disponibles

| Argument | Description | Défaut |
|----------|------------|--------|
| `-i`, `--interface` | Interface réseau à écouter (ex : eth0) | Auto |
| `-c`, `--count` | Nombre de paquets à capturer (0 = infini) | 0 |

### 💡 Exemples

```bash
# Écouter le trafic sur l'interface Ethernet
sudo python3 net_sniffer.py -i eth0

# Capturer seulement 100 paquets sur le Wi-Fi
sudo python3 net_sniffer.py -i wlan0 -c 100
```

---

## 🖥️ Aperçu du flux

Exemple de sortie du programme :

```text
[TCP ] 192.168.1.15 -> 192.168.1.134
[UDP ] 192.168.1.1  -> 192.168.1.255
[ICMP] 192.168.1.134 -> 8.8.8.8
[TCP ] 172.217.18.206 -> 192.168.1.15
```

---

## 🔬 Détails Techniques

- **Langage** : Python 3  
- **Moteur de capture** : `scapy.all.sniff`  
- **Couches analysées** :  
  - Couche 3 : IP  
  - Couche 4 : TCP / UDP / ICMP  
- **Performance** : Utilisation de `store=False` pour éviter la saturation mémoire lors de captures prolongées  

---

## ⚠️ Avertissement légal

Cet outil est strictement destiné à un usage **éducatif** ou **professionnel** dans le cadre de :

- diagnostics réseau
- tests d'intrusion autorisés

⚠️ L'interception de communications sur un réseau dont vous n'avez pas l'autorisation est **illégale** et passible de sanctions pénales.

L'auteur décline toute responsabilité en cas de mauvais usage.
