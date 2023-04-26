def is_palindrome_iterative(word):
    if len(word) < 1:
        return False

    return word == word[::-1]
