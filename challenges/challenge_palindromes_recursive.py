def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if len(word) == 1:
        return True
    if word[low_index] == word[high_index]:
        if len(word) == 2:
            return True
        return is_palindrome_recursive(word[1:-1], 0, len(word[1:-1]) - 1)
    else:
        return False
