# Input is some string sentence
# Повернути char який зусітрчаєтся масикмально у цьому речені

def get_max_repeated_char(sentence: str):
    my_dict = {}
    for char in sentence:
        if char == " ":
            continue
        elif char.lower() in my_dict:
            my_dict[char.lower()] += 1
        else:
            my_dict[char.lower()] = 1

    my_tup = tuple(my_dict.items())

    sorted_tuple = sorted(my_tup, key=lambda x: x[1], reverse=True)
    key, _ = sorted_tuple[0]
    return key
