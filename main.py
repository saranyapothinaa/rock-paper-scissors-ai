from RPS_game import play, quincy, kris, random_player
from RPS import player

# Test player vs bots
print("vs Quincy:", play(player, quincy, 1000))
print("vs Kris:", play(player, kris, 1000))
print("vs Random:", play(player, random_player, 1000))

# Run unit tests
# from test_module import test_player
# test_player(player)
