from src.CLI import get_team, display_results
from src.logic import calculate_scores, top_picks
from src.data_loader import load_counters


def main(): # Main function to run the LoL matchup recommendation engine

    counters = load_counters()

    while True:

        print("\n--- LoL Matchup Recommendation Engine ---")
        print("1. Run prediction")
        print("2. Exit")

        choice = input("Choose option: ").strip()

        if choice == "2":
            print("Exiting...")
            break

        if choice != "1":
            print("Invalid option.")
            continue

        enemy_team = get_team(counters)

        if len(enemy_team) == 0:
            print("No champions entered.")
            continue

        scores = calculate_scores(enemy_team,counters)
        top_3 = top_picks(scores)
        display_results(enemy_team, top_3)

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()