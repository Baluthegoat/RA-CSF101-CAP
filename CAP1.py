##############################
# Tashi Penjor
# Section A 
# 02230306
#############################
# REFERENCES
# https://www.w3schools.com/python/ref_file_readlines.asp#:~:text=The%20readlines()%20method%20returns,the%20number%20of%20lines%20returned
# https://www.geeksforgeeks.org/count-number-ways-reach-given-score-game/
# https://codereview.stackexchange.com/questions/281633/calculate-score-of-rock-paper-scissors-advent-of-code-2022-day-2
##############################
# Solution
#
#
###############################

# Define the mapping between letters and moves
moves = {'rock': 'A', 'paper': 'B', 'scissors': 'C'}

# Define the scoring system
score_map = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_scores = {'lose': 0, 'draw': 3, 'win': 6}

def draw(opponent_move):
    return opponent_move

def lose(opponent_move):
    return 'rock' if opponent_move == 'scissors' else 'scissors' if opponent_move == 'paper' else 'paper'

def win(opponent_move):
    return 'scissors' if opponent_move == 'rock' else 'rock' if opponent_move == 'scissors' else 'paper'

def calculate_round_score(opponent_move, desired_outcome):
    # Determine the correct move to make
    opponent_move_value = moves
    
    if desired_outcome == 'draw':
        correct_move = draw(opponent_move_value)
    elif desired_outcome == 'lose':
        correct_move = lose(opponent_move_value)
    else:
        correct_move = win(opponent_move_value)

    # Calculate the score for the round
    score = score_map[correct_move]
    if correct_move == opponent_move_value:
        score += outcome_scores['win'] # You won
    else:
        score += outcome_scores['lose']
    
    return score

def calculate_total_score(filename):
    total_score = 0

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        opponent_move, desired_outcome = line.strip().split()
        print(f"Opponent Move: {opponent_move}, Desired Outcome: {desired_outcome}")
        round_score = calculate_round_score(opponent_move, desired_outcome)
        total_score += round_score

    return total_score

#Read the input.txt file
def read_input():
    filename = 'input_6_cap1.txt'
    total_score = calculate_total_score(filename)
    print(f"The total score is: {total_score}")


# Call the read_input function to start the game
read_input()



















