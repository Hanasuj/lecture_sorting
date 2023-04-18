import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        datas = []
        l1 = []
        l2 = []
        l3 = []
        all_data = file.readlines()
        data_lines = [thing.strip() for thing in all_data]
        titles = (data_lines.pop(0)).split(",")
        for idx in range(len(data_lines)):
            thingies = data_lines[idx].split(",")
            l1.append(thingies[0])
            l2.append(thingies[1])
            l3.append(thingies[2])
        datas.append(l1)
        datas.append(l2)
        datas.append(l3)
        data = dict(zip(titles, datas))
        return data

def selection_sort(list_of_numbers, direction=True):
    size = len(list_of_numbers)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if list_of_numbers[j] < list_of_numbers[min_index]:
                min_index = j
        (list_of_numbers[ind], list_of_numbers[min_index]) = (list_of_numbers[min_index], list_of_numbers[ind])
    if direction == True:
        return list_of_numbers
    else:
        return list_of_numbers[::-1]

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        for j in range(0, len(list_of_numbers) - i - 1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
    return list_of_numbers
def main():
    pass


if __name__ == '__main__':
    main()
    read_data("numbers.csv")
    print(selection_sort(['88', '36', '21', '54', '99', '1', '81', '18', '21', '36', '61'], False))
    print(bubble_sort(['88', '36', '21', '54', '99', '1', '81', '18', '21', '36', '61']))