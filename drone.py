import datetime 
def enregistrer_log(message):
    with open("logs.txt", "a", encoding="utf-8") as fichier:
        fichier.write(f"[{datetime.datetime.now()}]{message}\n")
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
enregistrer_log(f"Nom: {nom}")
enregistrer_log(f"Vitesse: {vitesse}")
enregistrer_log(f"Altitude: {altitude}")
enregistrer_log(f"Batterie: {batterie}")
enregistrer_log(f"Position: {position}")
enregistrer_log(f"En vol: {en_vol}")

def decoller():
    global en_vol
    global altitude
    if not en_vol:
        en_vol = True
        altitude = 50
        enregistrer_log(f"Le drone décolle. Altitude actuelle: {altitude}")
    else:
        enregistrer_log("Le drone est déjà en vol.")
def atterrir():
    global en_vol
    global altitude
    if en_vol:
        en_vol = False
        altitude = 0 
        enregistrer_log(f"Le drone atterrit. Altitude actuelle: {altitude}")
    else:
        enregistrer_log("Le drone est deja au sol")
def voler():
    global en_vol
    global batterie
    decoller()
    en_vol = True
    enregistrer_log("Le drone commence à voler.")
    for point in trajet:
        position["x"] = point["x"]
        position["y"] = point["y"]
        position["z"] = point["z"]
        batterie -= 10
        enregistrer_log(f"Le drone se déplace vers la position: {position}. Batterie restante: {batterie}%")    
        if batterie <= 0:
            enregistrer_log("Batterie faible. Le drone doit atterrir.")
            break
    atterrir()

voler()
#========== systeme de controle  drone ==============
while True:
    print("1. Décoller")
    print("2. voler")
    print("3. Atterrir")
    print("4. Afficher état")
    print("5. Quitter")
    input_utilisateur = input("choisissez une option:")
    if input_utilisateur =="1":
      decoller()
    elif input_utilisateur =="2":
      voler()
    elif input_utilisateur =="3":
      atterrir()
    elif input_utilisateur =="4":
     print(f"Nom: {nom}")
     print(f"Vitesse: {vitesse}")
     print(f"Altitude: {altitude}")
     print(f"Batterie: {batterie}")
     print(f"Position: {position}")
     print(f"En vol: {en_vol}")
    elif input_utilisateur =="5":
     break 
     print("Au revoir!")
 