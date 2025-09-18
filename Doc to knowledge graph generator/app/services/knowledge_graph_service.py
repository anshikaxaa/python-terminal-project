from rdflib import Graph, URIRef, Literal, Namespace, RDF, RDFS
from typing import Dict, List

def create_knowledge_graph(entities: Dict) -> Graph:
    g = Graph()
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)

    entity_uris = {}

    # Add entities
    for entity in entities.get("entities", []):
        entity_type = entity["type"]
        value = entity["value"]
        uri = URIRef(ex + value.replace(" ", "_"))
        entity_uris[value] = uri
        g.add((uri, RDF.type, ex[entity_type]))
        g.add((uri, RDFS.label, Literal(value)))

    # Add relationships
    for rel in entities.get("relationships", []):
        subject = rel["subject"]
        relation = rel["relation"]
        obj = rel["object"]
        if subject in entity_uris and obj in entity_uris:
            g.add((entity_uris[subject], ex[relation.replace(" ", "_")], entity_uris[obj]))

    return g

def serialize_graph(g: Graph, format: str = "turtle") -> str:
    return g.serialize(format=format)
