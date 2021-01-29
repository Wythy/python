def get_names(names):
    res = []
    count = 0

    for i in names:

        if len(names[count]) / 4 == 1:
            res.append(i)

        count += 1

    return res


if __name__ == '__main__':
    print(get_names(['Tom', 'Kevin', 'Richard', 'Mark', 'Max', 'Mikle', 'Nikolas', 'Margaret', 'Anya', 'Alia', 'Juliet']))