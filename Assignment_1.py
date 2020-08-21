from english_words import english_words_lower_set
import random

def generate_random_word():
    word_list = list(english_words_lower_set)
    word = random.choice(word_list)
    word = word.lower()
    return word

generated_word = generate_random_word()
print("\n"+ generated_word + "\n")

blank_spaces=[]
for letters in generated_word:
    blank_spaces.append("_")
print(" ".join(blank_spaces))
print("\nNumber of letters: "+ str(len(generated_word)))
print("Number of blank space: "+ str(len(blank_spaces))+"\n")

lives = 5
no_changes_made=[]
no_changes_made.extend(blank_spaces)

while "_" in blank_spaces:
    print("\nLives: "+str(lives)) 
    guess = input("\nGuess a letter: ").lower()
    
    if no_changes_made == blank_spaces:
        lives = lives-1
    for i in range(len(generated_word)):
        if generated_word[i] == guess:
            blank_spaces[i] = guess
        no_changes_made[i] = blank_spaces[i]
    
    print(" ".join(blank_spaces))

    