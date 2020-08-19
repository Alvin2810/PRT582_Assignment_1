from english_words import english_words_lower_set
import random

def generate_random_word():
    word_list = list(english_words_lower_set)
    word = random.choice(word_list)
    word = word.lower()
    return word

generated_word = generate_random_word()
print("\n"+ generated_word + "\n")

display=[]
display.extend(generated_word)

for i in range(len(display)):
    display[i]= "_"
print(" ".join(display))

print(len(generated_word))

print(len(display))