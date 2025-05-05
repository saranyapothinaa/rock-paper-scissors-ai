import random

def random_player(prev_play):
    return random.choice(['R', 'P', 'S'])

def quincy(prev_play):
    options = ['R', 'P', 'S']
    return options[0]

def kris(prev_play, player_history=[]):
    if prev_play:
        player_history.append(prev_play)
    if len(player_history) < 1:
        return "R"
    return player_history[-1]

def play(player1, player2, num_games=1000, verbose=False):
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0

    for _ in range(num_games):
        p1_play = player1(p2_prev)
        p2_play = player2(p1_prev)

        if p1_play == p2_play:
            result = "Tie"
        elif (p1_play == 'R' and p2_play == 'S') or \
             (p1_play == 'S' and p2_play == 'P') or \
             (p1_play == 'P' and p2_play == 'R'):
            result = "Player 1 wins"
            p1_score += 1
        else:
            result = "Player 2 wins"
            p2_score += 1

        if verbose:
            print(f"P1: {p1_play} | P2: {p2_play} => {result}")

        p1_prev = p1_play
        p2_prev = p2_play

    print("Final Score:", p1_score, "vs", p2_score)
    return p1_score / num_games
