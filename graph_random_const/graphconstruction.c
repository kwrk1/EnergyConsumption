#include<stdio.h>
#include<limits.h>
#include<stdlib.h>
#include<string.h>


#include "graphconstruction.h"


// taken from github
int randInRange(int min, int max)
{
  return min + (int) (rand() / (double) (RAND_MAX) * (max - min + 1));
}

int check_valid_neighbors(Node node, int potential_neighbor)
{
    for (int i = 0; i < node.neighbor_count; i++)
    {
        if (node.neighbor[i].end_node == potential_neighbor)
        {
            return 0;
        }
    }
    return 1;
}


void addEdge(struct Graph *graph, int node_id1, int node_id2, int weight)
{
    int new_neighbor = graph->nodes[node_id1].neighbor_count;
    //printf("%d new_neighbor \n", graph->nodes[node_id1].neighbor[new_neighbor].end_node);
    graph->nodes[node_id1].neighbor[new_neighbor].end_node = node_id2;
    graph->nodes[node_id1].neighbor[new_neighbor].weight = weight;
    graph->nodes[node_id1].neighbor_count++;

    new_neighbor = graph->nodes[node_id2].neighbor_count;
    //printf("%d new_neighbor \n", new_neighbor);
    graph->nodes[node_id2].neighbor[new_neighbor].end_node = node_id1;
    graph->nodes[node_id2].neighbor[new_neighbor].weight = weight;
    graph->nodes[node_id2].neighbor_count++;

    return;
}


void addEdges(struct Graph *graph, int node_id, int max_degree, int max_weight)
{      
    if (graph->nodes[node_id].neighbor_count == max_degree)
    {
        return;
    } else if (graph->nodes[node_id].neighbor_count < max_degree)
    {
        for (int i = 0; i < 10; i++) 
        {
            int rand_node_id = randInRange(0, graph->node_count - 1);
            
            if (graph->nodes[rand_node_id].neighbor_count == max_degree)
            {
                continue;
            } else if (
                graph->nodes[rand_node_id].neighbor_count < max_degree &&
                node_id != rand_node_id &&
                check_valid_neighbors(graph->nodes[node_id], rand_node_id) == 1
            ) 
            {   
                int rand_weight = randInRange(0, max_weight + 1);
                
                addEdge(graph, node_id, rand_node_id, rand_weight);
                return;
            }
        }
    }
}


Graph* random_graph(int node_count, int max_degree, int max_weight) 
{
    // initialize graph, its nodes and its neighbor lists
    struct Graph* graph = (Graph*) malloc(sizeof(Graph));
    graph->node_count = node_count;

    graph->nodes = (Node*) malloc(sizeof(Node) * node_count); 
    for (int i = 0; i < node_count; i++) 
    {   

            //printf("hi %d\n", i);
            graph->nodes[i].node_id = i;
            graph->nodes[i].neighbor_count = 0;
            graph->nodes[i].neighbor = (Edge*) malloc(sizeof(Edge) * max_degree);
            //printf("hi %d %d\n",  graph->nodes[i].node_id,  graph->nodes[i].neighbor_count);

            // init neighbor nodes for modification down the line 
            for (int j = 0; j < max_degree; j++) 
            {   
                //printf("bye %d\n", j);
                graph->nodes[i].neighbor[j].end_node = -1;
                graph->nodes[i].neighbor[j].weight = max_weight + 1;
                //printf("bye %d\n", graph->nodes[i].neighbor->weight);
            }
    }

    for (int i = 0; i < node_count; i++)
    {
        int weight = randInRange(0, max_weight);
        
        if (i == node_count - 1)
        {
            addEdge(graph, i, 0, weight);
            
            //puts("pls");
        } else 
        {
            //printf("%d new_neighbor \n", graph->nodes[i].neighbor_count);
            //printf("bye %d %d\n", i, i+1);
            addEdge(graph, i, i + 1, weight);
        }
    }

    // add random edges
    for (int i = 0; i < node_count; i++) 
    {
        if (randInRange(1, 2) == 2)
        {
            addEdges(graph, i, max_degree, max_weight);
        }
    }

    return graph;
}


// int main(int argc, char *argv[]) 
// {
//     for (int i = 0; i < 10; i++) 
//     {
//         printf("%d\n", randInRange(1,2));
//     }

//     int x = 2000000;
//     struct Graph* graph = random_graph(10, 3, 20);
    
//     printf("%d\n", graph->node_count);
//     for (int i = 0; i < 10; i++)
//     {   
//         printf("%d\n", graph->nodes[i].node_id);
//         for (int j = 0; j < graph->nodes[i].neighbor_count; j++)
//         {
//             printf("%d, %d\n", graph->nodes[i].neighbor[j].end_node, graph->nodes[i].neighbor[j].weight);
//         }
//     }
//     // length of int
//     //int length = snprintf( NULL, 0, "%d", x );

//     //printf("%ld, %d", sizeof(2000000000000000), length);
//     return 0;
// }