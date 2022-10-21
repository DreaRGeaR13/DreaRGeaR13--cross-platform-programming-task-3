import random


def random_array(r, c):
    array = []
    for i in range(0, r):
        sub_array = []
        for j in range(c):
            number = random.randrange(0, 100)
            sub_array.append(number)
        array.append(sub_array)
    return array


def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end=' ')
        print()
    print()


def min_max(array):
    min_index_i = 0
    min_index_j = 0
    max_index_i = 0
    max_index_j = 0
    max_value = array[max_index_i][max_index_j]
    min_value = array[min_index_i][min_index_j]
    for i in range(len(array)):
        for j in range(len(array[i])):
            temp = array[i][j]
            if temp > max_value:
                max_value = temp
                max_index_i = i
                max_index_j = j
            if temp < min_value:
                min_value = temp
                min_index_i = i
                min_index_j = j
    return min_value, min_index_i, min_index_j, max_value, max_index_i, max_index_j


def main():
    rowCount = 4
    colCount = 5
    task = True
    array = random_array(rowCount, colCount)
    print("Условие задания:\n"
          "Если макс элемент расположен после минимального,\n"
          "то поменять значения элементов первой и второй строки между собой")

    print_array(array)

    # max_value, min_value = counting(array)
    while True:
        print()
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2, или 3): ')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            print_array(array)

        elif key == '2':
            # проверка выполнения условия

            min_value, min_index_i, min_index_j, max_value, max_index_i, max_index_j = min_max(array)

            if (max_index_i > min_index_i) or ((max_index_i == min_index_i) and (max_index_j > min_index_j)):
                for j in range(rowCount - 1):
                    buff = array[0][j]
                    array[0][j] = array[1][j]
                    array[1][j] = buff

                print()
                print("элементы первой строки поменялиь местами с элементами второй строки")
                print_array(array)
                break


        elif key == '3':
            break  # выход из программы


if __name__ == '__main__':
    main()
