# League-of-Legends-Counter-Pick-Recommendation-Engine
A Python CLI tool that recommends optimal champion picks based on enemy team composition using a generated matchup dataset and a scoring system.

---

## How it works

- User enters up to 5 enemy champions
- The program loads matchup data from `counters.json`
- Each matchup has a winrate value
- Winrates are converted into advantage scores using:
    advantage = 50 - winrate
    (Winrates are converted into an "advantage score" so the program can rank champions consistently.

    A 50% winrate represents an even matchup.
    
    To measure how strong a counter is, the system compares each winrate to 50%:
    
    - If a champion has a **low winrate vs an enemy**, it means the enemy counters them strongly
    - If a champion has a **high winrate vs an enemy**, it means they perform well into them
    
    The formula used is:
    advantage score = 50 - winrate


- Scores are summed across the enemy team
- Top 3 highest scoring champions are returned as recommended picks

---

## Features

- CLI-based input system
- JSON-based dataset storage
- Weighted scoring system
- Modular structure (CLI, logic, data loader)
- Scalable to full champion pool
- Easy upgrade path to real API data

---

## Project structure

lol-counter-picker/
│
├── main.py
├── random_wr_generator.py
│
├── src/
│ ├── CLI.py
│ ├── logic.py
│ ├── data_loader.py
│
├── data/
│ ├── champions.json
│ ├── counters.json
│
└── README.md

---

## Setup

### 1. Generate dataset
```bash
python random_wr_generator.py
```
```bash
python main.py
```
### Example Output

Enemy team: Ahri, Zed, Jinx

Top 3 picks:
1. Lissandra (advantage score: 12.4)
2. Malphite (advantage score: 10.8)
3. Galio (advantage score: 9.6)
