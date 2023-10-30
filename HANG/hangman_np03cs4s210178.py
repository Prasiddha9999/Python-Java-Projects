# Coding Challenge 3, hangman_np03cs4s210178.py
# Name: Prasiddha Regmi 
# Student No: np03cs4s210178


import random
import string
import json




def load_words(bool):
    if bool:
        print("Loading wordlist from a file: words.txt")
        
    try:
        with open("words.txt", "r") as WORDLIST_FILENAME:
            list_of_words = WORDLIST_FILENAME.read().split()
    except IOError:
        print("The file was not loaded.")
        
    if bool:  
        print(len(list_of_words)," words loaded.")
    
    WORDLIST_FILENAME.close()
    return list_of_words





"""
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
"""
def choose_random_word(all_words):
    random_word = random.choice(all_words)
    return random_word









def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    length = 0
    for chr in letters_guessed:
        for ltr in word:
            if chr == ltr:
                length += 1
    if len(word) == length:
        return True
    else:
        return False



    

def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """
    list = []
    for chr in word:
        list.append(chr)
    guessed_list = []
    for i in range (len(list)):
        guessed_list.append(' _ ')
    for x in range(len(list)):
        for y in range(len(letters_guessed)):
            if list[x] == letters_guessed[y]:
                guessed_list[x] = letters_guessed[y]
    sep = ''
    result = sep.join(guessed_list)
    return result      
        



def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    Words_for_guessing = string.ascii_lowercase
    for letters in letters_guessed:
        if letters in Words_for_guessing:
            Words_for_guessing = Words_for_guessing.replace(letters, "")

    return Words_for_guessing



# Checking for error in user inputs
def user_input():
    User_guess = input('Please Guess a letter: ')
    User_guess = User_guess.lower()
    while User_guess not in string.ascii_lowercase or len(User_guess)>1:
            print("Invalid input, You may have entered two alphabet or you may have entered characters other than alphabets")
            User_guess = input('Please Guess a letter: ')
            User_guess = User_guess.lower()
    return User_guess



#Score by multiplying the unique numbers in words to Guesses left
def Score(word, No_of_Guesses_left):
    letters = string.ascii_lowercase
    unique_letters = 0
    for ltr in letters:
        if ltr in word:
            unique_letters += 1
    score = unique_letters * No_of_Guesses_left
    return score



def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    

    
    P_choice = input("Do you want to Play (p) view the leaderboard (l) or quit (q): ")
    while P_choice != "p" and P_choice != "l" and P_choice != "q":
        print ("Invalid input. Try again.")
        P_choice = input("Do you want to Play (p) view the leaderboard (l) or quit (q): ")

        
    if P_choice == "p":
        name = input("What is your name? ")
        name = name.upper()
        print("I am thinking of a word that is {0} letters long".format(len(word)))
        print('')
        print("-------------------------")
        print('')
     
        Guessed_letters = []
        Number_of_guesses = 6
        Is_guessed = is_word_guessed(word, Guessed_letters )

        
        while Number_of_guesses > 0 and Is_guessed == False:
            
            print(f"You have {Number_of_guesses} guesses left.")
            Available_letters = get_remaining_letters(Guessed_letters)
            print(f"Available letters: {Available_letters}")
            User_guess = user_input()
            
            if User_guess not in  Guessed_letters:
                Guessed_letters.append(User_guess)
                if User_guess in word:
                    Word_guessed = get_guessed_word(word, Guessed_letters)
                    print(f"Good Guess: {Word_guessed}")
                else:
                    Word_guessed = get_guessed_word(word, Guessed_letters)
                    print(f"Oops! That letter is not in my word: {Word_guessed}")
                    if User_guess in ('a', 'e', 'i', 'o', 'u'):
                        Number_of_guesses -= 2
                    else:
                        Number_of_guesses -= 1
                    
            else:
                Word_guessed = get_guessed_word(word, Guessed_letters)
                print(f"Oops! You've already guessed that letter: {Word_guessed}")
                
            print('')   
            print('---------------------')
            print('')
            Win_or_not = is_word_guessed(word, Guessed_letters)
            if Win_or_not == True:
                print("Congratulations, you won!")
                score = Score(word, Number_of_guesses)
                print (f"Your total score for this game was : {score}")
                
                P_best = get_score(name)
                
                if score>P_best:
                    user_choice = input("A new personal best! Would you like to save your score(y/n): ")
                    while user_choice != "y" and user_choice != "n" :
                        print("Invalid input. Try again.")
                        user_choice = input("A new personal best! Would you like to save your score(y/n): ")
                        
                    if user_choice == "y":
                        save_score(name, score)
                        print("Ok, your score has been saved.")
                        print("")
                        wordlist = load_words(False)
                        word = choose_random_word(wordlist)
                        print("")
                        hangman(word)
                    else:
                         print ("Thanks for playing.")
                         print("")
                         wordlist = load_words(False)
                         word = choose_random_word(wordlist)
                         print("")
                         hangman(word)
                    
                Is_guessed = True
                
            if Number_of_guesses == 0:
                print(f"Sorry, you ran out of guesses. The word was: {word}")
                print("")
                wordlist = load_words(False)
                word = choose_random_word(wordlist)
                print("")
                hangman(word)

    if P_choice == "l":
        try:
            fp = open("score.txt")
            contents = fp.read()
            if contents != "":
                y = json.loads(contents)
                Names = y.keys()
                print("Score             Name")
                print("--------------------------------")
                for nm in Names:
                    sc = y[nm]
                    print(f"{sc}                {nm}")
                fp.close()
            else:
                print("No ones score has been saved yet.")

        except IOError:
            print("File does not exist.")

            
        print("")
        wordlist = load_words(False)
        word = choose_random_word(wordlist)
        print("")
        hangman(word)
            


    if P_choice == "q":
        print ("Thanks for playing, Goodbye!")

        
def get_score(Name):
    try:
        fp = open('score.txt', 'r')
                        
        data = (fp.read())
        
        if Name in data:
            score = data[Name]
            return score
        else:
            score = 0
            return score
        fp.close()
        
    except IOError:
        print('File doesnot exist.')



def save_score(name, score):
    try:
        fp = open('score.txt', 'r')
        data = fp.read()
        if data != "":
            js = json.loads(data)
            js[name] = score
            fp.close()
        
            file = open('score.txt','w')
            json.dump(js, file)
            file.close()
            
        else:
            Dt = {}
            Dt[name] = score
            file = open('score.txt','w')
            json.dump(Dt, file)
            file.close()
            
    except IOError:
        print('File doesnot exist.')


    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program

if __name__ == "__main__":
    wordlist = load_words(True)
    word = choose_random_word(wordlist)
    print("")
    print("Welcome to Hangman Ultimate Edition")
    hangman(word)

