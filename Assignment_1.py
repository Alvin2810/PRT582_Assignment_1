from english_words import english_words_lower_set
import random

word_list = list(english_words_lower_set)
word = random.choice(word_list)
word = word.lower()
print("\n"+ word +"\n")
