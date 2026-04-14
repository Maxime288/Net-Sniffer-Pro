#!/usr/bin/env python3
"""
🕵️ Net-Sniffer Pro
Analyseur de trafic réseau en temps réel.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
import argparse
import sys

# ──────────────────────────────────────────────────────────────
# Couleurs ANSI & Style
# ──────────────────────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[38;5;196m"
    GREEN   = "\033[38;5;82m"
    YELLOW  = "\033[38;5;226m"
    BLUE    = "\033[38;5;45m"
    PURPLE  = "\033[38;5;135m"
    GRAY    = "\033[38;5;244m"

BANNER = fr"""
{C.BLUE}   _   _      _   {C.PURPLE}  _____       _  {C.RESET}
{C.BLUE}  | \ | |    | |  {C.PURPLE} / ____|     (_) {C.RESET}
{C.BLUE}  |  \| | ___| |_ {C.PURPLE}| (___  _ __  _  {C.RESET}
{C.BLUE}  | . ` |/ _ \ __|{C.PURPLE} \___ \| '_ \| | {C.RESET}
{C.BLUE}  | |\  |  __/ |_ {C.PURPLE} ____) | | | | | {C.RESET}
{C.BLUE}  |_| \_|\___|\__|{C.PURPLE}|_____/|_| |_|_| {C.RESET}
{C.GRAY}        Network Packet Sniffer v1.0{C.RESET}
"""

def process_packet(packet):
    """Analyse chaque paquet capturé."""
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = "OTHER"
        color = C.GRAY

        if packet.haslayer(TCP):
            proto = "TCP"
            color = C.GREEN
        elif packet.haslayer(UDP):
            proto = "UDP"
            color = C.BLUE
        elif packet.haslayer(ICMP):
            proto = "ICMP"
            color = C.YELLOW

        print(f"[{color}{proto:<4}{C.RESET}] {C.BOLD}{ip_src}{C.RESET} -> {C.BOLD}{ip_dst}{C.RESET}")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Sniffer de paquets simple")
    parser.add_argument("-i", "--interface", help="Interface réseau (ex: eth0, wlan0)")
    parser.add_argument("-c", "--count", type=int, default=0, help="Nombre de paquets à capturer (0 = infini)")
    args = parser.parse_args()

    print(f" {C.BOLD}[*]{C.RESET} Écoute sur l'interface : {C.YELLOW}{args.interface if args.interface else 'Par défaut'}{C.RESET}")
    print(f" {C.BOLD}[*]{C.RESET} Appuyez sur Ctrl+C pour arrêter...\n")

    try:
        # sniff() nécessite souvent les privilèges root
        sniff(iface=args.interface, prn=process_packet, count=args.count, store=False)
    except PermissionError:
        print(f"{C.RED}[!] Erreur : Vous devez exécuter ce script avec sudo.{C.RESET}")
    except Exception as e:
        print(f"{C.RED}[!] Erreur : {e}{C.RESET}")

if __name__ == "__main__":
    main()
