# Luodaan kilpikonna
import turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

# Tulosta ruudulle seuraavat tekstit
print("Mihin suuntaan haluat siirtää kilpikonnaa?")
print("Kirjoita oikea, vasen, ylös tai alas")

# Ota käyttäjän syöte vastaan
suunta = input()

# Jos käyttäjän syöte oli "oikea", liiku oikealle. 
if suunta == "oikea":
  kilpikonna.forward(50)

# Jos käyttäjän syöte oli "vasen", liiku vasemmalle.
if suunta == "vasen":
  kilpikonna.left(180)
  kilpikonna.forward(50)
  
# Jos käyttäjän syöte oli "ylös", liiku ylös.
if suunta == "ylös":
  kilpikonna.left(90)
  kilpikonna.forward(50)

# Jos käyttäjän syöte oli "alas", liiku alas.
if suunta == "alas":
  kilpikonna.right(90)
  kilpikonna.forward(50)

# Lisää tänne uusia valintalauseita.
# Huomaathan että valintalauseen alla olevat komennot sisennetään tabulaattorilla
# tai välilyönneillä.