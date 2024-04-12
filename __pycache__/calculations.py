import FileReader

def count_words(filename):
    content = FileReader.read_file(filename)
    words = content.split()
    return len(words)

def count_sentences(filename):
    content = FileReader.read_file(filename)
    sentences = content.split('.')
    return len(sentences)

def count_word_frequency(filename):
    content = FileReader.read_file(filename)
    words = content.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:5]

def count_vowels_and_consonants(filename):
    content = FileReader.read_file(filename)
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vowel_count = 0
    consonant_count = 0
    for char in content:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.lower() in consonants:
            consonant_count += 1
    return vowel_count, consonant_count