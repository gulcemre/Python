print("Kullanıcı Bilgileri")

Adı= input("Adı: ")
Soyadı = input("Soyadı: ")
Numarası = int(input("Numarası: "))

bilgiler = [Adı,Soyadı,Numarası]

print("Kaydediliyor...")

print("Adı : {}\nSoyadı : {}\nNumarası : {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi")