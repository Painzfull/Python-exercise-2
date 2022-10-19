print("""
***********************  
Beden Kitle İndeksi Ölçme Programı
***********************  
""")

a = float(input("Lütfen kilonuzu giriniz:"))
b = float(input("Lütfen boyunuzu metre cinsinden giriniz:"))

beden_kitle_indeksi = a / (b * b)

if(beden_kitle_indeksi < 18.5 ):
    print("Alınan Değerler Göre = Zayıf")
elif(18.5 <= beden_kitle_indeksi < 25):
    print("Alınan Değerler Göre = Normal")
elif(25 <= beden_kitle_indeksi < 30):
    print("Alınan Değerler Göre = Fazla Kilolu")
elif(30 <= beden_kitle_indeksi):
    print("Alınan Değerler Göre = Obez")
else:
    print("Teşekkür ederiz ")


