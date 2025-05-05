import random

def player(prev_play, opponent_history=[]):
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return random.choice(['R', 'P', 'S'])

    # Predict next move based on opponent's most frequent play
    most_common = max(set(opponent_history), key=opponent_history.count)
    return counter_moves[most_common]
