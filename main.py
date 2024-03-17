import requests

wordlist = []
dosya_adi = 'wordlist.txt'

try:
    with open(dosya_adi, "r") as dosya:
        wordlist.extend(dosya.read().splitlines())
except FileNotFoundError as e:
    print(f"Dosya BUlunamadı: {e}")

for i in wordlist:
    print(i) # wordlistin içini okumak içim