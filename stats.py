def get_number_words(text):
    return len(text.split())

def get_number_chars(text):
    all_chars = {}
    text.lower()
    for char in text:
        char = char.lower()
        if char in all_chars: all_chars[char] += 1
        else: all_chars[char] = 1
    return all_chars

def get_sorted_list_dict(dictionary):
    result = []
    for key in dictionary:
        aux_dict = {
            "char" : key,
            "num" : dictionary[key]
        }
        result.append(aux_dict)
    result.sort(reverse=True, key=sort_on)
    return result


def sort_on(items):
    return items["num"]