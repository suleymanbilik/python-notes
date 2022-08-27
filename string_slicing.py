name = "Suleyman"
surname = "Bilik"
age = "28"

text = "Benim Adım " + name + " ve soyadım " + surname + "." + "Yaşım ise " + age + "."

print(text)
print(text[0])
print(text[-1])
print(text[3])
print(text[0:5])
print(text[5:10])
print(text[5:]) # Bitişi belirtmeden başlangıca kadar.
print(text[:5])
print(text[0:30:2]) # En sondaki değer kadar atlayarak 0 dan başlayarak 2 şer 2 şer atlayarak 30 a kadar gider.
print(text[::2]) #Baştan sona kadar ikişer ikişer atlayarak gider.
print(text[::-1]) #Sondan başa kadar ikişer ikişer atlayarak gider.
