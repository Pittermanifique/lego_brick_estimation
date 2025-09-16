# Lego Pieces Estimation

Ce script permet de récupérer toutes les pièces présentes dans une liste de sets LEGO à partir de l’API [Rebrickable](https://rebrickable.com/) et de les stocker dans un fichier JSON avec le nombre total de chaque pièce.

---

## Prérequis

- Python 3.8+
- Installer les packages nécessaires :

```bash
pip install requests pandas tqdm python-dotenv
```

- Avoir un fichier `.env` contenant votre clé API Rebrickable :

```
API_KEY=VOTRE_CLE_API
```

- Avoir un fichier `sets.csv` avec la liste des numéros de sets LEGO dans la **première colonne**.

---

## Utilisation

```bash
python script.py
```

- Le script parcourt tous les sets de `sets.csv`.
- Pour chaque set, il récupère toutes les pièces et leurs quantités.
- Le dictionnaire final est sauvegardé dans `pieces_estimation.json`.

---

## Exemple de sortie

```json
{
    "3001": 12,
    "3002": 5,
    "3003": 8
}
```

Chaque clé correspond au numéro de la pièce et chaque valeur au nombre total présent dans tous les sets listés.

---

## Notes

- Le script inclut un `time.sleep(1)` pour éviter de surcharger l’API.
- Les sets sont traités avec une barre de progression via `tqdm`.

---

## Contribuer

Les contributions sont les bienvenues !  
- Créez un fork du projet.
- Faites vos modifications sur une branche.
- Ouvrez une pull request décrivant vos changements.

---

## Licence

Ce projet est sous licence MIT.
