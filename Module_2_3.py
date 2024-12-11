my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

while i < len(my_list):
    num = my_list[i]
    i += 1
    if num == 0:
        continue
    elif num < 0:
        break
    elif i == len(my_list):
        print(num)
    else:
        print(num)




