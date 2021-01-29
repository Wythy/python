def odd_ball(arr):

    odd_index = arr.index('odd')
    if odd_index in arr:
        return True
    else:
        return False


if __name__ == '__main__':
    print(odd_ball(['even', 12, 'even', 1, 'even', 3, 'even', 87, 'even', 11, 'odd', 9, 'even', 7, 'even']))