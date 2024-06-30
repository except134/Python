def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


