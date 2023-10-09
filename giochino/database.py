import random
import string
import dbconnection as dbcon
from colorama import Fore, Back, Style, init
init(autoreset=True)

portTypes = ["ssh", "http", "smtp"]

descriptions = [
    "Hack the user at the given IP address and steal all the money",
    "Hack this address and just disconnect",
    "Infiltrate a highly secure government database and extract classified information without leaving a trace.",
    "Breach a multinational corporation's network to expose their unethical practices and protect sensitive consumer data.",
    "Access a criminal syndicate's encrypted communications to gather evidence for law enforcement.",
    "Hack into a terrorist organization's communication network to prevent a potential threat or attack.",
    "Break into a rival tech company's servers to obtain their proprietary source code and gain a competitive edge.",
    "Disrupt the operations of a cybercriminal group by targeting their command and control servers.",
    "Gain access to a black market website and identify key vendors and buyers of illegal goods and services.",
    "Compromise a rogue AI system that poses a threat to global cybersecurity.",
    "Assist a whistleblower by hacking into a corrupt organization's servers to leak incriminating documents to the public.",
    "Infiltrate a high-stakes underground poker game to expose cheating players and recover stolen funds."
]


def casualString(l):
    c = string.ascii_letters + string.digits
    g = ''.join(random.choice(c) for _ in range(l))
    return g

def randomIpAddress():
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return str(ip_address)

def generateRandomUsername():
    adjectives = ["Clever", "Fast", "Silent", "Mysterious", "Cyber", "Stealthy", "Ninja", "Hacker", "Digital", "Anonymous"]
    nouns = ["Dragon", "Wolf", "Ghost", "Shadow", "Phantom", "Pirate", "Jedi", "Samurai", "Wizard", "Ninja"]

    random_adjective = random.choice(adjectives)
    random_noun = random.choice(nouns)
    random_number = random.randint(1000, 9999)

    random_username = f"{random_adjective}{random_noun}{random_number}"

    return random_username

def generateRandomPassword(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generatePort():
    return str(random.randint(4000, 7000))


def randomMission():
    prefixes = ["Operation", "Project", "Incognito", "Stealth", "SecureNet", "Ghost", "Spectre", "CyberStrike", "Infiltrator", "RogueWave", "SilentShadow", "Cipher", "DarkOps", "Phantom", "ZeroDawn"]
    suffixes = ["Revelation", "Protocol", "Intrusion", "Extraction", "Infiltration", "Cipher", "Espionage", "Defender", "Sabotage", "Syndicate", "Silencer", "Sovereign", "Assassin", "Phenomenon", "Nemesis"]
    mission_name = random.choice(prefixes) + random.choice(suffixes) # genera il nome della missione
    desc = descriptions[random.randint(0, len(descriptions) - 1)] # prende una descrizione casuale

    randomUser = generateRandomUsername() # genera uno user
    firstRandomPsw = generateRandomPassword() # genera una password
    secondRandomPsw = generateRandomPassword()
    randomIp = randomIpAddress() # genera un ip

    dbcon.insertIn(["passwords", firstRandomPsw, secondRandomPsw])
    dbcon.insertIn(["ipaddresses", randomIp])
    ipaddressRecord = dbcon.selectByIdOne("ipaddresses", "ipaddress", randomIp)
    passwordRecord = dbcon.selectByIdOne("passwords", "hashed_psw", firstRandomPsw)
    dbcon.insertIn(["users", randomUser, passwordRecord[0], ipaddressRecord[0]])
    userRecord = dbcon.selectByIdOne("users", "user", randomUser)
    dbcon.insertIn(["missions", mission_name, desc, userRecord[0], random.randint(250, 500), random.randint(100, 300), False])

    portsNumber = random.randint(1, len(portTypes))
    for i in range(portsNumber):
        dbcon.insertIn(["ports", generatePort(), random.choice(portTypes), ipaddressRecord[0]])
    

def visualizzaTutto():
    print(Fore.GREEN + Style.BRIGHT + "Table: ipaddresses =============" + Style.RESET_ALL)
    dbcon.visualizzaTabella("ipaddresses")
    print(Fore.GREEN + Style.BRIGHT + "\nTable: missions ================" + Style.RESET_ALL)
    dbcon.visualizzaTabella("missions")
    print(Fore.GREEN + Style.BRIGHT + "\nTable: passwords ===============" + Style.RESET_ALL)
    dbcon.visualizzaTabella("passwords")
    print(Fore.GREEN + Style.BRIGHT + "\nTable: ports ===================" + Style.RESET_ALL)
    dbcon.visualizzaTabella("ports")
    print(Fore.GREEN + Style.BRIGHT + "\nTable: users ===================" + Style.RESET_ALL)
    dbcon.visualizzaTabella("users")
    
