#  Hint:  You may not need all of these.  Remove the unused functions.

# UPER
# source represents the starting airport
# destination represents the next airport
# First ticket has a source of 'NONE'
# Last ticket has a destination of 'NONE'
# An array of tickets contains individual tickets that are dictionaries
# with a keys of ('source' and 'destination') and values of ('PNG', 'ORD') which represent airport names.

# ticket1 = ("None", "ATL")
# ticket2 = ("SPL", "None")
# ticket3 = ("ATL", "SPL")

"""
{
    "None": "ATL",
    "ATL": "SPL",
    "SPL": "None"
}
"""

"""
{
    source: destination
}
"""


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"Source: {self.source}, Destination: {self.destination}"


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    routes = {}
    for ticket in tickets:
        routes[ticket.source] = ticket.destination

    route = []
    # FIRST SOLUTION -> Passes short test
    # for source in routes:
    #     destination = routes[source]
    #     if destination != "None":
    #         route.append(destination)
    #         source = destination

    # SECOND SOLUTION -> Passes long test
    # Initialize starting route source
    source = "NONE"
    for _ in routes:
        # Get next destination from starting route
        destination = routes[source]
        # Add next destination to route
        route.append(destination)
        # move through the destination to get next source
        source = destination

    return route


if __name__ == '__main__':

    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
               ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
    print(tickets)

    route = reconstruct_trip(tickets, len(tickets))
    print("route", route)
