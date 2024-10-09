# Function to classify the hero's level based on experience
def classify_level(xp):
    if xp < 1000:
        return "Iron"
    elif 1001 <= xp <= 2000:
        return "Bronze"
    elif 2001 <= xp <= 5000:
        return "Silver"
    elif 5001 <= xp <= 7000:
        return "Gold"
    elif 7001 <= xp <= 8000:
        return "Platinum"
    elif 8001 <= xp <= 9000:
        return "Ascendant"
    elif 9001 <= xp <= 10000:
        return "Immortal"
    else:
        return "Radiant"


# Main function
def main():
    # Store the name and amount of experience of the hero
    name = input("Enter the hero's name: ")
    xp = int(input("Enter the hero's experience points (XP): "))

    # Classify the hero's level
    level = classify_level(xp)

    # Display the output message
    print(f"The hero named {name} is at the level of {level}.")


# Execute the main function
if __name__ == "__main__":
    main()
