def shift_list(steps, list_in):
    for i in range(0, steps):
      list_in.insert(0, list_in.pop(-1))
    return list_in

list_ = [1, 2, 3, 4, 5]
k = 1


print(shift_list(k, list_))
