from random import choice
import time

degerler = ["taş","kagıt","makas"]


while True:
    
    print("\nTaş Kagıt Makas Oyununa Hoşgeldin :)")
    
    kullancı = str(input("Taş mı? , Kagıt mı? , Makas mı ? => "))
    
    kullanıcı = kullancı.lower()
    print("Kullanıcı Seçim: ",kullancı)
    
    bilgisayar = choice(degerler)
    print("Bilgisayar Seçim: ",bilgisayar)
    
    if kullancı == "taş":
        if bilgisayar == "taş":
            print("Berabere")
        elif bilgisayar == "makas":
            print("Kullanıcı Kazandı")
        elif bilgisayar == "kagıt":
            print("Bilgisayar Kazandı")
        
        
    elif kullanıcı == "kagıt":
        if bilgisayar == "kagıt":
            print("Berabere")
        elif bilgisayar == "makas":
            print("Bilgisayar Kazandı")
        elif bilgisayar == "taş":
            print("Kullanıcı Kazandı")
        
        
    elif kullanıcı == "makas":
        if bilgisayar == "makas":
            print("Berabere")
        elif bilgisayar == "kagıt":
            print("Kullanıcı Kazandı")
        elif bilgisayar == "taş":
            print("Bilgisayar Kazandı")
        
        
    else:
        print("Yanlış Şeçim")
        
        
    karar = input("Oyuna Devam Etmek İster misin? Evet için 1 / Hayır İçin 0 => ")
    if karar == "evet" or karar == "EVET" or karar == "1":
        print("Yeniden Başlatıyor")
        time.sleep(3)
        continue
    else:
        print("Görüşmek Üzere...")
        break
    