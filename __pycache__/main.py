import greetings
import calculations

greetings.greet()
name = greetings.get_name()
print(f"Привет, {name}!")

filename = "sample.txt"
word_count = calculations.count_words(filename)
sentence_count = calculations.count_sentences(filename)
top_words = calculations.count_word_frequency(filename)
vovels_and_consonant= calculations.count_vowels_and_consonants(filename)

print(f"Количество слов в файле: {word_count}")
print(f"Количество предложений в файле: {sentence_count}")
print(f"Самые часто встречающиеся слова: {top_words}")
print(f"количество гласных/согласных: {vovels_and_consonant}")

