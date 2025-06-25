import socket
from datetime import datetime

def port_scan(target, startport, stopport):
    print(f"Hedef site/IP {target} taraniyor. Taranacak portlar {startport} ile {stopport} arasi")
    try:
        for port in range(startport, stopport + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)                    # Burada girintiye dikkat!
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Açik port bulundu: {port}")
            sock.close()
    except KeyboardInterrupt:
        print("Tarama iptal edildi")
    except socket.gaierror:
        print("Hedef IP veya adres bulunamadi")
    except socket.error:
        print("Ağ bağlantisi sorunu")
    print(f"\nTarama tamamlandi: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    target_ip = input("IP veya web sitesi giriniz: ")
    try:
        a = int(input("Port başlangic numaranizi giriniz: "))
        b = int(input("Port bitis numaranizi giriniz: "))
        
        if a > b or a < 1 or b > 65535:            # Burada da mantık kontrolünü düzelttim
            print("Gecersiz degerler! Port taramasi icin 1-65535 arasi deger verin. Baslangic portu bitis portundan buyuk olamaz.")
        else:    
            port_scan(target_ip, a, b)
    except ValueError:
        print("[!] Lütfen geçerli bir sayi girin.")