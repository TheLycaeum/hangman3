# hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)

def mask_word(s):
    n = len(s)
    l = "*"*n
    return l

def tries_left(n=10):
    while(n >= 0):
        if n == 0:
            l = print("too bad try next time!!")
        else:
            l = print("chances left {}".format(n))
        n = n - 1
        return l

def wrong_guess_word(word, s):
    guess_word = []
    if s not in word:
        print('\nGuess so far {}'.format(s))
        guess_word.append(s)
    return guess_word

def ask_to_type(word):
    match_letter = []
    s = input("Enter a letter: ")
    check1 = s.isalpha()
    check2 = s.islower()
    if (check1 == True and check2 == True):
        for i in word:
            if s == i:
                match_letter.append(s)
                print(match_letter)
                continue
            else:
                wrong_guess_word(word,s)
                continue
    else:
        print("please enter a alphabetic in lower ")
        return s

def main():
    print("Welcome to hangman game")
    word = get_secret_word(word_file="/usr/share/dict/words")
    while True:
        l1 = mask_word(word)
        print(l1)
        tries_left(10)
        ask_to_type(word)



if __name__ == '__main__':
    main()

            

            
        


    




 
