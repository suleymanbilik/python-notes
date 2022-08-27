# 7000 liralık bir ürünümüz olacak. Buna KDV eklemek istersek.

print(7000 + (7000*0.18))

# Ya da 

print(7000*1.18)


# Ürün oluşturalım.

urun1 = 7000
urun2 = 8500
print(urun1 + (urun1*0.18))
print(urun2 + (urun2*0.18))


# Kdv yi de otomatik değer vermeden yapmak için

kdv = 0.18

print(urun1 + (urun1 * kdv))

# değişkenler sayıyla başlamaz. Örneğin 3urun

# değişkenler boşluk içeremez. Örneğin urun 3

# değişkenlerde @ kullanılamaz. Örneğin urun@

# değişkenlerde türkçe karakter kullanılamaz. Büyük küçük harf duyarlılığı vardır.

# değişkenleri aynı satırda kodlayabiliriz. Örneğin

a, b, c = 20,30,40
print(a,b,c)

x = 1

y = 2.5

print(type(y))
print(type(x))

name = "Suleyman"
print(type(name))
