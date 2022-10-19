print("""
###################################  
Vize Final Notlarınızı Sisteme Girerek Kalıp Geçtiğinizi Öğrenebilirsiniz..

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.
""")
a = float(input("Lütfen 1. Vizeden Aldığınız Notu Giriniz:"))
b = float(input("Lütfen 2. Vizeden Aldığınız Notu Giriniz:"))
c = float(input("Lütfen Finalden Aldığınız Notu Giriniz:"))

a * (30/100) + b * (30/100) + c * (40/100)

if(a * (30/100) + b * (30/100) + c * (40/100) >= 90):
    print("Toplam Notunuz AA")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 85):
    print("Toplam Notunuz BA")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 80):
    print("Toplam Notunuz BB")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 75):
    print("Toplam Notunuz CB")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 70):
    print("Toplam Notunuz CC")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 65):
    print("Toplam Notunuz DC")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 60):
    print("Toplam Notunuz DD")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 55):
    print("Toplam Notunuz FD")
elif(a * (30/100) + b * (30/100) + c * (40/100) >= 50):
    print("Toplam Notunuz FF")
else:
    print("Kaldınız...")