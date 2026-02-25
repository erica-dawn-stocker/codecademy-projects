# function to add letter scores to score word
def score_word(word):
  # initialize point total
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter]
  return point_total

# function that adds a played word to the list of words played, takes in player and word
def play_word(player, word):
  player_to_words[player].append(word)
  return player_to_words

# function to add a word score to a plauyer's points
def update_point_totals():
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create dictionary to match letters to their score
letter_to_points = dict(zip(letters, points))

# Add spaces and score value of 0
letter_to_points[" "] = 0

# Record words played by player
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "LexiCon": ["ERASER", "BELLY", "HUSKY"],
  "ProfReader": ["ZAP", "COMA", "PERIOD"]
}