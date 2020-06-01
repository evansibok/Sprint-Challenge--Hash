def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Initialize a dictionary to hold key value pairs
    # where keys are file path strings
    # and values are the queries
    query_table = {}
    # Get the query to reconcile from the file path strings

    for file in files:
        query = file.split('/')
        query_table[file] = query[-1]

    for query in queries:
        print('query', query)

    # return result
    return query_table


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
