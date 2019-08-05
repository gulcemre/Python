a = int(input("Birinci Sayı : "))
b = int(input("İkinci Sayı : "))

print("Değiştirilmeden Önceki değerler \n a: {}\nb :{}\n".format(a,b))

a,b =b,a

print("Değiştirildikten Sonraki değerler \n a: {}\nb :{}\n".format(a,b))


