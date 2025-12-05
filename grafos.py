import csv
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque
import heapq

class Grafo:
    def __init__(self):
        self.adjacencia = defaultdict(list)

    def adicionar_aresta(self, u, v, peso):
        self.adjacencia[u].append((v, peso))
        self.adjacencia[v].append((u, peso))  # Grafo não direcionado

    def carregar_de_arquivo(self, arquivo):
        with open(arquivo, 'r') as f:
            if arquivo.endswith('.csv'):
                leitor = csv.reader(f)
                for linha in leitor:
                    u, v, peso = map(int, linha)
                    self.adicionar_aresta(u, v, peso)
            elif arquivo.endswith('.txt'):
                for linha in f:
                    u, v, peso = map(int, linha.split())
                    self.adicionar_aresta(u, v, peso)

    # ---------------- DFS -----------------
    def dfs(self, inicio):
        visitados = set()
        resultado = []

        def visitar(v):
            visitados.add(v)
            resultado.append(v)
            for vizinho, _ in self.adjacencia[v]:
                if vizinho not in visitados:
                    visitar(vizinho)

        visitar(inicio)
        return resultado

    # ---------------- BFS -----------------
    def bfs(self, inicio):
        visitados = set([inicio])
        fila = deque([inicio])
        resultado = []

        while fila:
            v = fila.popleft()
            resultado.append(v)

            for vizinho, _ in self.adjacencia[v]:
                if vizinho not in visitados:
                    visitados.add(vizinho)  # Correção importante
                    fila.append(vizinho)

        return resultado

    # --------------- DIJKSTRA ---------------
    def dijkstra(self, inicio, destino):
        distancias = {v: float('inf') for v in self.adjacencia.keys()}
        distancias[inicio] = 0
        heap = [(0, inicio)]
        caminho = {}

        while heap:
            dist, atual = heapq.heappop(heap)
            if atual == destino:
                break

            for vizinho, peso in self.adjacencia[atual]:
                nova_dist = dist + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    caminho[vizinho] = atual
                    heapq.heappush(heap, (nova_dist, vizinho))

        # Reconstroi caminho
        if destino not in caminho and destino != inicio:
            return [], float('inf')

        caminho_final = []
        atual = destino
        while atual in caminho:
            caminho_final.append(atual)
            atual = caminho[atual]
        caminho_final.append(inicio)

        return list(reversed(caminho_final)), distancias[destino]

    # ---------------- PRIM -----------------
    def prim(self):
        vertices = list(self.adjacencia.keys())
        visitados = set()
        arestas_resultado = []
        heap = [(0, None, vertices[0])]  # (peso, de, para)

        while heap:
            peso, de, para = heapq.heappop(heap)

            if para not in visitados:
                visitados.add(para)
                if de is not None:
                    arestas_resultado.append((de, para, peso))

                for vizinho, peso_aresta in self.adjacencia[para]:
                    if vizinho not in visitados:
                        heapq.heappush(heap, (peso_aresta, para, vizinho))

        return arestas_resultado

    # -------------- VISUALIZAÇÃO --------------
    def visualizar(self):
        G = nx.Graph()
        for u in self.adjacencia:
            for v, peso in self.adjacencia[u]:
                G.add_edge(u, v, weight=peso)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


# Exemplo de uso
if __name__ == "__main__":
    grafo = Grafo()
    grafo.carregar_de_arquivo("grafo.txt")

    print("DFS:", grafo.dfs(1))
    print("BFS:", grafo.bfs(1))
    print("Dijkstra (1 -> 4):", grafo.dijkstra(1, 4))
    print("Árvore Geradora Mínima (Prim):", grafo.prim())

    grafo.visualizar()
