print("""
#############################################      
Girilen değerlerin şekil belirtip belirtmediğini bulan algoritma..
Algoritmanın amacı şeklin dörtgen veya üçgen olduğunu tespit etmek,
Tespit edilen dörtgen ya da üçgenin hangi türde olduğunu belirtmek
""")
a = input("Hangi şekil bilgisini öğrenmek istiyorsunuz? ==>")

if(a == "Dörtgen"):
    print("Lütfen Kenarları sırasıyla belirtiniz ==>")
    a = int(input("Birinci Kenar Değeri:"))
    b = int(input("İkinci Kenar Değeri:"))
    c = int(input("Üçüncü Kenar Değeri:"))
    d = int(input("Dördüncü kenar değeri:"))

    if(a == b and a == c and a == d):
        print("Seçilen dörtgen bir kare.")
    elif(a == c and b == d):
        print("Seçilen dörtgen bir dikdörtgen.")
    else:
        print("Seçilen şekil kare veya dikdörtgen değil.")

elif(a == "Üçgen"):
    print("Lütfen kenarları sırasıyla belirtiniz ==>")
    a = int(input("Birinci Kenar Değeri:"))
    b = int(input("İkinci Kenar Değeri:"))
    c = int(input("Üçüncü Kenar Değeri:"))

    if(abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if(a == b and a == c):
            print("Seçilen şekil bir eşkenar üçgen!")
        elif((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Seçilen şekil bir ikizkenar üçgen!")
        else:
            print("Seçilen üçgen bir çeşitkenar üçgen")
    else:
        print("Seçilen şekil bir üçgen belirtmiyor..")
else:
    print("Şekil belirtmiyor...")






