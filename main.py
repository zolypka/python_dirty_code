import module1
import module2

module1.greet()
name = module1.get_name()
print(f"Привет, {name}!")

filename = "sample.txt"
word_count = module2.count_words(filename)
sentence_count = module2.count_sentences(filename)
top_words = module2.count_word_frequency(filename)
vovels_and_consonant= module2.count_vowels_and_consonants(filename)

print(f"Количество слов в файле: {word_count}")
print(f"Количество предложений в файле: {sentence_count}")
print(f"Самые часто встречающиеся слова: {top_words}")
print(f"количество гласных/согласных: {vovels_and_consonant}")
