def calculate_scores(enemy_team, counters): # Calculate scores for each champion based on the enemy team and counters data
    scores = {}

    for enemy in enemy_team:

        if enemy in counters:
            matchup_data = counters[enemy]
            
            for champion, winrate in matchup_data.items(): # Calculate the advantage score based on the winrate (50% is neutral, above 50% is an advantage)
                advantage = 50 - winrate
                
                if champion in scores: # If the champion already has a score, add the advantage to it, otherwise set the score to the advantage
                    scores[champion] += advantage
                else:
                    scores[champion] = advantage

    return scores


def top_picks(scores): # Sort the champions by their scores and return the top 3 picks

    sorted_scores = sorted(scores.items(),key=lambda x: x[1],reverse=True) # Sort the scores in descending order (higher score means better pick)
    
    return sorted_scores[:3] # Return the top 3 picks