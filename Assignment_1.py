from english_words import english_words_lower_set
import random
# declaring variables
lives_left = 5
no_changes_made=[]
used_words_list=[]
blank_spaces=[]

#defining the function to create a random word
def generate_random_word():
    word_list = list(english_words_lower_set)
    word = random.choice(word_list)
    word = word.lower()
    return word

#defining the function to check if the guess is a letter or not
def isnotaletter(guess):
    if guess.isalpha() == False:
        return True
    elif len(guess) > 1:
        return True
    else:
        return False

generated_word = generate_random_word() #creating a random word
print("\n"+ generated_word + "\n")

#creating blank spaces for each letter in the word
for letters in generated_word:
    blank_spaces.append("_")
print(" ".join(blank_spaces))

print("\nNumber of letters: "+ str(len(generated_word)))
print("Number of blank space: "+ str(len(blank_spaces))+"\n")

no_changes_made.extend(blank_spaces)

while "_" in blank_spaces:
    print("\nLives left: "+str(lives_left)) 

    guess = input("\nGuess a letter: ")
    guess.lower()

    used_words_list.append(guess) #adding the newly guessed character into the used words list

    #checking if the guess is in the word
    for number in range(len(generated_word)): 
        if generated_word[number] == guess:
            blank_spaces[number] = guess
    
    #if no changes are made then the guess was not correct and 1 life is deducted
    if no_changes_made == blank_spaces:
        print("\nSorry you guessed wrong")
        lives_left = lives_left-1  
    
    #checking if the guess is a letter or not
    if isnotaletter(guess):
        lives_left+=1
        print("\nPlease make sure that you are entering a single valid letter rather than symbols, numbers or a string of characters")
    
    #checking if the player has ran out of lives 
    if lives_left < 0:
        print("\nYou have run out of lives\n\nThe word was:  "+ generated_word+"\n")
        break 
    
    for number in range(len(blank_spaces)):
        no_changes_made[number] = blank_spaces[number]
        
    print("\n"+" ".join(blank_spaces))
    print("\nused words: "+ str(used_words_list)+"\n")

if "_" not in blank_spaces:
    print("\nCongratulations you have found the word\n")
    