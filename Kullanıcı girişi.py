print("""
**************************
kullanıcı girişi
**************************
""")


sys_kullanıcı_adı = "mete can yaşar "
sys_parola = "1122334455"


kullanıcı_adı = input("Kullanıcı adı:")
parola = input("Parola:")


if(kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("Parola Hatalı....")

elif(kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("Kullanıcı Adı Hatalı.......")

elif(kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("Kullanıcı Adı ve Parola Hatalı.......")

else:
    print("Sisteme Giriş Yapılıyor Hoşgeldiniz.......")