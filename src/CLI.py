def get_team(counters): # Get the enemy team from user input, ensuring that the champions are valid and not duplicated
    enemy_team = []

    while len(enemy_team) < 5:
        name = input(
            "Enter enemy champion (or X to stop): ").title()

        if name == "X":
            break

        if name not in counters:
            print("Champion not found.")
            continue

        if name in enemy_team:
            print("Champion already added.")
            continue
        enemy_team.append(name)

    return enemy_team


def display_results(enemy_team, top_3): # Display the enemy team and the recommended picks with their advantage scores

    print("\nEnemy team:")
    print(", ".join(enemy_team))

    print("\nRecommended picks:")

    for i, (champion, score) in enumerate(top_3, start=1):

        print(
            f"{i}. {champion} "
            f"(advantage score: {round(score, 2)})")