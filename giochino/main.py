import commands as cmds


def main():
    cmd = cmds.inputCommand()
    if cmd != '':
        cmds.executeCommand(cmd)
    main()

def start():
    print("\nWelcome to this simple hacker game: ")
    input("press enter to start\n")
    main()



start()