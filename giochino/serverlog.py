import time
from colorama import Fore, Back, Style, init
import sys
import os
from os import system
import ctypes
import datetime
import random

system("title SERVER HTTP")

data_ora_corrente = datetime.datetime.now()
data_corrente = data_ora_corrente.date()
ora_corrente = data_ora_corrente.strftime('%H:%M:%S')
print("\nCurrent date:", data_corrente)
print("Current time:", ora_corrente)

code_list = [
    "[Serial #12345] " + str(data_corrente) + " " + ora_corrente + ": Server started successfully. (Code: S101)",
    "[Serial #67890] " + str(data_corrente) + " " + ora_corrente + ": Connection established with client at 192.168.0.1. (Code: C215)",
    "[Serial #54321] " + str(data_corrente) + " " + ora_corrente + ": Received GET request for /home. (Code: R308)",
    "[Serial #98765] " + str(data_corrente) + " " + ora_corrente + ": Connection closed with 192.168.0.1. (Code: C420)",
    "[Serial #24680] " + str(data_corrente) + " " + ora_corrente + ": Database connection established. (Code: D507)",
    "[Serial #13579] " + str(data_corrente) + " " + ora_corrente + ": Error: Unable to process the request. (Code: E911)",
    "[Serial #11223] " + str(data_corrente) + " " + ora_corrente + ": Incoming data stream detected. (Code: I703)",
    "[Serial #98700] " + str(data_corrente) + " " + ora_corrente + ": Disk space usage exceeded 90%. (Code: D900)",
    "[Serial #11111] " + str(data_corrente) + " " + ora_corrente + ": Security alert: Multiple failed login attempts. (Code: S401)",
    "[Serial #54325] " + str(data_corrente) + " " + ora_corrente + ": User 'admin' logged in successfully. (Code: U200)",
    "[Serial #77777] " + str(data_corrente) + " " + ora_corrente + ": Received POST request for /submit_form. (Code: R409)",
    "[Serial #55555] " + str(data_corrente) + " " + ora_corrente + ": SSH connection established from 192.168.0.2. (Code: S202)",
    "[Serial #99999] " + str(data_corrente) + " " + ora_corrente + ": Resource utilization exceeded threshold. (Code: R804)",
    "[Serial #12312] " + str(data_corrente) + " " + ora_corrente + ": Network traffic spike detected. (Code: N601)",
    "[Serial #24624] " + str(data_corrente) + " " + ora_corrente + ": Critical error: Application crashed. (Code: E500)",
    "[Serial #77788] " + str(data_corrente) + " " + ora_corrente + ": Backup completed successfully. (Code: B301)",
    "[Serial #33333] " + str(data_corrente) + " " + ora_corrente + ": Warning: Disk space running low. (Code: W107)",
    "[Serial #12121] " + str(data_corrente) + " " + ora_corrente + ": Request for /dashboard received. (Code: R601)",
    "[Serial #98989] " + str(data_corrente) + " " + ora_corrente + ": SSL certificate renewed. (Code: S700)",
    "[Serial #45678] " + str(data_corrente) + " " + ora_corrente + ": Server shutdown initiated for maintenance. (Code: S400)"
]

for i in range(40):
    serial_number = random.randint(10000, 99999)
    data_ora = data_ora_corrente - datetime.timedelta(minutes=i * 15)
    code_list.append(f"[Serial #{serial_number}] {str(data_corrente)} {str(ora_corrente)}: Starting process... PID: {random.randint(1000, 5000)}. (Code: C{i+1})")

# Imposta la dimensione del buffer
ctypes.windll.kernel32.SetConsoleScreenBufferSize(ctypes.windll.kernel32.GetStdHandle(-12), ctypes.wintypes._COORD(80, 25))
# Imposta la dimensione della finestra
ctypes.windll.kernel32.SetConsoleWindowInfo(ctypes.windll.kernel32.GetStdHandle(-11), True, ctypes.byref(ctypes.wintypes._SMALL_RECT(0, 0, 120, 24)))


init(autoreset=True)

print("\n")
title = Fore.GREEN + Style.BRIGHT + """
     _______________  _______________  ______________  _______    _______  _______________  ______________ 
    /               \/               \/              \/       \  /       \/               \/              \\
    |               |                |      ____     |        |  |       |                |      ____     |
    |               |                |     /    \    |        |  |       |                |     /    \    |
    |       ________/         _______/     \____/    |        |  |       |         _______/     \____/    |
    |               \                \ 	             |        |  |       |                \               |
    \               |                |        _______/        |  |       |                |        _______/
     \_________     |                |               \        \  /       |                |               \\
     /              |         _______/               |         \/        |         _______/               |
    /               |                \      |\       |                   |                \      |\       |
    |               |                |      | \      |                   |                |      | \      |
    |               |                |      |  \     |                   /                |      |  \     |
    \_______________/\_______________/\_____/   \____/\_________________/ \_______________/\_____/   \____/
     """ + Style.RESET_ALL
print(title)   
print("\n\n")
print("                                  ╔══════════════════════════════════════╗")
print("                                  ║           SERVER STARTING...         ║")
print("                                  ╚══════════════════════════════════════╝")

time.sleep(4)
os.system("cls")
print("\n")
print(Style.NORMAL + "     Starting service server..." + Style.RESET_ALL)
time.sleep(3)
print()
for log_message in code_list:
    print(log_message)
    time.sleep(0.1)
time.sleep(4)
os.system("cls")

arg1 = sys.argv[1]
ipaddress = sys.argv[2]

port = "";
service = "";
if arg1 == "ssh":
    service = arg1
    port = "8080"
elif arg1 == "http":
    service = arg1
    port = "8686"


ctypes.windll.kernel32.SetConsoleWindowInfo(ctypes.windll.kernel32.GetStdHandle(-11), True, ctypes.byref(ctypes.wintypes._SMALL_RECT(0, 0, 50, 12)))

print()
time.sleep(0.5)
space = ""
for i in range(9-len(service)):
    space += " "
print("    ╔══════════════════════════════════════╗")
print("    ║     " + Fore.GREEN + Style.BRIGHT + "     SERVER " + service.upper() + " STARTED... " + Style.RESET_ALL + space + "║")
print("    ╚══════════════════════════════════════╝")
time.sleep(0.5)
print("     server running @ " + Fore.YELLOW + Style.BRIGHT + ipaddress + Style.RESET_ALL + " via port " + Fore.YELLOW + Style.BRIGHT + port + Style.RESET_ALL)

print()

time.sleep(3)
print("     Details:")
time.sleep(0.5)
print("         host ip: " + Fore.YELLOW + Style.BRIGHT + ipaddress + Style.RESET_ALL)
time.sleep(0.5)
print("         port: " + Fore.YELLOW + Style.BRIGHT + port + Style.RESET_ALL)
time.sleep(0.5)
print("         service: " + Fore.YELLOW + Style.BRIGHT + service + Style.RESET_ALL )
print()


time.sleep(3)
input("     Enter to shutdown...")
os.system("cls")
print()
print()
print("     Shutting down...")
time.sleep(3)