import json

# Charger le JSON
with open("pieces_estimation.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Trier par valeurs (croissant)
sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

# Sauvegarder dans un nouveau fichier
with open("pieces_estimation_sorted.json", "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, indent=4, ensure_ascii=False)

print("✅ Fichier trié sauvegardé dans pieces_estimation_sorted.json")