import networkx as nx
import matplotlib.pyplot as plt

# Lista de vértices (estados)
vertice = []

# Función para ingresar vértices
def ingresar_vertice():
    for _ in range(7):
        estado = input("Ingrese un estado del país: ")
        vertice.append(estado)
    print("Estados ingresados:", vertice)

# Crear grafo con las relaciones especificadas
def crear_grafo(vertice):
    return {
        vertice[0]: [vertice[1], vertice[2]],
        vertice[1]: [vertice[0], vertice[3]],
        vertice[2]: [vertice[0], vertice[3]],
        vertice[3]: [vertice[1], vertice[2], vertice[4]],
        vertice[4]: [vertice[5], vertice[6]],
        vertice[5]: [vertice[4], vertice[2]],
        vertice[6]: [vertice[4], vertice[5]]
    }

# Función para dibujar el grafo
def dibujar_grafo(grafo):
    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            G.add_edge(nodo, vecino)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
    plt.title("Grafo de Estados y sus Relaciones")
    plt.show()

# Función para el recorrido sin repetición (DFS)
def recorrido_sin_repetir(grafo, nodo, visitado):
    if nodo not in visitado:
        visitado.add(nodo)
        for vecino in grafo.get(nodo, []):
            recorrido_sin_repetir(grafo, vecino, visitado)

# Función para calcular el costo del recorrido sin repetición
def costo_recorrido(visitado):
    return len(visitado)

# Función para el recorrido con repetición usando DFS
def recorrido_con_repeticion(grafo, nodo_inicial, total_nodos=7):
    recorrido = []
    visitados = set()
    
    def dfs(nodo):
        # Detenerse si se han visitado suficientes nodos
        if len(visitados) >= total_nodos:
            return
        recorrido.append(nodo)
        visitados.add(nodo)
        
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                dfs(vecino)
    
    dfs(nodo_inicial)
    return recorrido

# Ingresar vértices
ingresar_vertice()

# Verificar que haya al menos 7 estados ingresados
if len(vertice) < 7:
    print("Se necesitan al menos 7 estados.")
else:
    # Crear el grafo con los vértices y relaciones
    grafo = crear_grafo(vertice)
    print("\nRelaciones entre estados en el grafo:")
    for estado, relaciones in grafo.items():
        print(f"{estado} -> {relaciones}")

    # Realizar el recorrido sin repetición
    visitado = set()
    recorrido_sin_repetir(grafo, vertice[0], visitado)
    costo_a = costo_recorrido(visitado)
    print(f"\nRecorrido sin repetir: {visitado}, Costo total: {costo_a}")

    # Realizar el recorrido con repetición (DFS)
    recorrido_b = recorrido_con_repeticion(grafo, vertice[0])
    costo_b = len(recorrido_b)
    print(f"Recorrido con repetición: {recorrido_b}, Costo total: {costo_b}")

    # Dibujar el grafo
    dibujar_grafo(grafo)
