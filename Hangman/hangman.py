import random

def hangman(word = None):
    if word == None:
        print("word generated")
        word = generate_random_word()

    #remove space if input have any
    word = word.replace(" ","")
    lifes = 7
    guessed_letter = []
    current_word = ["_"]*len(word)
    
    while lifes != 0:
        print("-------------------------------------")
        print("guess a letter")

        my_guess = input().lower()
        #input check
        if len(my_guess) != 1:
            print("what! why?")
            continue
        
        #when guessed wrong
        if (my_guess not in word):
            print("Your letter",my_guess,"is not in the word")
            lifes = lifes -1

        #when guessed word already picked
        elif (my_guess in guessed_letter):
            print("Your letter",my_guess,"is already picked")
            lifes = lifes -1
        #when picked right
        else:
            print("good pick")
            
            index = find(word,my_guess)
            for i in index:
                current_word[i] = my_guess
        
        guessed_letter.append(my_guess)    
        print("you have ",lifes," lifes remaining")
        print("you have used these letters ", guessed_letter)
        print("current word : ",current_word)
        print(hangman_visualization(lifes))
        #check if won
        if ("".join(current_word) == word):
            print("you win")
            return
            
    print("you lose, the correct answer is :",word)

                
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def generate_random_word():
    word_list = ["apple", "banana", "carrot", "dog", "elephant", "flower", "guitar", "house", "igloo", "jungle"]
    random_word = random.choice(word_list)
    return random_word

def hangman_visualization(lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      
           |      
           |    
           |      
           |     
           -
        """
    ]
    
    return stages[lives]


hangman("pepe poo poo")