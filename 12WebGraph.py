import networkx as nx
import matplotlib.pyplot as plt
from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movie.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element:%s"%collection.getAttribute("shelf"))
    movies = collection.getElementsByTagName("movie")
for movie in movies:
    print("***Movie***")
    if movie.hasAttribute("title"):
        print("Title:%s"%movie.getAttribute("title"))
    type_elem = movie.getElementsByTagName('type')[0]
    print("Types:%s"%type_elem.childNodes[0].data)
    format_elem = movie.getElementsByTagName('format')[0]
    print("Format:%s"%format_elem.childNodes[0].data)
    rating_elem = movie.getElementsByTagName('rating')[0]
    print("Rating:%s"%rating_elem.childNodes[0].data)
    description_elem = movie.getElementsByTagName('description')[0]
    print("Description:%s"%description_elem.childNodes[0].data)

def GenerateGraph():
    G = nx.Graph()
    G.add_node("a")
    G.add_edges_from([("a","b"),("b","c"),("c","d"),("d","a"),("a","c")])

    nx.draw(G,with_labels=True ,node_color='lightblue', edge_color='gray',node_size=2000,font_size=15)

    plt.savefig("simple_path.png")
    plt.show()
    print("Nodes of graph:")
    print(G.nodes())
    print("Edges of graph:")
    print(G.edges())
GenerateGraph()
