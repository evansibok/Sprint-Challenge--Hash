def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Initialize a dictionary to hold key value pairs
    # where keys are file path strings
    # and values are the queries
    query_table = {}
    for file in files:
        # Get the query to reconcile from the file path strings
        query = file.split('/')
        query_table[file] = query[-1]

    result = []
    for query in queries:
        for key, value in query_table.items():
            if value == query:
                result.append(key)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
