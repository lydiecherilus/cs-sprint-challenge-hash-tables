def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = dict()
    result = []

    for number in a:
        cache[number] = 1
        if number != 0 and -number in cache:
            result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
