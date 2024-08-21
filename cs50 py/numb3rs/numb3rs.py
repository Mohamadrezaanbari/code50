import re

import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        split_ip: list[str] = ip.split(".")

        if len(split_ip) < 4 or len(split_ip) > 4:
            return False

        for s in split_ip:
            if int(s) > 255:
                return False

    except ValueError:
        return False
    return True



if __name__ == "__main__":
    main()


