Задание 1

word = input('Введите слово')
word_index_1 = None
word_index_2 = None
if len(word) % 2 == 0:
    word_index_1 = int((len(word)/2-1))
    middle_lets = word[word_index_1]+word[word_index_1+1]
    print(middle_lets)
elif len(word) % 2 != 0:
    word_index_2 = int(len(word)//2)
    print(word[word_index_2])
else: print('Ошибка')

Задание 2
boys = ['max', 'peter', 'sam']
girls = ['kate', 'ann', 'nancy', 'lucy']
sorted_boys = sorted(boys)
sorted_girls = sorted(girls)
boys_len = len(boys)
girls_len = len(girls)
if boys_len == girls_len:
    print('Идеальные пары')
    for boy,girl in zip(sorted_boys, sorted_girls):
        print(f'{boy} и {girl}')
else :
    print('Внимание, кто-то может остаться без пары!')




