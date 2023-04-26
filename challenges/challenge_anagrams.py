def sort(array, low, high):
    if len(array) == 1:
        return array

    if high > low:
        index = division(array, low, high)
        sort(array, low, index - 1)
        sort(array, index + 1, high)


def division(array, low, high):
    pivot_index = low - 1
    pivot_value = array[high]

    for j in range(low, high):
        if array[j] <= pivot_value:
            pivot_index += 1
            array[pivot_index], array[j] = array[j], array[pivot_index]

    array[pivot_index + 1], array[high] = array[high], array[pivot_index + 1]

    return pivot_index + 1


def is_anagram(first_string, second_string):
    first_str = list(first_string.lower())
    second_str = list(second_string.lower())
    sort(first_str, 0, len(first_str) - 1)
    sort(second_str, 0, len(second_str) - 1)

    first = "".join(first_str)
    second = "".join(second_str)

    if (first_string == "" or type(first_string) is None
            or second_string == "" or type(second_string) is None):
        return (first, second, False)
    verify = first == second
    return (first, second, verify)
