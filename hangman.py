import random

def display_word(blank_list):
    """Display the word with spaces between characters."""
    return ' '.join(blank_list)

def making_a_guess():
    """Process the user's guess and update the display."""
    global update_display
    global blank_list
    global chosen_word
    global guesses_left
    global guesses_made
    
    guess = input("Make a guess? ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        return
    
    correct_guess = False
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            blank_list[index] = guess
            correct_guess = True
    
    if not correct_guess:
        print(f"There is no '{guess}', sorry.")
        update_display += 1
        guesses_left -= 1
    else:
        print(f"Good guess! The letter '{guess}' is in the word.")
    
    guesses_made += 1
    return

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

animal_list = [
    "ant", "antelope", "baboon", "bear", "beaver", "bee", "beetle", "bison", "blowfish", "buffalo",
    "butterfly", "camel", "canary", "capybara", "cat", "cheetah", "chimpanzee", "chicken", "cow",
    "coyote", "crab", "crocodile", "deer", "dolphin", "dog", "donkey", "duck", "eagle", "elephant",
    "falcon", "flamingo", "fox", "frog", "giraffe", "goat", "goldfish", "goose", "hummingbird",
    "gorilla", "hamster", "hedgehog", "hippopotamus", "horse", "hyena", "iguana", "impala", "jaguar",
    "kangaroo", "koala", "leopard", "lion", "lizard", "moose", "monkey", "mouse", "octopus",
    "ostrich", "otter", "panda", "parrot", "pig", "platypus", "pigeon", "porcupine", "rabbit",
    "raccoon", "rat", "seal", "shark", "sheep", "shrimp", "skunk", "snake", "squirrel", "turkey",
    "turtle", "whale", "zebra", "seagull", "jackal", "goat", "butterfly", "chipmunk", "panther", "bear",
    "sea lion", "penguin", "alligator", "wombat", "mole", "ladybug", "vulture","hare", "meercat",
    "badger", "swordfish", "pufferfish", "tuna", "oryx", "puma", "reindeer", "bulbul", "yak", "swan"
    "stork", "lamp", "catfish", "starfish", "maina"]

country_list = [
    "austrlia", "russia", "canada", "germany", "china", "france", "japan", " india", "sudan",
    "turkey", "iran", "iraq", "oman", "maldives", "vietnam", "singapore", "denmark", "sweden",
    "nairobi", "ankara", "burkina faso", "brazil", "sri lanka", "malaysia", "indonesia", "italy",
    "greece", "uganda", "victoria", "pakistan", "bangladesh", "nepal", "bhutan", "afghanistan",
    "spain", "mexico", "somalia", "zambia", "tanzania", "poland", "iceland", "canada", "austria",
    "australia", "england", "algeria", "andorra", "ghana", "botswana", "brunei", "belarus", "belgium"
    "camaroon", "belize", "argentina", "bahrain", "egypt", "syria", "uruguay", "cyprus", "hungary",
    "norway", "bahamas", "guatemala", "saudi arabia", "macau", "paraguay", "azerbaijan", "namibia",
    "south korea", "north korea", "uzbekistan", "georgia", "kyrgyzstan", "latvia", "netherlands",
    "laos", "new zealand", "lithuania", "luxembourg", "portugal", "qatar", "panama", "suriname",
    "peru", "bolivia", "croatia", "palau", "yemen", "jamaica", "jordan"]

flower_list = [
    "azalea", "aster","begonia", "daisy", "daffodil", "dandelion", "lily", "hyacinth", "poppy", "peony",
    "lotus", "lavendar", "vinca rosia", "buttercup", "primrose", "calendula", "datura", "geranium",
    "chrisanthamum", "jasmine", "orchid", "cherry blossom", "dahlia", "iris", "rose", "plumeria",
    "tulip", "marigold", "sunflower", "magnolia", "freesia", "bluebell", "hibiscus", "moss rose",
    "wisteria", "rhododendron" ]

fruits_list = [
    "apple", "apricot", "mango", "papaya", "guava", "lychee", "banana", "dragonfruit", "custard apple",
    "pineapple", "orange", " persimmon", "kiwi", "cherry", "strawberry", "blueberry", "mulberry", "plum",
    "black currant", "mangosteen", "jackfruit", "watermelon", "melon", "pear", "tomato","grape",
    "pomegranate", "sapodilla", "white currant", "velvet apple", "raspberry", "passion fruit",
    "nectarine", "avocado", "cucumbers", "pumpkin", "tangerine", "tamarind", "fig", "java apple",
    "wolfberry", "dewberry", "elderberry", "clementine", "mandarin", "prune", "hackberry", "mulberry",
    "cranberry", "red currant", "jujube", "durian", "lemon", "coconut", "olive", "gooseberry" ]

chosen_word = list(random.choice(animal_list))
blank_list = ['_'] * len(chosen_word)

update_display = 0
guesses_left = 6
guesses_made = 0

print("Welcome to Hangman!")
print(HANGMANPICS[update_display])
print(display_word(blank_list))
print('')
print(f"Guesses left: {guesses_left}")
print('')
print('')

while update_display < 6:
    making_a_guess()
    print(HANGMANPICS[update_display])
    print(display_word(blank_list))
    print('')
    print(f"Guesses left: {guesses_left}")
    print('')
    print('')
    
    if '_' not in blank_list:
        print("YOU WIN!")
        print(f"You guessed the word '{''.join(chosen_word)}' in {guesses_made} guesses.")
        break
else:
    print("GAME OVER. The word was: " + ''.join(chosen_word))
