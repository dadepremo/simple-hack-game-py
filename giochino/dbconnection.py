from colorama import Fore, Back, Style, init
import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hack_game"
)

mycursor = mydb.cursor()

def countRecords(table):
    sql = "SELECT COUNT(*) FROM " + table
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    return myresult

def selectAll(table):
    mycursor.execute("SELECT * FROM " + table)
    myresult = mycursor.fetchall()
    return myresult

def visualizzaTabella(table):
    mycursor.execute("SELECT * FROM " + table)
    myresult = mycursor.fetchall()

    if table == "ipaddresses":
        print("+--------------+---------------------+")
        print("| ipaddress_id |      ipaddress      |")
        print("+--------------+---------------------+")
        for x in myresult:
            l = len(str(x[0]))
            l1 = len(x[1])
            space = ""
            for i in range(13-l):
                space += " "
            space1 = ""
            for i in range(19-l1):
                space1 += " "
            print("| " + str(x[0]) + space + "| " + x[1] + space1 + " |")
        print("+--------------+---------------------+")
    
    if table == "missions":
        for x in myresult:
            print(x)

    if table == "passwords":
        print("+-------------+--------------------+------------------+")
        print("| password_id |     hashed_psw     |     password     |")
        print("+-------------+--------------------+------------------+")
        for x in myresult:
            l = len(str(x[0]))
            space = ""
            for i in range(12-l):
                space += " "
            print("| " + str(x[0]) + space + "|    " + x[1] + "    |   " + x[2] + "   |")
        print("+-------------+--------------------+------------------+")

    if table == "ports":
        print("+---------+-------+----------+--------------+")
        print("| port_id | value |   type   | ipaddress_id |")
        print("+---------+-------+----------+--------------+")
        for x in myresult:
            l = len(str(x[0]))
            l1 = len(str(x[2]))
            l2 = len(str(x[3]))
            space = ""
            for i in range(7-l):
                space += " "
            space1 = ""
            for i in range(8-l1):
                space1 += " "
            space2 = ""
            for i in range(12-l2):
                space2 += " "
            print("| " + str(x[0]) + space + " | " + str(x[1]) + "  | " + x[2] + space1 + " | " + str(x[3]) + space2 + " |")
        print("+---------+-------+----------+--------------+")

    if table == "users":
        print("+---------+--------------------------+-------------+--------------+")
        print("| user_id |           user           | password_id | ipaddress_id |")
        print("+---------+--------------------------+-------------+--------------+")
        for x in myresult:
            l = len(str(x[0]))
            l1 = len(str(x[1]))
            l2 = len(str(x[2]))
            l3 = len(str(x[3]))
            space = ""
            for i in range(7-l):
                space += " "
            space1 = ""
            for i in range(24-l1):
                space1 += " "
            space2 = ""
            for i in range(11-l2):
                space2 += " "
            space3 = ""
            for i in range(12-l3):
                space3 += " "
            print("| " + str(x[0]) + space + " | " + x[1] + space1 + " | " + str(x[2]) + space2 + " | " + str(x[3]) + space3 + " |")
        print("+---------+--------------------------+-------------+--------------+")

def selectByField(table, field):
    sql = "SELECT {} FROM {}".format(table, field)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def selectByIdOne(table, key, id):
    sql = "SELECT * FROM {} WHERE {} = %s".format(table, key)
    mycursor.execute(sql, (id,))
    myresult = mycursor.fetchone()
    return myresult

def selectByIdAll(table, key, id):
    sql = "SELECT * FROM {} WHERE {} = %s".format(table, key)
    mycursor.execute(sql, (id,))
    myresult = mycursor.fetchall()
    return myresult

def insertIn(args): # args[0] = table
    if args[0] == "passwords":
        sql = "INSERT INTO passwords (hashed_psw, password) VALUES (%s, %s)"
        mycursor.execute(sql, (args[1], args[2]))
    elif args[0] == "ports":
        sql = "INSERT INTO ports (value, type, ipaddress_id) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (args[1], args[2], args[3]))
    elif args[0] == "ipaddresses":
        sql = "INSERT INTO ipaddresses (ipaddress) VALUES (%s)"
        mycursor.execute(sql, (args[1], ))
    elif args[0] == "users":
        sql = "INSERT INTO users (user, password_id, ipaddress_id) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (args[1], args[2], args[3]))
    elif args[0] == "missions":
        sql = "INSERT INTO missions (name, description, user_id, reward, money, flag) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, (args[1], args[2], args[3], args[4], args[5], args[6]))

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def completeMission(name):
    if name[0] == "all":
        sql= "UPDATE missions SET flag = 1"
        mycursor.execute(sql)
    else:
        for i in range(len(name)):
            sql = "UPDATE missions SET flag = 1 WHERE name = %s"
            values = (name[i],)
            mycursor.execute(sql, values)
            print(Fore.RED + Style.BRIGHT + "-> MISSION ENDED" + Style.RESET_ALL)
            time.sleep(0.5)

    mydb.commit()

def userJoinPsw(user):
    sql = "SELECT DISTINCT * FROM users"
    sql += "INNER JOIN passwords ON users.password_id = passwords.password_id"
    sql += "WHERE user = " + user
    mycursor.execute()
    myresult = mycursor.fetchall()  
    return myresult

def getUserAndPswJoin(ip, port):
    sql = "SELECT DISTINCT * FROM users "
    sql += "INNER JOIN passwords ON users.password_id = passwords.password_id "
    sql += "INNER JOIN ipaddresses ON users.ipaddress_id = ipaddresses.ipaddress_id "
    sql += "INNER JOIN ports ON ports.ipaddress_id = ipaddresses.ipaddress_id "
    sql += "WHERE ipaddress = %s AND value = %s"
    values = (ip, port)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchone()  
    return myresult

def missionVisJoin():
    sql = "SELECT DISTINCT * FROM missions " 
    sql += "INNER JOIN users ON missions.user_id = users.user_id "
    sql += "INNER JOIN ipaddresses ON ipaddresses.ipaddress_id = users.ipaddress_id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()  
    return myresult