word_input = input('Введите слово:')

word_reversed = "".join(reversed(word_input))

if word_input == word_reversed:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
