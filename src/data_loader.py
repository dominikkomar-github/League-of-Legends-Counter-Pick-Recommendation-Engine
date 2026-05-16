import json

def load_counters(): # Load the counters data from the JSON file and return it as a dictionary

    with open("data/counters.json", "r") as f:
        return json.load(f)