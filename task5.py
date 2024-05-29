container_list = []
container_quantity = int(input('Количество контейнеров:'))
i = 0

while i < container_quantity:
    container_weight = int(input('Введите вес контейнера:'))
    if (200 > container_weight):
        if 0 == i:
            container_list.append(container_weight)
            i += 1
        elif (0 < i) and container_list[i-1] >= container_weight:
            container_list.append(container_weight)
            i += 1
        else:
            print('Вес контейнера не может быть больше предыдущего')
    else:
        print('Вес контейнера должен быть меньше 200')

new_container_weight = int(input('Введите вес нового контейнера:'))
new_container_number = 0

if new_container_weight > container_list[0]:
        new_container_number = 1
elif new_container_weight <= container_list[-1]:
        new_container_number = (len(container_list)+1)
else:
    for index in range(1, len(container_list)):
        if new_container_weight <= container_list[(index-1)] and new_container_weight > container_list[index]:
            new_container_number = (index+1)
            break


print('Номер, который получит новый контейнер:', new_container_number)
