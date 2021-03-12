import random



def game():
    words = ["python", "java", "kotlin", "javascript"]
    n = random.randrange(4)
    pcword = words[n]

    wordset = set(pcword)
    word = ""
    for m in pcword:
        word += "-"
    
    wordlist = list(word)
    again = set()

    print("H A N G M A N")
    
    hp = 0
    while hp < 8:
        print()
        print("".join(wordlist))
    
        letter = input("Input a letter: >")
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter.islower() != True:
            print("Please enter a lowercase English letter.")
        elif letter in again:
            print("You've already guessed this letter")
        else:
            if letter in wordset:
                for f in range(len(pcword)):
                    if letter == pcword[f]:
                        wordlist[f] = letter
            else:
                print("That letter doesn't appear in the word")
                hp += 1

        again.add(letter)
        if "".join(wordlist) == pcword:
            print("You guessed the word "+ pcword + "! \nYou survived! \n")
            break
    if "".join(wordlist) != pcword:
        print("You lost! \n")

def menu():
    while True:
        command = input("Type \"play\" to play the game, \"exit\" to quit:")
        if command == "play":
            game()
        elif command == "exit":
            exit()

menu()
