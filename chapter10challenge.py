
# 例
def hangman(word):
    wrong = 0
    stages = ["",
              "_________         ",
              "|        |        ",
              "|        |        ",
              "|        o        ",
              "|      ／|＼　　　",
              "|      ／ ＼      ",
              "|                 "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = char
            rletters[cind] = '$'

        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))


hangman("cat")

---------------------------------------------------------------------------------------------------------------

#チャレンジ
def hangman():
    import random
    num = random.randint(0,2)
    ans = ["cat","dog","rabbit"]
    word = ans[num]
    number = 7
    wrong = 0
    stages = ["",
              "_________         ",
              "|        |        ",
              "|        |        ",
              "|        o        ",
              "|      ／|＼　　　",
              "|      ／ ＼      ",
              "|                 "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")
    print(board)
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね(あと{}回間違ったゲームオーバー！)".format(number)
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = char
            rletters[cind] = '$'

        else:
            wrong += 1
            number -= 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

        
hangman()

---------------------------------------------------------------------------------------------------------------

#著者の答え
import random


def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()





















