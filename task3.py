from heapq import nlargest


card_list = [3070, 2060, 3090, 3070, 3090]
card_quantity = len(card_list)
max_count = 0

print('Количество видеокарт:', card_quantity)

for i in range(0, card_quantity):
    print('Видеокарта', i+1, card_list[i])

max_ = (max(card_list))
max_count = card_list.count(max_)

for i in range(0, max_count):
    card_list.remove(max_)

print(card_list)
