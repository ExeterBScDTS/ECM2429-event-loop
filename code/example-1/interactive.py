"""_summary_
"""

def print_help() -> None:
    """_summary_
    """
    print("Enter one of the following commands:")
    print("\thelp\tdisplays this message")
    print("\tquit\tquit the program")
    print("\tdir\tprint a directory listing")
    print("\tpwd\tprint the current directory path")
    print()


def print_unknown(command: str) -> None:
    """Prompts user to enter help if they attempt and unknown command.

    :param command: the unknown command
    :type command: str
    """
    print(f"The command '{command}' is not recognised.")
    print("Enter 'help' to see a list of recognised commands.")
    print()


def do_dir() -> None:
    print()


def do_pwd() -> None:
    print()


def mainloop():
    """An even-loop that takes a typed command using the input() statement.
    """
    while True:
        # Wait here until the user types a command
        command = input("enter a command > ")

        if command == "help":
            print_help()
        # Can match the command to one of several words using 'in'
        elif command in ("quit", "exit"):
            break
        elif command == "dir":
            do_dir()
        elif command == "pwd":
            do_pwd()
        else:
            print_unknown(command)


if __name__ == "__main__":
    mainloop()
    print("Goodbye")
