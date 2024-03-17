import requests
from colorama import Fore, Back, Style

wordlist = []
dosya_adi = 'wordlist.txt'
sitegir = input("Lütfen Bir Site Girin (örnek: yemeksepeti.com):  ")
try:
    with open(dosya_adi, "r") as dosya:
        wordlist.extend(dosya.read().splitlines())
except FileNotFoundError as e:
    print(f"Dosya Bulunamadı: {e}")

for i in wordlist:
    print(i+sitegir)