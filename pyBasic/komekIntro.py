# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:33:51 2024

@author: Artun
"""

#%%
tc = "123456789028"
isim = "irem bahar"

print("Merhaba", isim[0:4])
print(tc[10])
print(tc[-1])

print(tc[9:-1])

#%% len fonksiyonu

print(len(tc))

ad2 = input("Adınızı Giriniz:")
print(ad2[len(ad2)-1])

#%% split,sprit
bilgi = "artun ankara 10".split()

ad = bilgi[0]
soyad = bilgi[1]
yas = int(bilgi[2])
#%% tersten yazdırma

durum = "bugün hava çok güzel"

print(durum[::-1])
print(durum.replace("ü","u"))
print(durum.replace("ü", "ü").replace("a","e"))
print(durum.count("a"))
#%% büyük küçük harf

durum = "Bugün Hava Çok Güzel"

print(durum.upper())
print(durum.lower())
#%% çalışma

cumle = input("Deger girin:")

kelime = cumle.split()

print("Küçük Harflerle:" + cumle.lower())
print("Büyük harfler ile:" + cumle.upper())
print("Cümledeki a sayısı:" + str(cumle.count("a") + cumle.count("A")))
print("İlk iki kelime:" + kelime[0] + kelime[1])
print("Cümledeki son harf:" + cumle[-1])
print("Cümledeki son kelime:" + kelime[len(kelime)- 1])
print("Tersten yazdırma:" + cumle[::-1])
print("Birinci kelime dünya:" + cumle.replace(kelime[0], "dünya"))
print("Cümle uzunluğu:" + str(len(cumle)))
#%% çalışma cevre alan
import math
kare = int(input("Kare kenar:"))
print()
dikdortgenKısa = float(input("Dikddörtgen kısa kenar:"))
dikdortgenUzun = float(input("Dikdörtgen Uzun kenar:"))
print()
ucgenTaban = float(input("Üçgen taban:"))
ucgenYukseklik = float(input("Üçgen yukseklik:"))
print()
cemberYariCap = float(input("Çember yarıçap"))
print()

print("Kare alan:" + str(kare * kare))
print("Kare çevre:" + str(kare * 4))
print()
print("Dikdörtgen alan:" + str(dikdortgenKısa * dikdortgenUzun))
print("Dikdörtgen alan:" + str(dikdortgenKısa * 2 + dikdortgenUzun * 2))
print()
print("Üçgen alan:" + str((ucgenTaban * ucgenYukseklik) / 2))
print("Üçgen çevere:" + str(ucgenTaban * 3))
print()
print("Çember çevrre:" + str(2*math.pi*cemberYariCap))
print("Çember Alan:" + str(math.pi*math.pow(cemberYariCap, 2)))
#%% diziler

ogrenciler = ["Ali", "Veli", "Mehmet"]
print(ogrenciler)
print(type(ogrenciler))
print(len(ogrenciler))

ogrenciler.append("Kerem")
ogrenciler.insert(1, "object")

#%% copy index ..

og3 = ogrenciler.copy()
og3[0] = "omer"

print(og3)
print(ogrenciler)
#%% calisma

arabalar = []

for i in range(5):
    arabalar.append(input(str(i)+". araba ekle:"))

print("Alınan liste:"+str(arabalar))

arabalar.remove("BMW")
print("Remove BMW:" + str(arabalar))

arabalar.pop()
print("Sobndakini çıkar:"+str(arabalar))

print("Dizi uzunluğu: "+ str(len(arabalar)))

arabalar.insert(2, "mazda")
print("2. indise mazda ekle" + str(arabalar))

arabalar.insert(1, "ferrari")
print("2. sıraya ferrari ekle" + str(arabalar))

arabalar2 = arabalar.copy()
arabalar2.insert(0, "opel")

print("Arabalar liste:" + str(arabalar))
print("Arabalar 2 opelli liste:" + str(arabalar2))

arabalar.reverse()
print("Arabalar tersten:"+str(arabalar))

arabalar.sort()
print("Sırala alfbatik:" + str(arabalar))

arabalar3 = ["şimşir mcquen", "emekçi mater"]
arabalar3.append(arabalar)
print("Arabalar 3"+ str(arabalar3))

arabalar.clear()
arabalar2.clear()
arabalar3.clear()
#%% 4 işlem

sayılar = []

sayılar.append(int(input("Sayı ekle:")))
sayılar.append(int(input("Sayı ekle:")))

print(str(sayılar[0] + sayılar[1]))
print(str(sayılar[0] - sayılar[1]))
print(str(sayılar[0] / sayılar[1]))
print(str(sayılar[0] * sayılar[1]))
#%% veri yapıları

liste = ["Elma","Armut"]
tup = ("elma","armut")

print(type(liste))
print(type(tup))

liste[0] = "Kivi"
tup[0] = "kivi"
#%% item value

set1 = {"elma", "armut","muz"}
print(set1)

sozluk = {
    "book" : "kitap",
    "pencil" : "kalem"
    }
notlar = {
    "book" : 70,
    "pencil" : 80
    }

print(sozluk["book"])
print(sozluk.items())
print(sozluk.values())
print(sozluk.keys())

liste = ["elma","armut"]

print("muz" in liste)
print("elma" in liste)

#%% deneme
Kayısı = "kayısı"
Kayısı[::-1]
print(Kayısı[0:3])
#%% operatörler

# sayi1= 10
# sayi2= 20

# print(sayi1==sayi2)
# print(sayi1 != sayi2)
# print(sayi1 < sayi2)
# print(sayi1 > sayi2)
# print(sayi1 != sayi2)
# print(sayi1 <= sayi2)
# print(sayi1 >= sayi2)
#%% if else
sayi1= 10
sayi2= 10
if sayi1 > sayi2:
    print("sayi1 büyük")
if sayi1 < sayi2:
    print("sayi2 büyük")
else: 
    print("sayilar eşit")


#%% trafik ışıkları


isiklar=["kirmizi","sari","yesil"]

suan= isiklar[0]

if suan == "kirmizi":
    print("DUR")
elif suan == "sari":
    print("HAZIRLAN")
elif  suan == "yesil":
    print("GEC")
else:
    print("yanlis isik")
    
    
#%%
sayi1= 10
sayi2= 20
sayi3= 30

if (sayi1 < sayi2) and (sayi1 < sayi3):
    print("en kucuk sayi sayi1")
elif sayi2 < sayi3:
    print("sayi2 en kucuk")
else:
    print("sayi3 en kucuk")
#%% calsisma

m = 9
t = True
f = False
a = 11

print( m > 11 or False)
print( m > 11 and True)
print(t or True)
print(t or m==m)
print(f or -a < 2)
#%% polidrom kelimler

isim = input("tersi kontrol edilicek kelime:")

if(isim.upper() == isim[::-1].upper()):
    print(isim + " polidrom bir ifadedir.")
else:
    print(isim + " polidrom bir ifade değildir.")
#%% pozitif ve tek mi sorusu

sayi = 10

if (sayi > 0) and ((sayi % 2) == 0):
    print("sayi çit ve pozitif")
else:
    print("sayı çift ve pozitif değil")
#%% döngüler

sehirler = ["Kocaeli","İstanbul","Ankara","Siirt"]

for sehir in sehirler:
    print(sehir)

for x in range(5): # sıfırdan 5 e kadar
    print(x)
    
for x in range(1,5): # 1 den 5 kadar
    print(x)

for x in range(0,5,2): # 0 dan 5 kadar 2 şerli
    print(x)
#%% uygulama

sayilar = []

for x in range(4):
    while True:
        sayi = int(input("Lütfen " + str(x + 1)+".elemanı girin : "))
        if sayi in sayilar:
            print("Sayı listede var")
        else:
            break
    print("Sayı eklendi")
    sayilar.append(sayi)

for sayi in sayilar:
    if sayi == 2:
        print("2 çıkarıldı")
        sayilar.remove(2)

print(sayilar)
#%% asal kontrol

def asaslmi(sayi):
    if sayi <= 1:
        print("Sayı asal değil")
        return
    for x in range(2, int(sayi/2)):
        if (sayi % x) == 0:
            print("Sayı asal değil")
            return
    print("Sayı asal")


sayi = int(input("Sayi giriniz:"))
asaslmi(sayi)
#%% faktoryel hesabı recusive

sayi = int(input("Faktoryeli hesaplanması istenen sayı(recusive):"))

def fak(sayi):
    if(sayi > 0):
        return sayi * fak(sayi-1)
    else:
        return 1

sonuc = fak(sayi)
print("Sonuc:" + str(sonuc))

#%% faktoryel while

sayi = int(input("Faktoryeli hesaplanması istenen sayı:"))
sonuc = 1

for x in range(1,sayi):
    sonuc = (x+1) * sonuc
    
print("Cevap:"+str(sonuc))
#%% fibonaci arr
 
sayi = int(input("Fibonaci hesaplaması hesaplanması istenen sayı:"))
sonuc = [1,1]

for x in range(sayi):
    if x == 0:
        print("1")
    elif x == 1:
        print("1")
    else:
        print(str(sonuc[x-1] + sonuc[x-2]))
        sonuc.append(sonuc[x-1] + sonuc[x-2])
#%% fibonaci değşlken 

a,b = 0,1
sayi = int(input("Fibonaci hesaplaması hesaplanması istenen sayı:"))

for x in range(sayi):
    a,b = b,a+b
    print(str(a))
#%% menü
import os

durum = "Y"
secim = 0

while durum == "Y":
    print("1\) Topla")
    print("2\) Çıkar")
    print("3\) Çarp")
    print("4\) Böl")
    secim = input("Seçim:")
    print("-----")
    sayi1 = int(input("Sayı 1:"))
    sayi2 = int(input("Sayı 2:"))
    if secim == "1":
        print(str(sayi1 + sayi2))
    elif secim == "2":
        print(str(sayi1 - sayi2))
    elif secim == "3":
        print(str(sayi1 * sayi2))
    elif secim == "4":
        print(str(sayi1 / sayi2))  
    durum = input("Devam edicekmisiniz Y/N:").upper()
    os.system("cls")
#%% ışıklar
ışıklar = ["Kırmızı","Sarı","Yeşil"]
durum = {
    "Kırmızı" : "Dur",
    "Sarı" : "Bekle",
    "Yeşil" : "Geç"
    }

for x in range(3):
    print(durum[ışıklar[x]])
    for y in range(1,4):
        print(y)
#%% dosyalar ile çalışmak

f = open("musteriler.txt","r") #read
f.read()

f = open("musteriler.txt","w") #write
f.write("ali")

f = open("musteriler.txt","a") #append
f.write("veli")

f = open("musteriler.txt","a") #append
f.write("ali")

vize = 34
final = 95
f.write(f"{vize},{final}")

f.close()
#%% dosya okuma

f = open("musteriler.txt","r")
a = f.read()
b = f.readline()
print(b)

for line in f:
    print(line)

for line in f:
    print(line.split(",")[0])    
f.close()
#%% dosyada silme işlemi

# r Read w Write a append x Dosya varsa hata

import os

os.remove("musteriler.txt")

#%% doya denemeleri-

kisiler = [["Bahar","43","50"],["Furkan","70","90"],["Murat","95","10"]]

file = open("notAlanInsanlar.txt","a")
for satir in kisiler:
    for sutun in satir:
        file.write(f"{sutun},")
    file.write("\n")

file.close()

file = open("notAlanInsanlar.txt","r")
for satir in file:
    sutun = satir.split(",")
    print(sutun[0] + " vize:" + sutun[1] + " final:"+sutun[2])

file.close()
#%% class

class Matemetik:
    def topla(self,a,b):
        return a+b
    
    def cıkar(self,a,b):
        return a-b
    
    def carp(self,a,b):
        return a*b
    
    def bol(self,a,b):
        return a/b
    
mat = Matemetik()
print(mat.topla(4, 2))
print(mat.cıkar(4, 2))
print(mat.carp(4, 2))
print(mat.bol(4, 2))
#%% class cont

class Matemetik:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def topla(self):
        return self.a + self.b
    
    def cıkar(self):
        return self.a - self.b
    
    def carp(self):
        return self.a * self.b
    
    def bol(self):
        return self.a / self.b

mat = Matemetik(4, 2)

print(mat.topla())
print(mat.cıkar())
print(mat.carp())
print(mat.bol())


#%% claslar data

class Kisi:
    
    def __init__(self,ad,soyad,yas,email,maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.email = email
        self.kardes_sayisi = 2
        self._maas = maas
        
    def maas(self):
        if self.kardes_sayisi == 2:
            self._maas *= 2 
            print(f"kardes sayısı oluğu için maaş: {self._maas}")
        else:
            print(f"maas: {self._maas}")
            
    def kardes_sayi(self,kardes_sayisi):
        self.kardes_sayisi = kardes_sayisi
    
kisi1 = Kisi("Ziyya","Ahmedov",18,"lazziya@email.com",7000)

print(kisi1.ad)
print(kisi1.kardes_sayisi)
kisi1.maas()

kisi1.kardes_sayi(4)
print(kisi1.kardes_sayisi)

#%% atm uygulaması 

class BankaATM:
    def __init__(self, balance=0,username="user",age=18,credi=0):
        self.balance = balance
        self.username = username
        self.age = age
        self.credi = credi

    def check_balance(self):
        print(f"Bu kadar paran oldu artık {self.balance} TL")
        print(f"{self.credi} TL bocunu da va")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} TL yatırdın ho")
        self.check_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} TL çekmektesiniz")
        else:
            print("Insufficient funds")
        self.check_balance()
        
    def has_credid(self, amaunt):
        if self.age < 18:
            print("Yaşın kaç başın kaç ne kredisi")
        elif self.balance * 4 < amaunt:
            print("O kadar parayı nörcen")
        else:
            self.credi += amaunt
            print(f"{amaunt} TL borç verdik sana tepe tepe kullan")
            
    def i_am(self):
        print("Sen seçilmiş kişi " + self.username+"'sin")
    
def main():
    atm = BankaATM(1000,"himler",18)  
    while True:
        print("\n*** Welcome Capitalizim HELLL to the ATM ***")
        print("1. Kaç TL var")
        print("2. Para çek")
        print("3. Para yatır")
        print("4. Bana kredi varmı")
        print("5. Ben burada kimim")
        print("6. Çık")
        choice = input("Seçimini yap paranı yönet: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Ne kadar yatırıyorsun: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Ne kadar çekecen: "))
            atm.withdraw(amount)
        elif choice == '4':
            amount = float(input("Ne kadar borç istiyon şimdi: "))
            atm.has_credid(amount)
            break
        elif choice == '5':
            
            break
        elif choice == '6':
            print("Yolun açık ola! Byy")
            break
        else:
            print("Seçimin buranın gerçekliğinden omak zorunda.")

if __name__ == "__main__":
    main()
#%% hamburgerci calss

class Hamburger():
    def __init__(self, ad, fiyat, icerikler=None):
        self.ad = ad
        self.fiyat = fiyat
        self.icerikler = icerikler if icerikler is not None else []

    def icerik_ekle(self, fiyat, icerik):
        self.fiyat += fiyat
        self.icerikler.append(icerik)
        print(f"Yeni içerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")

    def icerik_cikar(self, fiyat, icerik):
        if icerik in self.icerikler:
            self.fiyat -= fiyat
            self.icerikler.remove(icerik)
            print(f"{icerik} çıkarıldı - Yeni içerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")
        else:
            print(f"{icerik} listede bulunamadı.")

    def goster(self):
        print(f"{self.ad} - İçerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")

    def ozellik_guncelle(self, ad, fiyat, icerikler):
        self.ad = ad
        self.fiyat = fiyat
        self.icerikler = icerikler
        print("Hamburger özellikleri güncellendi.")


ham = Hamburger("Mega Menu", 70, ["Domates", "Et", "Ekmek"])
ham.goster() 

ham.icerik_ekle(4, "Sevgi")  
ham.icerik_cikar(20, "Domates")  

ham.ozellik_guncelle("Big Mac", 60, ["Soğan", "Et", "Turşu", "Ekmek"])
ham.goster()

#%% mat clası

class Mat():
    pi = 3.141592653589793
    
    def topla(self,s1,s2): #clastan çağrılırsa method olur
        return s1 + s2
    
    def cikar(self,s1,s2):
        return s1 - s2
    
    def bol(self,s1,s2):
        return s1 / s2
    
    def carp(self,s1,s2):
        return s1 * s2
    
    
        
mat = Mat()
print(mat.topla(1, 2) + 5)

        
class Matematik():
    pi = 3.141592653589793
    
    def topla(s1,s2): #clastan çağrılırsa method olur
        return s1 + s2
    
print(Matematik.topla(5,4))


class Mate():
    pi = 3.141592653589793
    
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        
    def topla(self):
        print(self.s1 + self.s2)
        
    def cikar(self):
        print(self.s1 + self.s2)
    
mat = Mate(2,3)
mat.topla()

#%% private public get set

class Banka:
    def __init__(self,adi,para_mik):
        self.adi = adi
        self.__para_mik = para_mik
        
    def getPara(self):
        return self.__para_mik
    
    def setPara(self):
        return self.__para_mik + 500
    
    def __pirvateFunc(self):
        print("Cant use")
        
    def getPrivateFunc(self):
        return self.__pirvateFunc()
    
m1 = Banka("Acun", 50000)
m2 = Banka("İcardi", 40000)

m1.getPrivateFunc()    
print(m2.__para_mik)
#%% parent class

class Hayvanlar():
    
    def __int__():
        print("Havanlar çağırıldı")
    def yurumek():
        print("Yürümekteyiz")

class Kuş(Hayvanlar):
    
    def __init__():
        print("Kuç çağırıldı")
    def ucmak():
        print("Kuşum uçarım")

class Maymun(Kuş):

    def __init__():
        print("Maymun çağırıldı")
    def tırmanmak():
        print("Maymunum trımanırım")

m1 = Maymun()
m1.yurumek()

kuş1 = Kuş()
kuş1.yürümek()
#%% polymofizim

class  CompEng:
    def __init__(self,maas):
        self.maas = maas
    def zam(self,zam_mik):
        self.maas += (zam_mik / 2)
        return self.maas

class EEE:
    def __init__(self,maas):
        self.maas = maas
    def zam(self,zam_mik):
        self.maas += (zam_mik / 3)
        return self.maas

class Industrial:
    def __init__(self,maas):
        self.maas = maas
    def zam(self,zam_mik):
        self.maas += (zam_mik / 4)
        return self.maas
        
c1 = CompEng(5000)
print(c1.zam(7000))

e2 = EEE(5001)
print(e2.zam(8000))

#%% hamburger hambuger kofte hamburger tavuk

class Hamburger():
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat

class HamburgerKofte(Hamburger):
    
    def __init__(self, ad, fiyat, icerikler=None):
        super().__init__(ad, fiyat)
        self.icerikler = icerikler if icerikler is not None else []
    
    def icerik_ekle(self, fiyat, icerik):
        self.fiyat += fiyat
        self.icerikler.append(icerik)
        print(f"Yeni içerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")

    def icerik_cikar(self, fiyat, icerik):
        if icerik in self.icerikler:
            self.fiyat -= fiyat
            self.icerikler.remove(icerik)
            print(f"{icerik} çıkarıldı - Yeni içerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")
        else:
            print(f"{icerik} listede bulunamadı.")

    def goster(self):
        print(f"{self.ad} - İçerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")

    def ozellik_guncelle(self, ad, fiyat, icerikler):
        self.ad = ad
        self.fiyat = fiyat
        self.icerikler = icerikler
        print("Hamburger özellikleri güncellendi.")
        
class HamburgerTavuk(Hamburger):
    
    def __init__(self, ad, fiyat, icerikler=None):
        super().__init__(ad, fiyat)
        self.icerikler = icerikler if icerikler is not None else []
    
    def icerik_ekle(self, fiyat, icerik):
        self.fiyat += fiyat
        self.icerikler.append(icerik)
        print(f"Yeni içerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")

    def icerik_cikar(self, fiyat, icerik):
        if icerik in self.icerikler:
            self.fiyat -= fiyat
            self.icerikler.remove(icerik)
            print(f"{icerik} çıkarıldı - Yeni içerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")
        else:
            print(f"{icerik} listede bulunamadı.")

    def goster(self):
        print(f"{self.ad} - İçerikler: {', '.join(self.icerikler)} - Fiyat: {self.fiyat} TL")

    def ozellik_guncelle(self, ad, fiyat, icerikler):
        self.ad = ad
        self.fiyat = fiyat
        self.icerikler = icerikler
        print("Hamburger özellikleri güncellendi.")

def anaMenu():
    print("1. Köfte Hamburger")
    print("2. Tavuk Hamburger")
    print("3. Çıkış")

def kofteHamburgerMenu():
    print("1. İçerik Ekle")
    print("2. İçerik Çıkar")
    print("3. Göster")
    print("4. Özellikleri Güncelle")
    print("5. Ana Menü")

def tavukHamburgerMenu():
    print("1. İçerik Ekle")
    print("2. İçerik Çıkar")
    print("3. Göster")
    print("4. Özellikleri Güncelle")
    print("5. Ana Menü")

def main():
    while True:
        anaMenu()
        secim = input("Seçiminizi yapın: ")
        if secim == "1":
            print("Köfte Hamburger Menüsü")
            kofteHamburger = HamburgerKofte("Kofte Hamburger", 10)
            while True:
                kofteHamburgerMenu()
                secim = input("Seçiminizi yapın: ")
                if secim == "1":
                    icerik = input("Eklemek istediğiniz içeriği girin: ")
                    fiyat = float(input("İçeriğin fiyatını girin: "))
                    kofteHamburger.icerik_ekle(fiyat, icerik)
                elif secim == "2":
                    icerik = input("Çıkarmak istediğiniz içeriği girin: ")
                    fiyat = float(input("İçeriğin fiyatını girin: "))
                    kofteHamburger.icerik_cikar(fiyat, icerik)
                elif secim == "3":
                    kofteHamburger.goster()
                elif secim == "4":
                    ad = input("Yeni ismi girin: ")
                    fiyat = float(input("Yeni fiyatı girin: "))
                    icerikler = input("Yeni içerikleri girin (virgülle ayırın): ").split(",")
                    kofteHamburger.ozellik_guncelle(ad, fiyat, icerikler)
                elif secim == "5":
                    break
                else:
                    print("Geçersiz seçim!")
        elif secim == "2":
            print("Tavuk Hamburger Menüsü")
            tavukHamburger = HamburgerTavuk("Davuk Hamburger", 10)
            while True:
                kofteHamburgerMenu()
                secim = input("Seçiminizi yapın: ")
                if secim == "1":
                    icerik = input("Eklemek istediğiniz içeriği girin: ")
                    fiyat = float(input("İçeriğin fiyatını girin: "))
                    tavukHamburger.icerik_ekle(fiyat, icerik)
                elif secim == "2":
                    icerik = input("Çıkarmak istediğiniz içeriği girin: ")
                    fiyat = float(input("İçeriğin fiyatını girin: "))
                    tavukHamburger.icerik_cikar(fiyat, icerik)
                elif secim == "3":
                    tavukHamburger.goster()
                elif secim == "4":
                    ad = input("Yeni ismi girin: ")
                    fiyat = float(input("Yeni fiyatı girin: "))
                    icerikler = input("Yeni içerikleri girin (virgülle ayırın): ").split(",")
                    tavukHamburger.ozellik_guncelle(ad, fiyat, icerikler)
                elif secim == "5":
                    break
                else:
                    print("Geçersiz seçim!")
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

main()
