from neo4j.v1 import GraphDatabase

uri = "bolt://neo4j:7687"


class Neo4jRepository():
    node_type = ''

    def __init__(self):
        self.graph_database = GraphDatabase.driver(uri, auth=("neo4j", "password"))
