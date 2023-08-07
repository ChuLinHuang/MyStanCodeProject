"""
File: hangman_ext.py
Name: Chu-Lin Huang
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. 先叫出答案
    2. 將答案隱藏 "---"
    3. 將使用者輸入字母統一轉成大寫
    4. 建立 function，若使用者猜對字母，就將字母做替換，將替換好的字串 return 到 main function
    5. 逐一更新細節 ex：判斷是否輸入字母、是否重複輸入字母、猜錯次數是否達到 7次
    """
    ans = random_word()
    block = ""  # 將答案用'---'隱藏
    for i in range(len(ans)):
        block += "-"
    # print(ans) 寫程式的過程中用來檢查用的
    live = 0  # 有 7 次機會，一開始從 0，到 7 時強制跳出
    your_situation(live)
    print("The word looks like: " + block)
    print("You have 7 wrong guesses left.")
    player_guess = input("Your guess: ")
    player_guess_upper = turn_upper(player_guess)

    record = block  # record 重新清空重填

    while record != ans:  # 如果沒猜到答案，就重複下去
        if player_guess.isdigit():  # 判斷是否為數字
            print("Illegal format !!")
            player_guess = input("Your guess: ")
            player_guess_upper = turn_upper(player_guess)

        elif len(player_guess) >= 2:  # 判斷是否不只一個字母f
            print("Illegal format !!")
            player_guess = input("Your guess: ")
            player_guess_upper = turn_upper(player_guess)

        elif ans.find(player_guess_upper) != -1:  # 代表有猜到字母
            record = record_answer(ans, record, player_guess_upper)
            print("You are correct!!")
            if record == ans:  # 每次猜完，檢查答案是否已經出來
                print("The answer is: " + ans)
                break
            else:
                print("You have " + str(7 - live) + " wrong guess left")
                your_situation(live)
                print("The word looks like: " + record)
                player_guess = input("Your guess: ")
                player_guess_upper = turn_upper(player_guess)
        else:
            live += 1  # 沒猜到字母，機會少一次
            print("There is no " + str(player_guess) + " in the word")
            if live != 7:  # 檢查是否出局
                print("You have " + str(7 - live) + " wrong guess left")
                your_situation(live)
                print("The word looks like: " + record)
                player_guess = input("Your guess: ")
                player_guess_upper = turn_upper(player_guess)
            else:
                your_situation(live)
                print("You are completely hung QQ")
                print("The word was: " + ans)
                break


def record_answer(ans, record, player_guess):  # 用於暫存目前猜到的答案，將對應位置的 '-' 改為對應的字母
    updated_ans = ""
    for i in range(len(ans)):
        ch = ans[i]
        if ch == player_guess:
            updated_ans += player_guess
        else:
            updated_ans += record[i]

    return updated_ans


def turn_upper(player_guess):  # 用於將字母統一轉成大寫
    ans = ""
    if player_guess.islower() != -1:
        ans = player_guess.upper()
    else:
        ans = player_guess
    return ans


def your_situation(live):
    if live == 0:
        gallows()
    if live == 1:
        gallows()
        head()
    if live == 2:
        gallows()
        head()
        body()
    if live == 3:
        gallows()
        head()
        body_hand()
    if live == 4:
        gallows()
        head()
        body_hands()
    if live == 5:
        gallows()
        head()
        body_hands()
        one_foot()
    if live ==6:
        gallows()
        head()
        body_hands()
        two_feet()
    if live ==7:
        gallows()
        dead_head()
        body_hands()
        two_feet()


def dead_head():
    print("  ", end='')
    for i in range(6):
        print("-", end='')
    print("")
    print(" ", end='')
    for i in range(1):
        print(" Q", end="")
        print("   ", end="")
        print(" Q", end="")
        print("")
    print("  ", end='')
    for i in range(6):
        print("-", end='')
    print("")


def body_hands():
    for i in range(3):
        for j in range(3-i):
            print(" ", end='')
        print("/", end='')
        for j in range(i):
            print(" ", end='')
        print("||", end='')
        for k in range(i):
            print(" ", end='')
        print("\\")


def body_hand():
    for i in range(3):
        for j in range(3-i):
            print(" ", end='')
        print("/", end='')
        for j in range(i):
            print(" ", end='')
        print("||")


def two_feet():
    for i in range(2):
        for j in range(3-i):  # 空格數量由多到少遞減
            print(" ", end='')
        print("/", end='')
        for j in range(i+1):  # 空格數量由少到多遞減
            print("  ", end='')
        print("\\", end='')

        print("")


def one_foot():
    for i in range(2):
        for j in range(3-i):  # 空格數量由多到少遞減
            print(" ", end='')
        print("/", end='')

        print("")


def body():
    for i in range(3):
        for j in range(4):
            print(" ", end='')
        print("||")


def head():
    print("  ", end='')
    for i in range(6):
        print("-", end='')
    print("")
    print(" ", end='')
    for i in range(1):
        print(" =", end="")
        print("   ", end="")
        print(" =", end="")
        print("")
    print("  ", end='')
    for i in range(6):
        print("-", end='')
    print("")


def gallows():
    for i in range(9):
        print("=", end='')

    print('')

    for i in range(2):
        for j in range(4):
            print(" ", end='')
        print("|")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
