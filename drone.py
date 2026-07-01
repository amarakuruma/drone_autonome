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

def voler():
    global en_vol
    global batterie
    decoller()
    en_vol = True
    print("Le drone commence à voler.")
    while en_vol:
        print("Le drone est en vol.")
        print("altitude actuelle:", altitude)
        print("position actuelle:", position)
        print("batterie restante:", batterie)
        batterie -=10
        if batterie <= 0:
            print("Batterie faible. Le drone doit atterrir.")
            break
voler()
