# gestion de drone 
nom = "drone 001"
vitesse = 0 
altitude = 0 
batterie = 100
position = {"x": 0, "y": 0, "z": 0}
en_vol = False # type: ignore

print("initialisation du drone")
print("nom :", nom)
print("vitesse:", vitesse)
print("altitude:", altitude)
print("batterie:", batterie)
print("position:", position)
print("en-vol:", en_vol)

def decoller():
    global en_vol
    global altitude
    if not en_vol:
        en_vol = True
        altitude = 50
        print("Le drone décolle.")
        print("altitude actuelle:", altitude)
    else:
        print("Le drone est déjà en vol.")

decoller()
def atterrir():
    global en_vol
    global altitude
    if en_vol:
        en_vol = False
        altitude = 0 
        print("Le drone atterrit.")
        print(" altitude actuelle:", altitude)
    else:
        print("Le drone est deja au sol")
atterrir()
