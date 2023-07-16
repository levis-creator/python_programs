numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def is_the_same(list):
    list_index = int(len(list)-1)
    if list[0]==list[list_index]:
        print(True)
    else:
        print(False)

is_the_same(numbers_y)