print("Привет! Это плохо написанная программа.")
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"
try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        print(f"Количество слов в файле: {len(words)}")
        sentences = content.split('.')
        print(f"Количество предложений в файле: {len(sentences)}")
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        print(f"Самые часто встречающиеся слова: {sorted_words[:5]}")
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
