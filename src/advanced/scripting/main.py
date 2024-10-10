import sys


def main(source, target):
    pass


if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) != 3:
        raise Exception("Invalid number of args")
    source, target = args[1:]
    main(source, target)
