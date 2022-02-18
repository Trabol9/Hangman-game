# Hangman-game
Data structure hangman game proyect

#Access to different menus

def mainmenu():
    selected = int((input('Select one of the three options:\n1.Modyfy words\n2.Play\n3.Exit\n Your choice:')))
    while (selected <=0) and (selected>3):
        print('Wrong selection')
        selected=int((input('Select one of the three options:\n1.Modyfy words\n2.Play\n3.Exit\n Your choice:')))    
    if selected==1:
       modifywords()
    elif selected==2:
        playmenu()
        mainmenu()
    else:
        print('Thanks for playing\nWe hope you have liked it')
        return exit(0)
        
def modifywords():
    selected2=int((input('Select one of the four options:\n1.Add category\n2.Modify category\n3.Delete category\n4.Return to main menu\nYour choice:')))
    if selected2==1:
        addcategory()
        modifywords()
    elif selected2==2:
        modifycategory()
        modifywords()
    elif selected2==3:
        deletecategory()
        modifywords()
    elif selected2==4:
        mainmenu()


def modifycategory():
    selected3=int((input('Select one of the four options:\n1.Change a Category Name\n2.Add a new Word\n3.Remove a word\n4.Return to main menu\nYour choice:')))
    return selected3

def playmenu():
    print('TODO')
def addcategory():
    print('TODO')
def modifycategory():
    print('TODO')
def deletecategory():
    print('TODO')
    
def main():
    mainmenu()
        
if __name__=='__main__':
    main()

def mod_Category_name(json_Dict,old_Name,new_Name):

    json_Dict[new_Name]=json_Dict[old_Name]
    del json_Dict[old_Name]
    
    return json_Dict 

def add_Word(json_Dict,category_choice,new_Word):

    json_Dict[category_choice].append(new_Word)
    
    return json_Dict

def remove_Word(json_Dict,category_choice,removed_word):

    json_Dict[category_choice].remove(removed_word)
    
    return json_Dict
    
ilustration_list=[" ________\n  |     |\n  |     0\n  |    \|/\n  |     |\n  |    / \ \n ---",
" ________\n  |     |\n  |     0\n  |    \|/\n  |     |\n  |\n ---",
" ________\n  |     |\n  |     0\n  |     |\n  |     |\n  |\n ---",
" ________\n  |     |\n  |     0\n  |\n  |\n  |\n ---",
" ________\n  |\n  |\n  |\n  |\n  |\n ---",
"\n  |\n  |\n  |\n  |\n  |\n ---"]

def play_hangman(i):

    if i == 1: #play from selected category
    
        print(data.keys())
        elected_category=(input("Choose one of the categories: ")).lower()
        
        word_guess = random.choice(list(data[elected_category]))
        
    else: #play from random category

        word_guess = random.choice(list(data[random.choice(list(data))]))
#choose a random word from a random category
    word_decreasing = word_guess.lower()

    print("\nThe word to be guessed is: ",word_guess)

    word_blank = [] #we create the blank spaces
        
    for a in word_guess:
        
        word_blank.append("_")

        victory = False

    for i in range(6,0,-1): #repeat 6 timess
        
        print("-------------------------------------------------------------------------------\n")
        print("You have",i,"tries")

        print(word_blank)

        guess = (input("Guess a letter or the word: ")).lower()

        if guess.lower() in word_guess.lower():
            
            if guess.lower() == word_guess.lower(): #user has guessed the word
                
                print("You won!!!!")
                victory = True
                break
                    
            elif guess.lower() in word_guess.lower(): #user has guessed a letter
                    
                counter=(word_guess.lower()).count(guess.lower())
                
                for numbers in range(0,counter):
                    
                    word_blank[word_decreasing.find(guess.lower())] = guess
                    word_decreasing = word_decreasing.replace(guess.lower(),"-",1)


                print("\n",guess,"is in the word")
                
                counter_02=0
                
                for elements in word_decreasing:
                    
                    if elements.isalpha():
                        
                        counter_02+=1
                        
                if counter_02==0:
                    
                    print("You won!!!!")
                    victory=True
                    
                    break

        else: #user didn't guess anything
            
            print(guess,"is not in the word")
                
        print(ilustration_list[i-1])

    if not victory:
 
        print("You lost!!!!!!!!!")
