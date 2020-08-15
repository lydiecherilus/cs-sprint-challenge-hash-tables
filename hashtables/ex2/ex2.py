#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = dict()
    # flights
    route = [None] * length

    # go through tickets, link source to destination
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    # ticket source is next ticket destination
    next = cache['NONE']

    for flight in range(length):
        route[flight] = next
        next = cache[next]

    return route
