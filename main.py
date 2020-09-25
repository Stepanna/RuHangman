from words import ru_word_list
from random import choice


def get_word():
    word = choice(ru_word_list)
    return word.upper()


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Давай сыграем в Виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries > 0:
        guess = input("Отгадай букву или слово: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Ты уже загадывал букву', guess)
            elif guess not in word:
                print('Буквы', guess, 'нет в этом слове')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Молодец, буква', guess, 'есть в этом слове!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Ты уже отгадал слово', guess)
            elif guess != word:
                print(guess, 'не загаданное слово')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Не корректная попытка")
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print('Поздравляю, ты отгадал слово', word)
    else:
        print('Попытки закончились, я задумал слово', word)


def display_hangman(tries):
    stages = [
        """
        -------
        |     |
        |     O
        |    \\|/
        |     |
        |    / \\
        -
        """,
        """
        -------
        |     |
        |     O
        |    \\|/
        |     |
        |    / 
        -
        """,
        """
        -------
        |     |
        |     O
        |    \\|/
        |     |
        |    
        -
        """,
        """
        -------
        |     |
        |     O
        |    \\|
        |      |
        |    
        -
        """,
        """
        -------
        |     |
        |     O
        |     |
        |     |
        | 
        -
        """,
        """
        -------
        |     |
        |     O
        |
        |
        |
        -
        """,
        """
        -------
        |     |
        | 
        |
        |
        |
        -
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Сыграем еще? (Д/Н) ").upper() == 'Д':
        word = get_word()
        play(word)


if __name__ == '__main__':
    main()
