def is_anagram(first_string, second_string):
    first_arr = sort(list(first_string.lower()))
    first_string = "".join(first_arr)
    second_arr = sort(list(second_string.lower()))
    second_string = "".join(second_arr)

    if not first_string or not second_string:
        return (first_string, second_string, False)
    return (first_string, second_string, first_string == second_string)


def sort(letters):
    if len(letters) <= 1:
        return letters
    mid = letters[0]
    right = [letter for letter in letters[1:] if letter < mid]
    left = [letter for letter in letters[1:] if letter >= mid]
    return sort(right) + [mid] + sort(left)
