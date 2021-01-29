def find_sum(N):

    num_line = list(range(1, N+1))
    result = []

    for i in range(1, len(num_line) + 1):
        if (i % 3 == 0) or (i % 5 == 0) in num_line:
            result.append(i)

    result = sum(result)

    return result


if __name__ == '__main__':
    print(find_sum(5))