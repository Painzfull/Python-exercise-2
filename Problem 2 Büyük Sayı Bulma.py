print("""
*****************************      
Kullanıcının Seçtiği Sayıların En Büyük Olanını Bulma
*****************************     
""")

a = int(input("Lütfen Birinci Sayıyı Giriniz:"))
b = int(input("Lütfen İkinci Sayıyı Giriniz:"))
c = int(input("Lütfen Üçüncü Sayıyı giriniz:"))

a > b > c

if(a > b > c):
    print("1.sayı en büyük")
elif(b > c > a):
    print("2.sayı en büyük")
elif(c > b > a):
    print("3.sayı en büyük")
else:
    print("Teşekkür ederiz...")


