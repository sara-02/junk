"""TODOS:
* Load list from file.
* Time out raw_input.
* Have a score for the game(partial marking alllowed).
* Make the print statements more decorative.
* Optimise the string checking algo.
* Add instructions to play.
* If a word is guess in the same game, do not repeat it.
* If the user gusses all words in the same game add a print statment for that.
* Log and display the time taken for individual word and the time spent on the game.
* Better expcetion Handling."""

from random import choice


def play_game():
    word_list = ["apple", "mango", "books", "analytics", "games"]
    random_word = list(choice(word_list))
    word_len = len(word_list)
    turns_allowed = word_len + 3

    answer_list = ["__ "] * word_len
    print answer_list

    while(turns_allowed):
        user_guess = raw_input("Enter a char:: ")
        for index, char in enumerate(random_word):
            if user_guess is not None and char == user_guess:
                answer_list[index] = char
        print answer_list
        if answer_list == random_word:
            print "## You Won! ##"
            break
        turns_allowed = turns_allowed - 1
    else:
        print "@@ You Lost! @@"


def main():
    play_game()
    play_more = raw_input("Enter y to play:: ")
    while(play_more.lower()[0:1] == "y"):
        play_game()
        play_more = raw_input("Enter y to play:: ")


if __name__ == '__main__':
    main()
