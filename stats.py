def count_words(input_text):
    words = input_text.split()
    #print(words)
    return len(words)

def count_characters(input_text):
    characters = {}
    for char in input_text:
        if char.lower() not in characters:
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1
    return characters

def sort_on(characters):
    return characters["num"]

def sort_characters(characters):
    character_list = []
    for char in characters:
        char_stats = {"char": char,
                        "num": characters.get(char)}
        character_list.append(char_stats)
    
    character_list.sort(reverse=True, key=sort_on)
    return character_list
