import requests
import pandas as pd
import json
import time
from tqdm import tqdm
from dotenv import load_dotenv
import os

# --- Fonction de requête sécurisée avec retries ---
def safe_request(url, headers, params, max_retries=1, delay=0.3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()  # Erreur si status != 200
            return response.json()
        except requests.exceptions.RequestException:
            pass  # on ignore l'erreur, on réessaie
        time.sleep(delay)
    return {}

# --- Chargement des sets ---
df = pd.read_csv("sets.csv")
premiere_colonne = df[df.columns[0]].tolist()

# --- Chargement de la clé API ---
load_dotenv()
key = os.getenv("API_KEY")

pieces_estimation = {}

# --- Boucle principale ---
for set_num in tqdm(premiere_colonne, desc="Traitement des sets"):
    all_parts = []
    url = f"https://rebrickable.com/api/v3/lego/sets/{set_num}/parts/"
    headers = {"Authorization": f"key {key}"}
    params = {"page": 1, "page_size": 1000}

    while True:
        time.sleep(0.3)  # pour respecter le rate-limit
        data = safe_request(url, headers, params)
        if not data:
            break

        results = data.get("results", [])
        if not results:
            break

        all_parts.extend(results)
        params["page"] += 1

    # --- Ajout des pièces au dictionnaire global ---
    for p in all_parts:
        part_num = p["part"]["part_num"]
        quantity = p["quantity"]
        pieces_estimation[part_num] = pieces_estimation.get(part_num, 0) + quantity

# --- Sauvegarde ---
with open("pieces_estimation.json", "w", encoding="utf-8") as f:
    json.dump(pieces_estimation, f, indent=4)
print("fin")
