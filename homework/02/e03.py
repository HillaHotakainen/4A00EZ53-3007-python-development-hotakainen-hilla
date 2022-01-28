#Tämän sisälle voi laittaa ' mutta ei "
a = "hello"
#Tämän sisälle voi laittaa " mutta ei '
b = 'hello'
c = """hello
          world"""
d = '''hello
          world'''
e = "Matti"
paino = 25.112312

print(a)
print(b)
print(c)
print(d)
print(a, e)
print(f"Hello {e}, your bmi is {paino:.2f}")
print(e[0], e[4])
print(len(e))

kokeilu_jutu = "haha hasua"
#keskittää stringin
print(kokeilu_jutu.center(30))
#etsii stringistä tietyn merkin tai merkkijonon
print(kokeilu_jutu.find("hasua"))
#tarkistaa onko kaikki stringin merkit aakkosia ja palauttaa joko kyllä tai ei
print(kokeilu_jutu.isalpha())
#tarkistaa ovatko kaikki merkit stringissä pieniä
print(kokeilu_jutu.islower())
#vaihtaa määritellyn merkkijonon toiseksi
print(kokeilu_jutu.replace("hasua", "jänää"))
#tarkistaa alkaako stringi tietyllä merkkijonolla
print(kokeilu_jutu.startswith("hehe"))
#Vaihtaa pienet isoiksi ja isot pieniksi
print(kokeilu_jutu.swapcase())

print("\n")
print("Give a:", end="")
nimi_a=input()

print("Give b:", end="")
nimi_b=input()

print(id(nimi_a))
print(id(nimi_b))

print(nimi_a == nimi_b)
print((id(nimi_a))is(id(nimi_b)))
