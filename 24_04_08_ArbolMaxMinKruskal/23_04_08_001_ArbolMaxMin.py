import networkx as nx
import matplotlib.pyplot as plt
#Modulos que requiero para que funcion networkx que basicamente es como represento mi grafo de datos estructurado 
#matplot para visualizar 
#  funcion que nos ayuda a encontrar el padre del vertice
def find(vertex, parent):
    if parent[vertex] == vertex:
        return vertex
    parent[vertex] = find(parent[vertex], parent)
    return parent[vertex]

#En esta seccion  se encuentra un funcion que actua auxiliar que implementa la optimizacion de compresion de la ruta intentando encontrar  el padre de un vertice
#en la estructura de datos del conjunto. el diccionario padre almacena el padre de cada vertice del conjunto disjunto 

#Algoritmo de Kruskals para ambos tanto minimo como maximos  
def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    edges.sort()
    #Extraemos todos los bordes del grafico 
    
    parent = {vertex: vertex for vertex in graph}
    included_edges_min = set()
    included_edges_max = set()
    #Ordenamos de manera ascendente segun su pesos 
    for weight, u, v in edges:
        parent_u = find(u, parent)
        parent_v = find(v, parent)
        if parent_u != parent_v:
            included_edges_min.add((u, v, weight))
            included_edges_max.add((u, v, -weight))
            parent[parent_u] = parent_v
            #Creamos un padre diccionario que almacena el padre de cada vertice en el conjunto 
            #Creamos dos conjuntos vacios added_edges_min y max para almacenar los bordes incluidos en los arboles de expansion minimo y maximo
            #Iteramos a traves de los bordes verificando si sus puntos finales pertenecen a diferentes conjuntos disjuntos 
            #Realizamos una operacion haciendo de union para el padre de uno de los dos extremos sea el padre de otro,para fusionarlos 

    # Creo maximos y minimos para la representacion de los grafos  
    graph_min = nx.Graph()
    graph_max = nx.Graph()
    #Creo dos objetos graficos que correspondadn a los arboles de expansion minimo y maximo 
    for u, v, weight in included_edges_min:
        graph_min.add_edge(u, v, weight=weight)
    for u, v, weight in included_edges_max:
        graph_max.add_edge(u, v, weight=abs(weight))
        #Iteramos a traves de los borde agregando los objetos graficos utilizando el metodo .add_edge,estableciendo el atributo de peso de cada borde al peso del mismo 
        #EN el caso de expansion maxima usamos la funcion abs para poder convertir el peso nuevamente a su valor positivo original 

    #Imprimo el maximo y el minimo de los arboles  
    print("Minimum Spanning Tree:")
    pos = nx.spring_layout(graph_min)#Establecemos el diseño del grafico usando la funcion spring layout de networkx
    nx.draw_networkx_nodes(graph_min, pos, node_size=500)#Dibujo los nodos de los bordes 
    nx.draw_networkx_edges(graph_min, pos, edgelist=graph_min.edges(), width=2)#Establesco los atributos del node size 
    nx.draw_networkx_edge_labels(graph_min, pos, edge_labels=nx.get_edge_attributes(graph_min, 'weight'))#Agrefo etiquetas  y muestro el grafico 
    plt.show()
    

    print("Maximum Spanning Tree:")
    pos = nx.spring_layout(graph_max)
    nx.draw_networkx_nodes(graph_max, pos, node_size=500)
    nx.draw_networkx_edges(graph_max, pos, edgelist=graph_max.edges(), width=2)
    nx.draw_networkx_edge_labels(graph_max, pos, edge_labels=nx.get_edge_attributes(graph_max, 'weight'))
    plt.show()
    #Aplicamos los mismo para el maximo
    return included_edges_min, included_edges_max


# grafo que utilizo de base para el programa 
graph = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('C', 8), ('H', 11)],
    'C': [('B', 8), ('D', 7), ('F', 4), ('I', 2)],
    'D': [('C', 7), ('E', 9), ('F', 14)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('H', 1), ('I', 6)],
    'H': [('A', 8), ('B', 11), ('G', 1), ('I', 7)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}

# Find the minimum and maximum spanning tree and display them as graphs
kruskal(graph)
