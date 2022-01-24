#!/bin/python3

print("Anna neliön korkeus")
korkeus = int( input() )
rivi = 0
while rivi < korkeus:
    sarake = 0
    while sarake < rivi:
        # Tulosta "X" ilman enter painallusta
        # Huom! tämä vaatii python3 - tulkin joka asetettu päälle rivillä 1
        print(" ", end='')
        sarake = sarake + 1
    
    # Tulosta enter
    print("X")
    rivi = rivi + 1