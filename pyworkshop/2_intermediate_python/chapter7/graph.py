# Let's create a graph that represents relationships between 10 users.
# We will create a graph class, add nodes (users), and edges (relationships) between them.
# Additionally, we'll implement a function to display relationships between any two users.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_relationship(self, user1, user2):
        if user1 in self.graph and user2 in self.graph:
            self.graph[user1].append(user2)
            self.graph[user2].append(user1)  # Assuming a bidirectional relationship

    def show_relationship(self, user1, user2):
        if user1 in self.graph and user2 in self.graph[user1]:
            return f"{user1} and {user2} are connected."
        else:
            return f"{user1} and {user2} are not connected."

# Create a graph instance and add 10 users
g = Graph()

users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8", "User9", "User10"]
for user in users:
    g.add_user(user)

# Add relationships between some users
g.add_relationship("User1", "User2")
g.add_relationship("User2", "User3")
g.add_relationship("User4", "User5")
g.add_relationship("User6", "User7")
g.add_relationship("User8", "User9")
g.add_relationship("User9", "User10")
g.add_relationship("User1", "User5")

# Let's test the show_relationship function
relationships = [
    g.show_relationship("User1", "User2"),
    g.show_relationship("User1", "User3"),
    g.show_relationship("User5", "User1"),
    g.show_relationship("User7", "User9"),
]

print(relationships)