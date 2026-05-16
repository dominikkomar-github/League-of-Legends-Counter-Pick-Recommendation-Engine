# League of Legends Counter Pick Recommendation Engine

A Python CLI tool that recommends optimal champion picks based on enemy team composition using a generated matchup dataset and a scoring system.

------------------------------------------------------------

## PROJECT OVERVIEW

This project simulates a simplified recommendation system similar to tools like u.gg.

It takes an enemy team composition, evaluates matchup data, and returns the best champion picks based on statistical advantage.

The goal is to demonstrate:
- data processing
- algorithm design
- modular Python architecture
- recommendation system logic

------------------------------------------------------------

## HOW IT WORKS

1. Load champion list from champions.json
2. Generate matchup dataset (counters.json)
3. User inputs up to 5 enemy champions
4. Matchup winrate data is retrieved for each enemy champion
5. Winrates are converted into advantage scores:

    advantage score = 50 - winrate

## WHY THIS WORKS:
- 50% winrate = even matchup
- Below 50% = enemy is stronger (positive counter value)
- Above 50% = favorable matchup

This allows the system to consistently rank champion effectiveness against an enemy team.

------------------------------------------------------------

## SCORING SYSTEM

For each enemy champion:
- Retrieve all counter matchups
- Convert winrates into advantage scores
- Aggregate scores across all enemies

Final result:
- Champions ranked by total advantage score

------------------------------------------------------------

## FEATURES

- CLI-based user input system
- JSON-based dataset storage
- Weighted scoring system
- Modular architecture (CLI, logic, data loader)
- Scalable champion pool
- Easy upgrade path to real API data

------------------------------------------------------------

## SETUP

1. Generate dataset:
   python random_wr_generator.py

2. Run application:
   python main.py

------------------------------------------------------------

## EXAMPLE OUTPUT

Enemy team: Ahri, Zed, Jinx

Top 3 picks:
1. Lissandra (advantage score: 12.4)
2. Malphite (advantage score: 10.8)
3. Galio (advantage score: 9.6)

------------------------------------------------------------

## TECH STACK

- Python 3
- JSON for data storage
- CLI interface

------------------------------------------------------------

## FUTURE IMPROVEMENTS

- Integration with Riot Games API for real matchup data
- Role-based filtering (top, jungle, mid, etc.)
- Team synergy scoring system
- Web interface (Flask / FastAPI)
- Patch-based dataset versioning
- Improved recommendation weighting system

------------------------------------------------------------

## PURPOSE

This project demonstrates:
- algorithm design
- data transformation
- modular system architecture
- CLI application development
- recommendation logic based on statistical data

------------------------------------------------------------

## NOTES

This project uses a procedurally generated dataset to simulate matchup winrates. It is structured to be easily replaced with real-world data sources in the future.
