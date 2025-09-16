import requests
import pandas as pd
import pprint as pp
import json
import time
from tqdm import tqdm
from dotenv import load_dotenv
import os

df = pd.read_csv("sets.csv")
premiere_colonne = df[df.columns[0]].tolist()
load_dotenv()
key = os.getenv("API_KEY")
pieces_estimation = {}

for set_num in tqdm(premiere_colonne):
    all_parts =[]
    url = f"https://rebrickable.com/api/v3/lego/sets/{set_num}/parts/"
    headers = {"Authorization": f"key {key}"}

    params = {
        "page": 1,
        "page_size": 1000  # max possible
    }
    time.sleep(1)
    while True:
        time.sleep(1)
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            break
        data = response.json()
        results = data.get("results", [])
        if not results:
            break
        all_parts.extend(results)
        params["page"] += 1

    for p in all_parts:
        parts = p["part"]["part_num"]
        q = p["quantity"]
        if parts not in pieces_estimation:
            pieces_estimation[parts] = 0
        pieces_estimation[parts] += q

pp.pprint(pieces_estimation)
with open("pieces_estimation.json", "w", encoding="utf-8") as f:
    json.dump(pieces_estimation, f, indent=4)  # indent=4 pour que le JSON soit lisible
print("✅ Dictionnaire sauvegardé dans pieces_estimation.json")
