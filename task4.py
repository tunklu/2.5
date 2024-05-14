films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
'Отступники', 'Деревня']
favourite_films = []


film_quantity = int(input('Сколько фильмов хотите добавить? '))

for i in range(0, film_quantity):
    film_name = input('Введите название фильма:')
    if film_name in films:
        favourite_films.append(film_name)
    else:
        print('Ошибка: фильма', film_name, 'у нас нет :(')

print('Ваш список любимых фильмов:', end = ' ')
print(' '.join(favourite_films))
