'''
In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.

To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

Run the following code that defines this Server class.

NEXT STEPS:
- generate a random connection_id when server is instantiated
- finish the load average calculation for the LoadBalancer class
'''
#Begin Portion 1#
import random
import string

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        print('New connection load: ', connection_load)
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections.keys():
            del self.connections[connection_id]
            return connection_id
        else:
            return None

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for _ in self.connections.values():
            total += 1
        return total

    # def __str__(self):
    #     """Returns a string with the current load of the server"""
    #     return "{:.2f}%".format(self.load())
    
#End Portion 1#

server = Server()
server.add_connection("192.168.1.1")
print(server.load())

server.close_connection("192.168.1.1")
# server.close_connection("192.168.1.0")
print(server.load())


#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        server.add_connection(connection_id)
        self.connections[connection_id] = server
        # Add the connection to the server
        self.servers.append(server)

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        if connection_id in self.connections.keys():
            # Close the connection on the server
            del self.connections[connection_id]
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total = 0
        for server in self.servers:
            print('Value: ', server.connections)
            # for conn in server.connections.values():
            #     print('Server: ', conn)
        return 0

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())
