import networkx as nx

def build_full_graph(vertices, edge_weights):
    g = nx.Graph()
    g.add_nodes_from(vertices)
    for (v1, v2), weight in edge_weights.items():
        g.add_edge(v1, v2, weight=weight)
    return g


def build_threshold_graph(vertices, edge_weights, threshold):
    g = nx.Graph()
    g.add_nodes_from(vertices)
    for (v1, v2), weight in edge_weights.items():
        if weight >= threshold:
            g.add_edge(v1, v2, weight=weight)
    return g


def find_max_clique(g):
    max_cliques = []
    max_weight = 0
    for clique in nx.algorithms.clique.enumerate_all_cliques(g):
        if len(clique) > 1:
            weight = sum(g[u][v]['weight'] for u, v in nx.utils.pairwise(clique))
            if weight > max_weight:
                max_weight = weight
                max_cliques = [g.subgraph(clique).copy()]
            elif weight == max_weight:
                max_cliques.append(g.subgraph(clique).copy())
    if len(max_cliques) > 1:
        raise Exception('технически непонятно что делать в этом случае, вероятность такого события около нуля')
    return max_cliques[0] if max_cliques else nx.Graph()


def find_max_independent_set(g):
    return g.subgraph(nx.algorithms.maximal_independent_set(g)).copy()
