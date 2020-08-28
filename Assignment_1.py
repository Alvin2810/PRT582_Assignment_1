from english_words import english_words_lower_set
import random
# declaring variables
lives = 5
no_changes_made=[]
used=[]
blank_spaces=[]
def generate_random_word():
    word_list = list(english_words_lower_set)
    word = random.choice(word_list)
    word = word.lower()
    return word

def isnotaletter(guess):
    if guess.isalpha() == False:
        return True
    elif len(guess) > 1:
        return True
    else:
        return False

generated_word = generate_random_word()
print("\n"+ generated_word + "\n")

for letters in generated_word:
    blank_spaces.append("_")
print(" ".join(blank_spaces))

print("\nNumber of letters: "+ str(len(generated_word)))
print("Number of blank space: "+ str(len(blank_spaces))+"\n")

no_changes_made.extend(blank_spaces)

while "_" in blank_spaces:
    print("\nLives: "+str(lives)) 
    guess = input("\nGuess a letter: ").lower()
    used.append(guess)
    for number in range(len(generated_word)):
        if generated_word[number] == guess:
            blank_spaces[number] = guess
    if no_changes_made == blank_spaces:
        print("\nSorry you guessed wrong")
        lives = lives-1  
     
    if isnotaletter(guess):
        lives+=1
        print("\nPlease make sure that you are entering a single valid letter rather than symbols, numbers or a string of characters")
    
    if lives < 0:
        print("\nYou have run out of lives\n\nThe word was:  "+ generated_word+"\n")
        break 

    for number in range(len(blank_spaces)):
        no_changes_made[number] = blank_spaces[number]
        
    print("\n"+" ".join(blank_spaces))
    print("\nused words: "+ str(used)+"\n")

if "_" not in blank_spaces:
    print("\nCongratulations you have found the word\n")
    