#ifndef GRAPHCONSTRUCTION_H_   
#define GRAPHCONSTRUCTION_H_

typedef struct Edge 
{
    int end_node;
    int weight;
} Edge;

typedef struct Node
{
    int node_id;

    int neighbor_count;
    struct Edge* neighbor;
} Node;

typedef struct Graph
{
    int node_count;
    struct Node* nodes;
} Graph;

int randInRange(int min, int max);  
int check_valid_neighbors(struct Node node, int potential_neighbor);
void addEdge(struct Graph *graph, int node_id1, int node_id2, int weight);
void addEdges(struct Graph *graph, int node_id, int max_degree, int max_weight);
struct Graph* random_graph(int node_count, int max_degree, int max_weight);

#endif 