from graphconstruction import random_graph


def dijkstra (graph, max_weight):
    
    #setup
    result_dict = {}
    traversal_list = []
    for node in graph:
        
        # each node has its prev node and the current max weight saved in a list
        if node == '0':
            result_dict[node] = [None, 0]
        else:
            result_dict[node] = ["UNDEF", max_weight * len(graph)]
        traversal_list.append(node)
        
    # dijkstra body
    while len(traversal_list) > 0:
        
        min_node = compare_dist(traversal_list, result_dict, max_weight=max_weight)
        traversal_list.remove(min_node)
        
        for neighbor in graph[min_node]:
            new_dist = result_dict[min_node][1] + int(neighbor[1])
            
            if new_dist < result_dict[neighbor[0]][1]:
                result_dict[neighbor[0]][0] = min_node
                result_dict[neighbor[0]][1] = new_dist
               
    return result_dict

# find lowest distance that is still in traversal list
def compare_dist(traversal_list, dist_dict, max_weight):
    min_dist = max_weight + 1
    min_node = traversal_list[0]
    
    for node in traversal_list:
        if dist_dict[node][1] < min_dist:
            min_dist = dist_dict[node][1]
            min_node = node
    
    return min_node
        
def main():
    max_weight = 20
    node_count = 1000
    
    graph = random_graph(node_count, 3, max_weight)
   # print(graph)
    
    dijkstra_result = dijkstra(graph=graph, max_weight=max_weight)
    #print(dijkstra_result)
    
    return

if __name__ == "__main__":
    main()