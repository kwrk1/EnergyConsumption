#include<stdio.h>
#include<limits.h>
#include<stdlib.h>
#include<string.h>

#include "graphconstruction.h"

typedef struct DijkstraNode 
{
    int prev_node_id;
    int min_dist;
} DijkstraNode;

typedef struct TraversalList
{
    int* node_id;
    int len;
} TraversalList;

void set_results(DijkstraNode* results, int id, int prev_node_id, int min_dist)
{
    results[id].prev_node_id = prev_node_id;
    results[id].min_dist = min_dist;
}


int compare_dist(TraversalList* traversal_list, DijkstraNode* results, int max_weight)
{
    int min_dist = max_weight * 100;
    int min_node_id = traversal_list->node_id[0];

    //printf("minnode in compare dist = %d\n", min_node_id);
    for (int i = 0; i < traversal_list->len; i++)
    {
        int cur_node_id = traversal_list->node_id[i];

        //printf("results dist %d, mindist %d\n", results[cur_node_id].min_dist, min_dist);
        if (results[cur_node_id].min_dist < min_dist)
        {
            min_dist = results[cur_node_id].min_dist;
            min_node_id = cur_node_id;
        }
    }
    //printf("return min node in compare dist = %d\n", min_node_id);
    return min_node_id;
}

DijkstraNode* dijkstra(Graph* graph, int max_weight)
{
    int node_count = graph->node_count;
    DijkstraNode* results = (DijkstraNode*) malloc(sizeof(DijkstraNode) * node_count);

    TraversalList* traversal_list = (TraversalList*) malloc(sizeof(TraversalList));
    traversal_list->node_id = (int*) malloc(sizeof(int) * node_count);

    for (int i = 0; i < node_count; i++)
    {
        if (i == 0)
        {
            set_results(results, i, -1, 0); // -1 signifies starting node
        } else {
            set_results(results, i, -2, max_weight * node_count);
        }

        traversal_list->node_id[i] = i;
        traversal_list->len++;
    }

    //dijkstra body
    while (traversal_list->len > 0)
    {
        int min_node_id = compare_dist(traversal_list, results, max_weight);
        // for (int i = 0; i < traversal_list->len; i++) 
        // {
        //     printf("%d travlist %d\n", i, traversal_list->node_id[i]);
        // }
        // printf("min node %d\n", min_node_id);
        // removal by just shifting the node_id to the last spot
        for (int i = 0; i < traversal_list->len; i++)
        {
            if (traversal_list->node_id[i] == min_node_id)
            {
                traversal_list->node_id[i] = traversal_list->node_id[traversal_list->len - 1];
                traversal_list->len--;
            }
        }        

        for (int i = 0; i < graph->nodes[min_node_id].neighbor_count; i++)
        {
            Node min_node = graph->nodes[min_node_id];
            int new_dist = results[min_node_id].min_dist + min_node.neighbor[i].weight;

            int neighbor_id = min_node.neighbor[i].end_node;

            if (new_dist < results[neighbor_id].min_dist)
            {
                set_results(results, neighbor_id, min_node_id, new_dist);
            }
        }
    }

    return results;
}

int main(int argc, char *argv[])
{
    int node_count = 15;
    Graph* graph = random_graph(node_count, 4, 20);
    printf("%d\n", graph->node_count);
    for (int i = 0; i < 10; i++)
    {   
        printf("%d\n", graph->nodes[i].node_id);
        for (int j = 0; j < graph->nodes[i].neighbor_count; j++)
        {
            printf("%d, %d\n", graph->nodes[i].neighbor[j].end_node, graph->nodes[i].neighbor[j].weight);
        }
    }
    DijkstraNode* results = dijkstra(graph, 20);
    
    for(int i = 0; i < node_count; i++)
    {
        printf("Node %d, prev_node %d, min_dist %d\n", i, results[i].prev_node_id, results[i].min_dist);       
    }

    return 0;
}