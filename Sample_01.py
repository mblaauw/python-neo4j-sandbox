__author__ = 'MBlaauw'

from py2neo import neo4j
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

die_hard = graph_db.create(
    node(name="Andre"),
    node(name="Michel"),
    node(name="Martijn"),
    node(name="Jorg"),
    node(name="Leon"),
    node(name="Deloitte"),
    node(name="Macaw"),
    node(name="School"),
    node(name="Choco"),
    node(name="Coffee"),
    node(name="Water"),
    node(name="Climbing"),
    node(name="BI Lead"),
    node(name="BI Architect"),
    node(name="BI Manager"),
    node(name="Male"),
    node(name="Female"),

    rel(0, "DRINKS", 8),
    rel(0, "WORKS_AT", 5),
    rel(0, "DRINKS", 10),
    rel(0, "HAS_ROLE", 14),
    rel(0, "HAS_GENDER", 15),

    rel(1, "DRINKS", 8),
    rel(1, "DRINKS", 9),
    rel(1, "DRINKS", 10),
    rel(1, "WORKS_AT", 5),
    rel(1, "HAS_ROLE", 14),
    rel(1, "HAS_GENDER", 15),

    rel(2, "WORKS_AT", 6),
    rel(2, "DRINKS", 9),
    rel(2, "LIKES", 11),
    rel(2, "HAS_ROLE", 12),
    rel(2, "LIKES", 11),
    rel(2, "HAS_GENDER", 15),
    rel(2, "HAS_GENDER", 15),

    rel(3, "DRINKS", 9),
    rel(3, "WORKS_AT", 6),
    rel(3, "HAS_ROLE", 13),
    rel(3, "HAS_GENDER", 15),

    rel(4, "DRINKS", 9),
    rel(4, "WORKS_AT", 5),
    rel(4, "WORKS_AT", 7),
    rel(4, "HAS_GENDER", 15),

)
from py2neo import node, rel




