import time
import sys
import os
import database as db
import dbconnection as dbcon
from colorama import Fore, Back, Style, init
import subprocess
init(autoreset=True)

clear = lambda: os.system('cls')


USER = ""
PSW = ""
ADDRESS = ""
ROOT = False

HASHED_PASSWORD_LENGTH = 10

#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

def inputCommand():
    s = "> "
    if USER != "":
        s = " > "

    c = ""
    if ROOT == True:
        c = Fore.RED + USER + Fore.RESET
    else:
        c = USER

    cmd = input(c + s)
    return cmd

def executeCommand(cmd):
    details = cmd.split()
    # getting the command and arguments 
    command = details[0]
    details.pop(0)
    # number of the arguments
    l = len(details)
    # main logic
    if command == "nmap" and l == 1:
        nmap(details[0])
    elif command == "nmap":
        print("nmap [ip-address]")
    elif command == "decipher" and l != 0:
        decipher(details)
    elif command == "decipher":
        print("decipher [crypted password] [...]")
    elif command == "ssh" and l == 3:
        ssh(details)
    elif command == "ssh":
        print("ssh [user]@[password] [ip-address] [port]")
    elif command == "sshgetuser" and l == 2:
        getUserAndPsw(details)
    elif command == "sshgetuser":
        print("sshgetuser [ip-address] [port]")
    elif command == "httpserver":
        serverStart("http")
    elif command == "httpserver -h" or command == "httpserver --help":
        print("sshgetuser (ip-address)")
    elif command == "disconnect" and l == 1:
        disconnect(details[0])
    elif command == "disconnect":
        print("disconnect [yes/no]")
    elif command == "sudo" and l == 1:
        sudo(details)
    elif command == "sudo":
        print("sudo [password]")
    elif command == "mission":
        mission()
    elif command == "newmission":
        db.randomMission()
    elif command == "endmission" and l != 0:
        closeMission(details)
    elif command == "endmission":
        print("endmission [mission_name1] [mission_name2] [...] or just [all]")
    elif command == "help":
        help()
    elif command == "cls":
        clear()
    elif command == "quit" and l > 0 and details[0] == 'yes':
        exit()
    elif command == "quit":
        print("quit [yes/no]")
    elif command == "visualizza":
        db.visualizzaTutto()
    elif command == "insertProva":
        dbcon.insertProva(input("user: "), input("psw: "))
    elif command == "selectAll":
        dbcon.selectAll(input("table: "))
    elif command == "prova":
        prova()
    elif command == "selectById":
        dbcon.selectByIdOne(input("table: "), input("key column: "), input("id: "))
    else:
        print("type help for the list of commands\nor type [command] -h")

def load(l):
    print("\n")
    for i in range(l+1):
        sys.stdout.write('\r')
        progress = (i * 100) // l
        s = "[%-" + str(l) + "s] %d%%"
        sys.stdout.write(s % ('=' * (i), progress))
        sys.stdout.flush()
        time.sleep(0.25)
    print("\n")

def help():
    print("\n")
    print(Style.BRIGHT + "LIST OF COMMANDS: " + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "    nmap [ip-addres]" + Style.RESET_ALL + " to scan the ip-addres for voulnerable ports")
    print(Fore.YELLOW + Style.BRIGHT + "    decipher [password1] [password2] [...]" + Style.RESET_ALL + " to decipher as many passwords you want")
    print()
    print(Fore.YELLOW + Style.BRIGHT + "    ssh [user] [password] [ip-address] [port]" + Style.RESET_ALL + " to connect remotely via ssh")
    print(Fore.YELLOW + Style.BRIGHT + "    sshgetuser [ip-address] [port]" + Style.RESET_ALL + " to get a user and an hashed password")
    print()
    print(Fore.YELLOW + Style.BRIGHT + "    httpserver [ip-address]" + Style.RESET_ALL + " to start the http server")
    print()
    print(Fore.YELLOW + Style.BRIGHT + "    endmission [mission_name1] [mission_name2] [...] or [all]" + Style.RESET_ALL + " to close as manu missions you want or all the missions")
    print(Fore.YELLOW + Style.BRIGHT + "    newmission" + Style.RESET_ALL + " creates a new mission")
    print(Fore.YELLOW + Style.BRIGHT + "    mission" + Style.RESET_ALL + " it visualizes all the active missions")
    print()
    print(Fore.YELLOW + Style.BRIGHT + "    disconnect [yes/no]" + Style.RESET_ALL + " to disconnect from user")
    print(Fore.YELLOW + Style.BRIGHT + "    sudo [password]" + Style.RESET_ALL + " to get root access")
    print(Fore.YELLOW + Style.BRIGHT + "    sudo su" + Style.RESET_ALL + " to leave the root access")
    print()
    print(Fore.YELLOW + Style.BRIGHT + "    quit [yes/no]" + Style.RESET_ALL + " to quit the game")
    print(Fore.YELLOW + Style.BRIGHT + "    cls" + Style.RESET_ALL + " to clear the console")
    print("\n")

def nmap(d):
    thisIp = dbcon.selectByIdOne("ipaddresses", "ipaddress", d)
    if thisIp:
        thisIpId = thisIp[0]
        ports = dbcon.selectByIdAll("ports", "ipaddress_id", thisIpId)
        print("Vulnerabilities discovered at " + Fore.GREEN + Style.BRIGHT + d + Style.RESET_ALL + ": ")
        for k in ports:
            time.sleep(0.5)
            print("->     " + Fore.YELLOW + Style.BRIGHT + str(k[1]) + Style.RESET_ALL + " " + k[2] + " port")
        print("\n")
    elif thisIp:
        error("ip-address not found")
    else:
        error("no voulnerable ports detected")

def decipher(psw):
    print(Fore.YELLOW + Style.BRIGHT + "CRYPTED PASSWORD " + Style.RESET_ALL + "=>" + Fore.GREEN + Style.BRIGHT + " PASSWORD\n" + Style.RESET_ALL)
    r = dbcon.selectAll("passwords")
    found = False
    for p in psw:
        for i in r:
            if p == i[1]:
                found = True
                foundHash = i[1]
                foundPsw = i[2]
        if found == True:
            print(Fore.YELLOW + Style.BRIGHT + foundHash  + Style.RESET_ALL + " => " + Fore.GREEN + Style.BRIGHT + foundPsw + Style.RESET_ALL)
        else:
            error("invalid password")
        found = False
    print("\n")

def ssh(args):
    usrAndPsw = args[0].split("@")
    user = usrAndPsw[0]
    psw = usrAndPsw[1]
    ip = args[1]
    port = args[2]
    global USER, PSW, ADDRESS
    thisUser = dbcon.selectByIdOne("users", "user", user)
    if thisUser is not None:
        thisPsw = dbcon.selectByIdOne("passwords", "password", psw)
        if thisPsw is not None:
            thisIp = dbcon.selectByIdOne("ipaddresses", "ipaddress", ip)
            if thisIp is not None:
                thisPort = dbcon.selectByIdOne("ports", "value", int(port))
                if thisPort[2] == "ssh" and thisPort is not None:
                    print("\nConnecting to " + Fore.GREEN + Style.BRIGHT + user + "@" + psw + Style.RESET_ALL + " \nat " + Fore.YELLOW + Style.BRIGHT + ip + Style.RESET_ALL + " via ssh port " + Fore.YELLOW + Style.BRIGHT + port + Style.RESET_ALL)
                    load(20)
                    USER = user
                    PSW = psw
                    ADDRESS = ip
                else:
                    error("cannot acces via this port")
            else:
                error("ip-address does not exist")
        else:
            error("wrong password")
    else:
        error("user does not exist")

def disconnect(yn):
    global USER, PSW, ADDRESS
    if yn == 'yes':
        USER = ''
        PSW = ''
        ADDRESS = ''
        print(Fore.RED + "DISCONNECTED" + Fore.RESET + "\n")

def mission():
    missions = dbcon.missionVisJoin()
    #print(missions)
    if missions is not None:
        print("\n" + Fore.MAGENTA + "Mission name" + Fore.RESET +  " : " + Fore.BLUE + "Description" + Fore.RESET + "\n")
        for x in missions:
            print("\n")
            if x[6] == True:
                continue
            print(Fore.MAGENTA + Style.BRIGHT + x[1] + Style.RESET_ALL + " : " + Fore.BLUE + Style.BRIGHT + x[2] + Style.RESET_ALL)
            print("Details:")
            print("ip-address: " + Fore.YELLOW + Style.BRIGHT + x[12] + Style.RESET_ALL)
            print("XP: " + Fore.MAGENTA + Style.BRIGHT + str(x[4]) + Style.RESET_ALL + " Pay: " + Fore.GREEN + Style.BRIGHT + str(x[5]) + Style.RESET_ALL + "$")
    else:
        print("\n" + Fore.RED + "YOU DON'T HAVE ANY ACTIVE MISSION" + Fore.RESET + "\n")

def closeMission(args):
    print("\n")
    if args[0] != 'all':
        dbcon.completeMission(args)
    else:
        dbcon.completeMission(args)
        print(Fore.RED + "ALL MISSIONS CLEARED" + Fore.RESET)
    print("\n")

def error(s):
    print("[" + Fore.RED + Style.BRIGHT + "ERROR" + Style.RESET_ALL + "] -> " + s)

def info(s):
    print("[" + Fore.BLUE + Style.BRIGHT + "INFO" + Style.RESET_ALL + "] -> " + s)

def sudo(d):
    global ROOT
    if ROOT == False:
        checkUser = dbcon.selectByIdOne("users", "user", USER)
        if checkUser is not None:
            join = dbcon.userJoinPsw(USER)
            stored_password = join[6]
            if d[0] == stored_password:
                info("accessed to root level")
                ROOT = True
            else:
                error("wrong password")
        else:
            error("user does not exist")
    elif ROOT == True:
        checkUser = dbcon.selectByIdOne("users", "user", USER)
        if d[0] == 'su':
            ROOT = False
        elif checkUser is not None:
            join = dbcon.userJoinPsw(USER)
            stored_password = join[6]
            if d[0] == stored_password:
                info("you already have root acces")

def getUserAndPsw(l):
    if len(l[1]) != 4:
        error("wrong port size")
        return
    
    join = dbcon.getUserAndPswJoin(l[0], l[1])
    try:
        if join is not None and join[11] == "ssh":
            print("\nRetrieving informations...")
            print("-> IP: " + Fore.GREEN + Style.BRIGHT + l[0] + Style.RESET_ALL)
            print("-> PORT: " + Fore.YELLOW + Style.BRIGHT + l[1] + Style.RESET_ALL)
            load(25)
            print(Fore.YELLOW + Style.BRIGHT + "USER" + Style.RESET_ALL + " => " + Fore.GREEN + Style.BRIGHT + "HASHED PASSWORD" + Style.RESET_ALL)
            print(join[1] + " => " + join[5])
        elif join[11] == "ssh":
            error("can't perform this exploit via this port")
        else:
            error("wrong ip-address or port")
    except Exception as e:
        print("Errore:", e)

def serverStart(type):
    # os.system("start /wait cmd /c serverlog.py")
    #os.system("start cmd /c serverlog.py")
    global USER
    global ADDRESS
    ip = ""
    if USER == "":
        ip = "127.0.0.1"
    else:
        ip = ADDRESS

    file_path = "serverlog.py"
    current_path = os.environ.get('PATH', '')
    os.environ['PATH'] = current_path + os.pathsep + os.path.dirname(file_path)
    cmd_command = f'start cmd /k python "{os.path.basename(file_path)}" {type} {ip}'
    subprocess.Popen(cmd_command, shell=True)
    os.environ['PATH'] = current_path

    
        
    #try:
    #    subprocess.Popen(["start", "cmd", "/c", "python", "C:/Users/david/OneDrive/Desktop/giochino/serverlog.py", type, ip])
    #except Exception as e:
    #    print("Errore:", e)
    #os.system("start cmd /c serverlog.py " + type + " " + ip)


def prova():
    print("prova")