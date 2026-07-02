from fastapi import FastAPI
import drone 

app = FastAPI()

@app.get("/")
def accueil():
    return {"message": "Système de contrôle drone actif"}
@app.get("/etat")
def etat_drone():
    return {
        "nom": drone.nom,
        "vitesse": drone.vitesse,
        "altitude": drone.altitude,
        "batterie": drone.batterie,
        "position": drone.position,
        "en_vol": drone.en_vol
    }
@app.get("/decoller")
def decoller_drone():
    drone.decoller()
    return {"message": "Le drone décolle."} 
@app.get("/atterrir")
def atterrir_drone():  
    drone.atterrir()
    return {"message": "Le drone atterrit."}    
