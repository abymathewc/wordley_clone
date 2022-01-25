import os
import random
import sys
from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)

# word file shenanigans
WORD_FILE = "words_list_sorted.txt"
# For creating exe using pyinstaller . In bundled mode, the exe looks for data file in MEIPASS variable.
# So, if that is available use that variable as the file path
# Else ( which basically means executing directly from the script and not as an exe, use the current directory as the path)
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
word_file_path = os.path.abspath(os.path.join(bundle_dir,WORD_FILE))
with open(word_file_path, "r") as wf:
    word_list = wf.readlines()
#The above word_list will have newline character as well. Strip it out in order not to have
#issues while comparing with the guess word.
word_list = [word.strip() for word in word_list]

class GameTile:
    def __init__(self,random_num):
        self.game_over = False
        self.game_tile = [['_' for j in range(6)] for i in range(6)]
        self.color_pallette = [['' for j in range(6)] for i in range(6)]
        self.word = word_list[random_num]

    def print_game_tile(self):
        #for game_tile_row in self.game_tile:
        #    print(str(game_tile_row))
        #print (self.game_tile)
        # TODO: Should figure out a pythonic way
        for row in range(6):
            print("[",end='')
            for index in range(5):
                #print(f"{self.color_pallette[row][index]}{self.game_tile[row][index]},",end='')
                print(f"{self.game_tile[row][index]},",end='')
            print("]")

    def insert_word(self,row,guess_word):
        #.game_tile[row] = guess_word.split()
        for _ in range(5):
            self.game_tile[row][_] = guess_word[_]

    def check_word(self,row,guess_word):
        if guess_word == self.word:
            print("***You guessed it correct***")
            self.game_over = True
            for index,letter in enumerate(self.game_tile[row]):
                #self.game_tile[row][index] = Fore.GREEN + self.game_tile[row][index]
                self.game_tile[row][index] = Fore.GREEN + letter
            return
        else :
            for index,_ in enumerate(guess_word):
                if guess_word[index] == self.word[index]:
                    self.game_tile[row][index] = Fore.GREEN + self.game_tile[row][index]
                elif guess_word[index] in self.word:
                    self.game_tile[row][index] = Fore.YELLOW + self.game_tile[row][index]


def main():
    random_num = random.randint(0,5000)
    game = GameTile(random_num)
    game.print_game_tile()
    #print(game.word)
    #print (word_list[:25])
    # Start with guesses
    row = 0

    while (not game.game_over and row<6):
        guess_word = input(" Enter you guess : ")
        while (len(guess_word)!= 5) :
            print(f" '{guess_word}' is not of length 5.Please enter again")
            guess_word = input(" Enter you guess : ")
        while (guess_word not in word_list):
            print(f" '{guess_word}' is not a valid word.Please enter again")
            guess_word = input(" Enter you guess : ")
        game.insert_word(row, guess_word)
        game.check_word(row, guess_word)

        game.print_game_tile()

        row = row+1
    if (row>=6 and not game.game_over) :
        print (" Exhausted the number of tries. Exiting...")
        print (" The word was : ", game.word)
        sys.exit(0)
    if (game.game_over):
        print(" Congrats..")
        sys.exit(0)

if __name__=="__main__":
    main()