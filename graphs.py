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
    max_clique = []
    max_weight = 0
    for clique in nx.algorithms.clique.enumerate_all_cliques(g):
        if len(clique) > 1:
            weight = sum(g[u][v]['weight'] for u, v in nx.utils.pairwise(clique))
            if weight > max_weight:
                max_weight = weight
                max_clique = [clique]
            elif weight == max_weight:
                max_clique.append(clique)
    return max_clique


def find_max_independent_set(g):
    return nx.algorithms.maximal_independent_set(g)

