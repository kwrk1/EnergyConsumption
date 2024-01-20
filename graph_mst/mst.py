from graph_random_const.graphconstruction import random_graph
import random as rand

def prims_algo(graph):
    #setup
    mst = {}
    start_node = str(rand.randrange(0, len(graph)))
    mst[start_node] = []
    it_graph = graph
    
    # prims algo body
    for node in graph:
        #print(graph)
        mst, it_graph = find_lowest_cost_edge(graph=it_graph, mst=mst)
        print(it_graph)
        #print(mst)
    return mst


# find lowest cost edge in the current graph, put it into our current mst and delete it from graph to exclude it from further consideration
def find_lowest_cost_edge(graph, mst):
    min_dist = 50 # arbitarily high 
    min_edge = []
    for node in mst:
        print(node)
        for neighbor in graph[node]:
            if int(neighbor[1]) < min_dist:
                min_dist = int(neighbor[1])
                min_edge = neighbor
                min_node = node
                new_node = neighbor[0]

    # if mst list is empty, just add the neighbor
    if mst[min_node] == None:
        mst[min_node] = []
        mst[min_node].append(neighbor)
        mst[new_node] = []
    else: 
        # check if we already have this node with another edge
        for node in mst:
            if mst[node] == min_edge[0]:
                if min_dist < int(mst[node][1]):
                    mst[node][1] = min_dist
                    mst[new_node] = [node, min_dist]
                else:
                    break
        # if not, append it, otherwise do what is shown above
        mst[min_node].append(min_edge)
    graph[min_node].remove(min_edge)
    return mst, graph

def main(): 
    
    max_weight = 20
    
    graph = random_graph(5, 4, max_weight)
    print(graph)
    
    mst = prims_algo(graph)
    print("minspantree")
    print(mst)
    
    return

if __name__ == "__main__":
    main()
    