# MODULE ---
import time
import pyfiglet
import os
from colorama import Fore, Style, init

teks_1 = ("SELAMAT DATANG DI PROGRAM RAFA 😏\n")
for kalimat in teks_1:
    time.sleep(0.08)
    print(kalimat, end=' ', flush=True)
print()
userInput = input("Masukan Kata yang ingin dijadikan Art Banner: ")
while True:
    userInputFont = input("Silahkan ingin memakai font apa:\nA > standard\nB > slant\nC > big\nD > doom\nE > banner3-D\nF > starwars\nG > isometric1\n Silahkan inputkan disini: ").lower()
    if userInputFont == "a":
        userInputFont = "standard"
        break
    elif userInputFont == "b":
        userInputFont = "slant"
        break
    elif userInputFont == "c":
        userInputFont = "big"
        break
    elif userInputFont == "d":
        userInputFont = "doom"
        break
    elif userInputFont == "e":
        userInputFont = "banner3-D"
        break
    elif userInputFont == "f":
        userInputFont = "starwars"
        break
    elif userInputFont == "g":
        userInputFont = "isometric1"
        break
    elif userInputFont.isdigit():
        print("Masukan berupa (A/B/C/D/E)")
    else:
        print("Silahkan masukan input yang benar")

os.system('cls' if os.name == 'nt' else 'cls') # Bersihkan Terminal
banner = pyfiglet.figlet_format(userInput, font=userInputFont)
print(banner)
time.sleep(0.8)
print("Welcome to your coding")