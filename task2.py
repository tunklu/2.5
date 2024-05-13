tournament_members = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []

for (index, item) in enumerate(tournament_members):
    if 0 == (index % 2):
        first_day.append(item)

print(first_day)
