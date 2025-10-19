letters = [c for c in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789']
morse = ['.-', '-...', '.--', '--.', '-..', '.', '...-',
          '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---',
            '.--.', '.-.', '...', '-', '..-', '..-.', '....', '-.-.',
              '---.', '----', '--.-', '.--.-.', '-.--', '-..-', '..-..', 
              '..--', '.-.-',
            '-----', '.----', '..---', '...--',
            '....-', '.....', '-....', '--...', '---..', '----.']
morse_to_letter = dict(zip(morse, letters))
t = ''
desh_words = input('Введите ваше зашифрованное слово: ').split(' ')
print('Процесс')
for i in range(5):
    print('Дешифровка',(i+1)*'.')
# Удаляем повторяющиеся пустые строки, оставляя только одну
cleaned_list = []
for item in desh_words:
    if item != '':
        cleaned_list.append(item)
    elif cleaned_list and cleaned_list[-1] != '':  # Добавляем только если предыдущий элемент не был пустым
        cleaned_list.append(item)
for desh_word in cleaned_list:
    if desh_word in morse_to_letter:
      t += morse_to_letter[desh_word].lower()
      #print(morse_to_letter[desh_word].lower(),end='')
             
    elif desh_word == '':
      t += ' '
      #print(' ', end='')  # Двойной пробел между словами
    else:
      t += desh_word
      #print(desh_word, end=' ')
print(t.title())