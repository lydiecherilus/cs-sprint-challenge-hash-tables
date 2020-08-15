def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = dict()

    for index in range(length):
        difference = limit - weights[index]

        if difference not in cache:
            cache[weights[index]] = index
        else:
            index_two = cache[difference]
            return (index, index_two)

    return None
