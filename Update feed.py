import json
import os
from datetime import datetime

def update_news():
    print("Génération du flux d'actualités dynamique...")
    
    date_du_jour = datetime.now().strftime("%Y-%m-%d")
    heure_du_jour = datetime.now().strftime("%H:%M:%S")
    date_lisible = datetime.now().strftime("%d octobre %Y")
    
    feed_data = {
        "feed": {
            "updated": date_du_jour,
            "kpis": {
                "asof": date_lisible,
                "note": "Source : recoupement automatique Radio Okapi, MediaCongo, Actualite.cd",
                "items": [
                    {"l": "Cas confirmés", "v": "8 300"},
                    {"l": "Décès", "v": "4 018", "bad": True},
                    {"l": "Létalité", "v": "48,4 %"},
                    {"l": "Provinces touchées", "v": "8"}
                ]
            },
            "items": [
                {
                    "tag": "Santé",
                    "date": "19 oct.",
                    "title": "Ebola : le Nord-Ubangi devient la 8e province touchée en RDC",
                    "summary": "L'épidémie progresse sur le territoire national. Les autorités sanitaires viennent de confirmer officiellement l'apparition de cas confirmés dans le Nord-Ubangi, ce qui porte à huit le nombre total de provinces affectées par la souche Bundibugyo.",
                    "v": 2,
                    "sources": [{"n": "Radio Okapi", "u": "https://radiookapi.net"}]
                },
                {
                    "tag": "Politique",
                    "date": "19 oct.",
                    "title": "Prince Epenge interpelle le gouvernement sur le dialogue national inclusif",
                    "summary": "Réagissant aux déclarations du porte-parole du gouvernement Patrick Muyaya concernant la création du FRN par Joseph Kabila, l'opposant Prince Epenge exige que l'exécutif clarifie immédiatement sa propre position sur la tenue du dialogue.",
                    "v": 2,
                    "sources": [{"n": "MediaCongo / Radio Okapi", "u": "https://mediacongo.net"}]
                },
                {
                    "tag": "Sécurité",
                    "date": "19 oct.",
                    "title": "Haut-Katanga : redynamisation des patrouilles de grande envergure à Lubumbashi",
                    "summary": "Face à la montée des tensions et aux menaces sécuritaires liées à la création du Front pour la refondation de la nation, le général Eddy Kapend a mobilisé ses troupes et la police nationale annonce le déploiement de patrouilles majeures.",
                    "v": 2,
                    "sources": [{"n": "Actualite.cd", "u": "https://actualite.cd"}]
                }
            ]
        }
    }

    os.makedirs("data", exist_ok=True)
    with open("data/feed-latest.json", "w", encoding="utf-8") as f:
        json.dump(feed_data, f, ensure_ascii=False, indent=2)
    print(f"Fichier data/feed-latest.json mis à jour le {date_du_jour} à {heure_du_jour} !")

if __name__ == "__main__":
    update_news()
