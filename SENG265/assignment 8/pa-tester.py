#!/usr/bin/env python3

import sys
import re
import os


def check_invalid(password):
    invalid = ""
    if len(password) < 8:
        invalid += ",TOO_SHORT"
    if len(re.findall(r"[^\x00-\x7F]+", password)) > 0:
        invalid += ",NONASCII"
    return invalid if invalid else False


def check_uppercase(password):
    if len(re.findall(r"[A-Z]", password)) > 0:
        return True
    return False


def check_lowercase(password):
    if len(re.findall(r"[a-z]", password)) > 0:
        return True
    return False


def check_number(password):
    if len(re.findall(r"[0-9]", password)) > 0:
        return True
    return False


def check_special_character(password):
    if len(re.findall(r"[!#$%&()*+,\\\\\-./:;<=>?@\[\]^_`{|}~]", password)) > 0:
        return True
    return False


def check_sequence(password):
    if len(re.findall(r"(.)\1\1", password)) > 0:
        return True
    return False


def check_password(password):
    invalid = check_invalid(password)
    if invalid:
        return "0,INVALID" + invalid

    strength_map = [
        ",INVALID",
        ",VERY_WEAK",
        ",WEAK",
        ",MEDIUM",
        ",STRONG",
        ",VERY_STRONG",
    ]
    strength = 1
    strength_message = ""

    if check_uppercase(password):
        strength += 1
        strength_message += ",UPPERCASE"

    if check_lowercase(password):
        strength += 1
        strength_message += ",LOWERCASE"

    if check_number(password):
        strength += 1
        strength_message += ",NUMBER"

    if check_special_character(password):
        strength += 1
        strength_message += ",SPECIAL"

    if check_sequence(password):
        strength -= 1
        strength_message += ",sequence"

    return str(strength) + strength_map[strength] + strength_message


def main():
    """This script reads a text from standard input,
    analyzes the validity of a password in each line,
    if valid assesses the strength of the password,
    and writes results of the password analysis into
    the standard output"""

    # if arguments provided, show error message
    if len(sys.argv) != 1:
        print("No arguments should be provided.")
        print("Usage: %s" % sys.argv[0])
        return 1

    # ADD YOUR CODE HERE
    for password in sys.stdin:
        password = password.rstrip()
        print(check_password(password))

    # end the script normally
    return 0


if __name__ == "__main__":
    main()