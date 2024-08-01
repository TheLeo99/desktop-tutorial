def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


root_word = "stop"
other_words = "Unstoppable", "Stopped", "Stopping", "Apostle"


result = single_root_words(root_word, *other_words)
print(result)
