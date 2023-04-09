class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    #  Funcion para añadir los edges al graph 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # Encontrar el set de elementos en i 
    # Comprime el path al mas corto 
    def find(self, parent, i):
        if parent[i] != i:
 
            #Reasignacion de nodos padre  
            #  el origen del nodo 
            # requiere que comprimamos el path
            parent[i] = self.find(parent, parent[i])
        return parent[i]
 
    #  union de los sets en x,y
    # Usa uniones por rango 
    def union(self, parent, rank, x, y):
 
        # junta al  los arboles de menor rango al origen de este 
        # El arbol de alto rango 
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
 
        #  si tienen un rango simila convierte a uno de estos a una raiz 
        #  e incrementa el rango en uno de la misma 
        else:
            parent[y] = x
            rank[x] += 1
 
    #  Funcion principal 
    #
    def KruskalMST(self):
 
        #  guardara el resultante en MST 
        result = []
 
        # contador para los edges que sean sorteados  
        i = 0
 
        #contador para los resultados[] A
        e = 0
 
        # acomoda de acuerdo a todos los edges  en un orden no decreciente  de su peso  S
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Crea un subset V para elementos individuales 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        #Numeros de edges que seran tomados cuando V-1 
        while e < self.V - 1:
 
            # Escoge el menor  y lo incrementa
            # y creamos una bandera para la siguiente iteracion 
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else descarta el edge 
 
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)
 
 

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
 
    # llamada a funcion 
    g.KruskalMST()