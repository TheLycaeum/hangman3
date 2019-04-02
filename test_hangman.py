# test_hangman.py

import hangman

# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))

def test_mask_word():
    assert hangman.mask_word("elephant", []) == "********"
    assert hangman.mask_word("elephant",['e']) == "e*e*****"

def test_status():
    actual_status = hangman.status('elephant', ['x', 'l', 'e'], 7)
    expected_status = """Secret word : ele*****
    guessed letters : e l x
    turns : 7
    """
    actual_status = expected_status

def test_guess_word():
    guesses = ['x', 'l', 'e']
    ret = hangman.guess_word('elephant', guesses, 'p', 8)
    assert ret == 8
    assert guesses == ['x', 'l', 'e', 'p']

def test_guess_word_repetitions():
    guesses = ['x']
    ret = hangman.guess_word('elephant', guesses, 'x', 8)
    assert ret == 8
    assert guesses == ['x']

