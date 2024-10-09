def calculate_rank(wins, losses):
    balance = wins - losses

    if wins < 10:
        rank = "Iron"
    elif 10 <= wins <= 20:
        rank = "Bronze"
    elif 21 <= wins <= 50:
        rank = "Silver"
    elif 51 <= wins <= 80:
        rank = "Gold"
    elif 81 <= wins <= 90:
        rank = "Diamond"
    elif 91 <= wins <= 100:
        rank = "Legendary"
    else:  # wins >= 101
        rank = "Immortal"

    return balance, rank


# Example usage
player_wins = int(input("Enter the number of wins: "))
player_losses = int(input("Enter the number of losses: "))
balance_victories, level = calculate_rank(player_wins, player_losses)

print(f"The player has a balance of {balance_victories} and is at the rank of {level}.")
