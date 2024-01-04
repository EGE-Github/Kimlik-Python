ad = input("Adınız: ")
soyad = input("Soyadınız: ")
cinsiyet = input("Cinsiyetiniz: ")
is_durumu = input("İş Durumunuz (örneğin, öğrenci): ")
born = input("Doğum Yılınız: ")
sonuc = 2024 - int(born)
boy = int(input("Boyunuz (cm): "))

if boy > 159:
    print("Çok uzunmuşşsunuz!")

if boy < 159:
    print('Çok kısasınız!')

if boy == 160:
    print('Neredeyse İyi.')

kilo = int(input("Kilonuz (kg): "))
memleket = input("Memleketiniz: ")
print("\nGirilen Bilgiler:")
print("Ad:", ad)
print("Soyad:", soyad)
print("Cinsiyet:", cinsiyet)
print("İş Durumu:", is_durumu)
print("Doğum Yılı:", born)
print("Yaş:", sonuc)
print("Boy:", boy, "cm")
print("Kütle:", kilo, "kg")
print("Memleket:", memleket)

if boy < 159:
    print('Biraz spor yapmayı deneyebilirsiniz!')

if boy == 160:
    print('Biraz daha spor yapın lütfen.')


