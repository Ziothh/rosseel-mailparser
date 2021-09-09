def main():
    from sys import argv
    from mailparser import MailparserLauncher
    from mailparser.helpers.errors._CustomErrors import LaunchArgumentsError

    # Read the input args and assign the right settings
    try:
        MailparserLauncher(argv[1:]).start()
    except LaunchArgumentsError as e:
        print(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("🛑 KeyboardInterrupt")
