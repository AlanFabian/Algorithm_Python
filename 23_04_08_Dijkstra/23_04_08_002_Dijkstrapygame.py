import pygame as pg
from heapq import *
#Implementacion del algoritmo de dijkstra

def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 4 #Forma los circulos 


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2

# determinacion de celdas vecinas revisando en el sentido 
'''
        x|y
         ____
        |    |
    x-y |____|    x -y 
         x|y
'''
def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in ways if check_next_node(x + dx, y + dy)] #


def heuristic(a, b):
   return abs(a[0] - b[0]) + abs(a[1] - b[1])

#Creacion del grid 
cols, rows = 23, 13 
TILE = 70

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()
# grid
#determino los costos  de movimiento de cada celda 
#Los meto como una lista de strings 
grid = ['22222222222222222222212',
        '22222292222911112244412',
        '22444422211112911444412',
        '24444444212777771444912',
        '24444444219777771244112',
        '92444444212777791192144',
        '22229444212777779111144',
        '11111112212777772771122',
        '27722211112777772771244',
        '27722777712222772221244',
        '22292777711144429221244',
        '22922777222144422211944',
        '22222777229111111119222']
#Convertir la lista de strings que le pase al grid a una lista de numeros ordinarios
grid = [[int(char) for char in string ] for string in grid]
# Lista de adyacencias 
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

#Parametros iniciales para el algoritmo de Dijkstra
start = (0, 7)
goal = (22, 7)#Punto final donde buscaremos el path mas corto
queue = []
heappush(queue, (0, start))
cost_visited = {start: 0}
visited = {start: None}
#Escalar la imagen a la resolucion del mapa  y ponerla de fondo 
bg = pg.image.load('2.png').convert()
bg = pg.transform.scale(bg, (cols * TILE, rows * TILE))

while True:
    # Llenamos la pantalla 
    sc.blit(bg, (0, 0))
    # Dibujamos el trabajo del algoritmo de dijkstra
    [pg.draw.rect(sc, pg.Color('forestgreen'), get_rect(x, y), 1) for x, y in visited]
    [pg.draw.rect(sc, pg.Color('darkslategray'), get_rect(*xy)) for _, xy in queue]
    pg.draw.circle(sc, pg.Color('purple'), *get_circle(*goal))

    #Aplicamos el algoritmo de Dijkstra
    if queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            queue = []
            continue

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                priority = new_cost + heuristic(neigh_node, goal)
                heappush(queue, (priority, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node

    # Dibuja el camino 
    path_head, path_segment = cur_node, cur_node
    while path_segment:
        pg.draw.circle(sc, pg.Color('brown'), *get_circle(*path_segment))
        path_segment = visited[path_segment]
    pg.draw.circle(sc, pg.Color('blue'), *get_circle(*start))
    pg.draw.circle(sc, pg.Color('magenta'), *get_circle(*path_head))
    # pygame necesita estas linas para que funcione bien 
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)
