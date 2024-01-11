#hangman

import random

word_list = [
    'palette', 'animal', 'whirlpool', 'toucan', 'zucchini', 'honeydew', 'giraffe',
    'universe', 'mongoose', 'elephant', 'geometric', 'illustrate', 'nuance',
    'vignette', 'harmony', 'oilpaint', 'vulture', 'raspberry', 'vertex', 'oilpaint',
    'pentagon', 'sculpture', 'kiwifruit', 'xylophone', 'sphere', 'isosceles', 'hexagon',
    'watercolor', 'jigsaw', 'nectarine', 'quokka', 'tangerine', 'realism', 'landscape',
    'gallery', 'flamingo', 'lemonade', 'yellowfin', 'labyrinth', 'xenopus', 'underpaint',
    'triangle', 'zebra', 'diamond', 'mosaic', 'giraffe', 'juxtapose', 'grapefruit', 'papaya',
    'elderberry', 'mosaic', 'quadrant', 'squirrel', 'animal', 'strawberry', 'buffalo',
    'octagon', 'banana', 'jellyfish', 'cheetah', 'kangaroo', 'narwhal', 'figure', 'drawing',
    'gallery', 'quill', 'cherry', 'dolphin', 'orange', 'yellowfin', 'umbrella', 'leopard',
    'rectangle', 'rhinoceros', 'fresco', 'canvas', 'xylograph', 'balloon', 'vignette',
    'elephant', 'animal', 'kiln', 'octagon', 'hippopotamus', 'penguin', 'labyrinth',
    'kaleidoscope', 'texture', 'easel', 'apple', 'diamond', 'artist', 'brushes', 'octopus',
    'watermelon', 'walrus', 'circle', 'yacht', 'mandarin', 'ellipse']

hangman = ['''
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
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

lives = 6
word = word_list[random.randint(0,99)]
word_aux = [i for i in word]
guess = ["_" for i in range(len(word))]



while lives > 0:
    aux = guess[:]
    chosen_letter = input("Choose a letter \n").lower()
    for i in range(0,len(word)):
        if word[i] == chosen_letter:
            guess[i] = chosen_letter
        else:
            pass
    if aux == guess:
        print(hangman[len(hangman) - lives])
        lives -=1
        print(f'You have {lives} lives left')
    else:
        pass
    if word_aux == guess:
        print("You won")
        break
    print(''.join(guess))


