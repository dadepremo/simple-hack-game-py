import commands as cmds
import os

def main():
    cmd = cmds.inputCommand()
    if cmd != '':
        cmds.executeCommand(cmd)
    main()

def start():
    print("\nWelcome to this simple hacker game: ")
    input("press enter to start\n")
    os.system("cls")
    main()



start()