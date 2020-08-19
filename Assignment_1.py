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

while "_" in blank_spaces:
    guess = input("\nGuess a letter: ").lower()
    for i in range(len(generated_word)):
        if generated_word[i] == guess:
            blank_spaces[i] = guess
    print(" ".join(blank_spaces))