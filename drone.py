# gestion de drone 
nom = "drone 001"
vitesse = 0 
altitude = 0 
batterie = 100
position ={"x":0,"y":0,"z":0}
en_vol = False # type: ignore
trajet =[
    {"x": 10, "y": 20, "z": 30},
    {"x": 15, "y": 25, "z": 35},
    {"x": 20, "y": 30, "z": 40},
    {"x": 25, "y": 35, "z": 45}
]

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
def voler():
    global en_vol
    global batterie
    decoller()
    en_vol = True
    print("Le drone commence à voler.")
    for point in trajet:
        position["x"] = point["x"]
        position["y"] = point["y"]
        position["z"] = point["z"]
        print("Le drone se déplace vers la position:", position)
        batterie -= 10
    
        if batterie <= 0:
            print("Batterie faible. Le drone doit atterrir.")
            break
    atterrir()

voler()

