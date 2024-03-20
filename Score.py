import json
import os

POINTS_OF_WINNING = 5

def add_score(name, difficulty):
    points = (difficulty * 3) + POINTS_OF_WINNING

    # Check if the scores file exists
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as file:
            scores = json.load(file)

        # Check if the name already exists in the scores
        if name in scores:
            scores[name] += points
        else:
            scores[name] = points
    else:
        scores = {name: points}

    # Write the updated scores back to the file
    with open("scores.json", "w") as file:
        json.dump(scores, file)

# Example usage:
# if __name__ == "__main__":
#     name = input("Enter your name: ")
#     difficulty = int(input("Enter game difficulty (1-5): "))
#     add_score(name, difficulty)
