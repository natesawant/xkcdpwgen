import argparse
import random
import requests

word_list_url = "https://raw.githubusercontent.com/hugsy/stuff/refs/heads/main/random-word/english-nouns.txt"
word_list = requests.get(word_list_url).text.split()

symbols_list = "~!@#$%^&*.:;"

desc = "Generate a secure, memorable password using the XKCD method. Written by Nate Sawant for CY2550."
parser = argparse.ArgumentParser(description=desc)

parser.add_argument(
    "-w", "--words", help="include WORDS words in the password", type=int, default=4)

parser.add_argument(
    "-c", "--caps", help="capitalize the first letter of CAPS random words", type=int, default=0)

parser.add_argument(
    "-n", "--numbers", help="insert NUMBERS random numbers in the password", type=int, default=0)

parser.add_argument(
    "-s", "--symbols", help="insert SYMBOLS random symbols in the password", type=int, default=0)

args = parser.parse_args()

words = args.words
caps = args.caps
numbers = args.numbers
symbols = args.symbols

if (caps > words):
    print("Caps must be less than or equal to words")
    exit()

parts = []

for i in range(words):
    parts.append(word_list[random.randrange(len(word_list))])
    if caps > 0:
        parts[i] = parts[i].capitalize()
        caps -= 1
for i in range(numbers):
    parts.append(random.randrange(0, 9))
for i in range(symbols):
    parts.append(symbols_list[random.randrange(len(symbols_list))])

random.shuffle(parts)

print("".join(str(p) for p in parts))
