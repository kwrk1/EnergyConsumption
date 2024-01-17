import random as rand

# TODO : remove duplicate edges, we dont want nodes to have multiple edges to one another necessarily
# make random weighted undirected graph 
# graphs have keys: node names, and edges w/ weights in their values (as lists)
def random_graph(node_count, max_degree, max_wght):
    # init graph dict, make sure all nodes are connected
    graph = {}
    for i in range(0, node_count):
        graph[str(i)] = []
    
    for i in range(0, node_count):
        if i == node_count - 1:
            weight = str(rand.randrange(0, max_wght))
            graph[str(i)].append([
                str(0), 
                weight
            ])
            graph[str(0)].append([
                str(node_count - 1), 
                weight
            ])
        else:  
            weight = str(rand.randrange(0, max_wght))
            graph[str(i)].append([
                str(i+1), 
                weight
            ])
            graph[str(i+1)].append([
                str(i), 
                weight
            ])
    
    for node in graph:
        # coin toss to determine whether an edge should be added
        if rand.random() >= 0.5:
            graph = add_edge(graph, node, max_degree, max_wght)
    
    # potential edge removal algorithm in order to make graphs more interesting and not include a full loop every time (potentially removes connectedness property)
    #graph = remove_edges(graph)
    
    return graph

# add random edges to other nodes in the graph
def add_edge(graph, node, max_degree, max_wght):
    if len(graph[node]) == max_degree:
        return graph
    
    elif len(graph[node]) < max_degree:
        # try to find an elible node for connection a few times
        for i in range(0, 10):
            rand_node = str(rand.randrange(0, len(graph)))
            if len(graph[rand_node]) == max_degree and rand_node != node:
                continue
            elif len(graph[rand_node]) < max_degree and rand_node != node:
                break
            
        rand_wght = str(rand.randrange(0, max_wght))
        
        # if nodes are fine, add edges to both nodes, including the same weight
        graph[node].append([
            rand_node,
            rand_wght
            ])
        
        graph[rand_node].append([
            node,
            rand_wght
        ])
    elif len(graph[node]) > max_degree:
        return ValueError
    
    return graph

# remove random edges if possible.
# 1. iterate through list in numerical order
# 2. then, check if edges to a node with a greater number exist. 
# 3. check if the bigger node has other edges to lower nodes
# 3.1 if yes: roll dice to delete og_node -> bigger_node and bigger_node -> og_node
# 3.2 if no: repeat 2. with other nodes
# 4. when all nodes are exhausted, skip to next node
def remove_edges(graph):
    print(graph)
    for node in graph:
        if len(graph[node]) > 1:
            for edge in graph[node]:
                if (
                    int(node) == int(edge[0]) - 1   and
                    rand.random() >= 0.5            and
                    check_edges(edge[0], graph[edge[0]])
                    ):
                    graph[node].remove(edge)  
                    graph[edge[0]].remove([node,edge[1]])  
    return graph

# check for lower nodes in edge list
def check_edges(node, edges):
    for edge in edges:
        # check that connections to previous nodes exist that arent the direct predecessor
        if (int(node) != int(edge[0]) and
            int(node) > int(edge[0])): 
            return True
    return False

def print_graph(graph):
    for node in graph:
        print(node)
        print(graph[node])
    
def main():
    graph = random_graph(5, 3, 20)
    print_graph(graph)
    return

if __name__ == "__main__":
    main() 
