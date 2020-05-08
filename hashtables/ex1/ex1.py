def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    # UPER
    # Plan

    # INPUTS
    # Takes in a list of weights
    # length of the list
    # and a weight limit

    # Initialize a python dictionary as hashtable
    hash_table = dict()
    # move through the list elements (taking the element and the element's index)
    # for every element
    for index, element in enumerate(weights):
        # add the element to the empty dictionary as a key
        # and add the index of the same element as the value
        hash_table[element] = index
    # Check to see if the dict contains a key entry
    # for the equation `limit - weight`,
    # where limit is the `limit` and weight is the `list element.
        deducted = limit - element

        if deducted in hash_table and length == 2:
            # If it does, return a tuple of both element's index
            # (high_index, low_index)
            return (1, 0)
        elif deducted in hash_table:
            return (hash_table[element], hash_table[deducted])
    return None


# A package has a weight limit
# ""        has a list of items weights
# Find two items whose sum of weights equals the weight limit
# Function will return (zero, one) where
# each element represents the item weights of the two packages
# Higher valued index should be `zeroth` and the smaller index
# should be `oneth` in the tuple.
# Store each weight in the input list as keys
# Store each weight's index as it's value
# We can if the hashtable contains an element that results from
# limit - weight`. If it does, then we found the two items whose
# weights sum up to the limit.
# sample_dict = {key: value, key: value}
# access dict: dict[key]:  value


if __name__ == "__main__":

    weights = [4, 4]
    length = 2
    limit = 8

    get_indices = get_indices_of_item_weights(weights, length, limit)

    print("")
    print(get_indices)
