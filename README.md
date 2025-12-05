Sistema de Análise de Grafos

Este projeto implementa os principais algoritmos clássicos de grafos estudados na disciplina:
- Travessia em Profundidade (DFS)
- Travessia em Amplitude (BFS)
- Dijkstra (menor caminho entre dois vértices)
- Prim (árvore geradora mínima)
- Visualização gráfica do grafo
- Leitura do grafo a partir de arquivos .txt ou .csv

O grafo é não direcionado e ponderado.

------------------------------------------------------------
Estrutura do Projeto

TrabalhoGrafos/
 ├── grafos.py
 ├── grafo.txt
 ├── grafo.csv
 ├── relatorio.pdf
 ├── README.txt
------------------------------------------------------------

Como executar o projeto:

1. Instale as dependências:
   pip install networkx matplotlib

2. Rode o programa:
   python codigo.py

------------------------------------------------------------
Formato dos arquivos de entrada

Arquivo grafo.txt:
1 2 4
2 3 5
3 4 6

Arquivo grafo.csv:
1,2,4
2,3,5
3,4,6

Cada linha representa uma aresta no formato:
vértice1 vértice2 peso

------------------------------------------------------------
Algoritmos implementados:
- DFS
- BFS
- Dijkstra
- Prim

------------------------------------------------------------
Autores:
Diogo Lamera, Gabriel Xavier, Matheus Amaral, Max Augusto e Ronaldo Soares

Data:
(07/12/2025
------------------------------------------------------------
