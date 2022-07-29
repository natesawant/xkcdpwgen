import argparse
import random
import requests

word_list_url = "http://www.mieliestronk.com/corncob_lowercase.txt"
word_list = requests.get(word_list_url).text.split()

desc = "Generate a secure, memorable password using the XKCD method. Written by Nate Sawant for CY2550."

parser = argparse.ArgumentParser(description=desc)

parser.add_argument(
    "-w", "--words", help="include WORDS words in the password\n(default=4)")

parser.add_argument(
    "-c", "--caps", help="capitalize the first letter of CAPS random words\n(default=0)")

parser.add_argument(
    "-n", "--numbers", help="insert NUMBERS random numbers in the password\n(default=0)")

parser.add_argument(
    "-s", "--symbols", help="insert SYMBOLS random symbols in the password\n(default=0)")

args = parser.parse_args()

words, caps, numbers, symbols = 4, 0, 0, 0

try:
    if (args.words):
        words = int(args.words)
    if (args.caps):
        caps = int(args.caps)
    if (args.numbers):
        numbers = int(args.numbers)
    if (args.symbols):
        symbols = int(args.symbols)
except:
    print("Arguments must be numbers")
    exit()

if (caps > words):
    print("Caps must be less than or equal to words")
    exit()

parts = []
symbols_list = "~!@#$%^&*.:;"

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

print("".join(map(str, parts)))
