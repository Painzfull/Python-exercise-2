print("""
##########################################
Ladies and Gentlemans.....!
2 takım arasında yapılacak olan ihalemize hoşgeldiniz....!
İhale şartlarına göre sadece 2 takım ihaleye dahil olabilecek ve ihaleyi alan takıma koz seçme hakkı verilecek
Kartlar Dağıtıldı Başlıyoruz.
##########################################
""")

a = int(input("Birinci takımın teklifi:"))
b = int(input("İkinci takımın teklifi:"))

if(a > b):
    print("Birinci takım teklifini sundu..")
elif(b > a):
    print("İkinci takım teklifini sundu..\nİhaleyi kazanan takımın koz belirlemesi gerekiyor:")

c = int(input("Lütfen bir koz belirleyiniz =\n1-sinek\n2-kupa\n3-maça\n4-karo\n====>"))

if(1 <= c < 5):
    print("Oyun başladı iki takıma da başarılar....")
else:
    print("Geçerli koz bilgisi  verilmedi....!")