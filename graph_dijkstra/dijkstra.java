package graph_dijkstra;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import graph_dijkstra.graphconstruction.Edge;
import graph_dijkstra.graphconstruction.Graph;

public class dijkstra {

    
    static class DijkstraNode {
        
        String id;
        String prev_node_id;
        int min_dist;

        // constructor
        public DijkstraNode(String id, int min_dist, String prev_node) {
            this.id = id;
            this.min_dist = min_dist;
            this.prev_node_id = prev_node;
        }

    }

    public static String compare_dist(
        List<String> traversal_list,
        HashMap<String, DijkstraNode> dist_dict,
        int max_weight
        ) {

            int min_dist = max_weight * dist_dict.size();
            String min_node = traversal_list.get(0);
            
            // compare nodes' current min_dist to find current lowest
            for (int i = 0; i < traversal_list.size(); i++) {
                String cur_node = traversal_list.get(i);

                if (dist_dict.get(cur_node).min_dist < min_dist) {
                    min_dist = dist_dict.get(cur_node).min_dist;
                    min_node = cur_node;
                }
            }
            
            return min_node;
    }
    public static HashMap<String, DijkstraNode> dijkstra(Graph graph, int max_weight) {

        int node_count = graph.graph.size();
        HashMap<String, DijkstraNode> result_dict = new HashMap<String, DijkstraNode>();
        List<String> traversal_list = new ArrayList<>();

        for (int i = 0; i < node_count; i++) {
            String cur_node = Integer.toString(i); 
            
            if (i == 0) {
                DijkstraNode new_node = new DijkstraNode(cur_node, 0, "START");
                result_dict.put(cur_node, new_node);
            } else {
                DijkstraNode new_node = new DijkstraNode(cur_node, max_weight * node_count, "UNDEF");
                result_dict.put(cur_node, new_node);
            }

            traversal_list.add(cur_node);
        }

        // dijkstra body
        while (traversal_list.size() > 0) {

            // find node with lowest weight
            String min_node_id = compare_dist(traversal_list, result_dict, max_weight);

            // deletion of currently used node
            for (int i = 0; i < traversal_list.size(); i++) {
                
                if (min_node_id.equals(traversal_list.get(i))) {
                    traversal_list.remove(i);
                }
            }

            // check neighbors of min node and update those
            for (Edge i : graph.graph.get(min_node_id)) {
                
                String neighbor = i.node1;
                if (i.node1.equals(min_node_id)) {
                    neighbor = i.node2;
                }

                int new_dist = result_dict.get(min_node_id).min_dist + i.weight;

                if (new_dist < result_dict.get(neighbor).min_dist) {
                    result_dict.get(neighbor).prev_node_id = min_node_id;
                    result_dict.get(neighbor).min_dist = new_dist;
                }
            }
        }
        return result_dict;
    }



    public static void main(String[] args) {
        Graph graph = graphconstruction.random_graph(10, 3, 20);
        for (int i = 0; i < 10; i++) {
            System.out.println("cur_node " + i);
            for (int j = 0; j < graph.graph.get(Integer.toString(i)).size(); j++) {
                Edge cur_edge = graph.graph.get(Integer.toString(i)).get(j);
                System.out.print(cur_edge.node1 + " " + cur_edge.node2 + " " + cur_edge.weight);
                System.out.println("");
            }
        }

        HashMap<String, DijkstraNode> result = dijkstra(graph, 20);

        for (int i = 0; i < 10; i++) {
            System.out.println("cur_node " + i);

                DijkstraNode curnode = result.get(Integer.toString(i));

                System.out.print(curnode.id + " " + curnode.min_dist + " " + curnode.prev_node_id);
                System.out.println("");
            
        }

        //System.out.println(test_node + " " + test_node.id + " " + test_node.prev_node + " ");
    }
}
