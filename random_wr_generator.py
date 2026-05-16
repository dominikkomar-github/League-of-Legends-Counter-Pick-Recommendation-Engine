import json
import random


def load_champions():
    with open("data/champions.json", "r", encoding="utf-8") as f:
        return json.load(f)


def generate_matchups(champions, counters_per_champ=5):
    data = {}

    for champ in champions:
        opponents = [c for c in champions if c != champ]

        selected = random.sample(opponents, counters_per_champ)

        matchups = {}

        for enemy in selected:
            # realistic-ish winrate range
            winrate = round(random.uniform(44.0, 49.8), 1)
            matchups[enemy] = winrate

        data[champ] = matchups

    return data


def main():
    champions = load_champions()

    dataset = generate_matchups(champions)

    with open("data/counters.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print("Generated counters.json for", len(champions), "champions")


if __name__ == "__main__":
    main()