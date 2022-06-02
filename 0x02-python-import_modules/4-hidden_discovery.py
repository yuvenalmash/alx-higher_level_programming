#!/usr/bin/python3
import hidden_4


def main():
    """
    that prints all the names defined by the compiled module hidden_4.pyc
    """
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)


if __name__ == "__main__":
    main()
