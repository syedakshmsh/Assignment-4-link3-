import random


stage = ['''
  -------
  |     |
  |
  |
  |
  |
  -------

''',
'''
  -------
  |     |
  |     O
  |
  |
  |
  -------
''',
'''
  -------
  |     |
  |     O
  |     |
  |
  |
  -------

''',
'''
  -------
  |     |
  |     O
  |    /|
  |
  |
  -------

''',
'''
  -------
  |     |
  |     O
  |    /|\\
  |
  |
  -------

''',
'''
  -------
  |     |
  |     O
  |    /|\\
  |    /
  |
  -------

''',
'''
  -------
  |     |
  |     O
  |    /|\\
  |    / \\
  |
  -------

''']

word = ["apple","mango","banana", "orange", "grapes","kivi","peach"]
chosen_word = random.choice(word)
word_display = ('_' for _ in chosen_word)
guess_letter = []
lives = len(stage)-1
print('welcom to hangman')
print("guess the fruit words")

while True:
    print(" ".join(word_display))
    guess = input("Guess a letter:").lower()

    if not guess.isalpha() or len(guess) != 1:
     print("Enter a valid letter")
     continue
    if  guess in guess_letter:
       print("you are already guess in guess_letter:")
       continue
    guess_letter.append(guess)

    if guess in chosen_word:
       print(f"Good guess! {guess} is in the word")
       for index, letter in enumerate(chosen_word):
          if letter == guess:
           word_display[index] = guess

    else:
       print(f"Sorry you {guess} not in the word:")
       print(stage[len(stage) -lives -1])
       lives -= 1
       print(f"you have {lives} lives left")

       if lives == 0:
          print(stage[lives])
          print(f"You lose! The word was {chosen_word}:")
          break
    

