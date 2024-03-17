import socket

wordlist = []
dosya_adi = 'wordlist.txt'
sitegir = input("Lütfen Bir Site Girin (örnek: yemeksepeti.com): ")

try:
    with open(dosya_adi, "r") as dosya:
        wordlist = [line.strip() for line in dosya if line.strip()]  # Boş satırları filtrele
except FileNotFoundError as e:
    print(f"Dosya Bulunamadı: {e}")

for subdomain in wordlist:
    if subdomain.endswith('.'):
        subdomain = subdomain[:-1]  # Eğer sondaki nokta varsa kaldır
    
    try:
        # Alt alan adını kontrol etmek için DNS sorgusu yap
        host = f"{subdomain}.{sitegir}"
        ip_address = socket.gethostbyname(host)
        print(f"{subdomain}.{sitegir} alt alanı mevcut: IP Adresi {ip_address}")
    except socket.gaierror as e:
        print(f"{subdomain}.{sitegir} alt alanı mevcut değil veya DNS çözümlenemedi: {e}")