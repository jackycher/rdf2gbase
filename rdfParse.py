from rdflib import Graph

g = Graph()
g.parse("C:\\Users\\Jacky\\Desktop\\02RDF文件\\1.owl", format="xml")


def sharp(s):
    a = s.split('#')
    return a[-1]


for s, p, o in g:
    print("hEntity:", sharp(s), "relation:", sharp(p), "tEntity:", sharp(o))
