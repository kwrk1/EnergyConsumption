import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ThreadLocalRandom;


class graphconstruction {    
    
    static class Edge {

        String node1;
        String node2;
        int weight;
        
        public Edge(String node1, String node2, int weight) {
            this.node1 = node1;
            this.node2 = node2;
            this.weight = weight;
        }
        
        public String getNode1() {
            return node1;
        }
    
        public String getNode2() {
            return node2;
        }
    
        public int getWeight() {
            return weight;
        }
    }
    
    
    static class Graph {
        // map working similar to python dictionary
        HashMap<String, List<Edge>> graph;
    
        public Graph(int size) {
            this.graph = new HashMap<String, List<Edge>>();
            List<Edge> empty_list = new ArrayList<>();
            
            for (int i = 0; i < size; i++) {
                this.graph.put(Integer.toString(i), empty_list); 
            }
            
        }
    
        public void addEdge(String node, int max_degree, int max_weight) {
    
            if (this.graph.size() == max_degree) {
                return;
            } else if (this.graph.size() < max_degree) {
    
                for (int i = 0; i < 10; i++) {
                    String rand_node = Integer.toString(
                        (ThreadLocalRandom.current().nextInt(0, this.graph.size() + 1)));
    
                    if (this.graph.get(rand_node).size() == max_degree) {
                        continue;
                    } else if (
                        this.graph.get(rand_node).size() < max_degree &&
                        node != rand_node && 
                        check_valid_neighbors(this.graph.get(node), rand_node)
                        ) {
    
                            int rand_weight = ThreadLocalRandom.current().nextInt(0, max_weight + 1);
                            Edge new_edge = new Edge(node, rand_node, rand_weight);
    
                            this.graph.get(node).add(new_edge);
                            this.graph.get(rand_node).add(new_edge);
                    }
                }
            }
    
        }

    
        private static boolean check_valid_neighbors(
            List<Edge> neighbors,
            String potential_neighbor
            ) {
            
            Set<String> cur_neighbors = new HashSet<String>();
    
            for (int i = 0; i < neighbors.size(); i++) {
                cur_neighbors.add(neighbors.get(i).node1);
                cur_neighbors.add(neighbors.get(i).node2);
            }
    
            if (cur_neighbors.contains(potential_neighbor)) {
                return true;
            }
    
            return false;
        }
    }

    public static Graph random_graph(int node_count, int max_degree, int max_weight) {

        Graph graph = new Graph(node_count);

        for (int i = 0; i < node_count; i++) {
            int weight = ThreadLocalRandom.current().nextInt(0, max_weight + 1);
            String cur_node = Integer.toString(i);

            if (i == node_count - 1) {

                Edge new_edge = new Edge("0", cur_node, weight);

                graph.graph.get("0").add(new_edge);
                graph.graph.get(cur_node).add(new_edge);

            } else {

                String node2 = Integer.toString(i+1);
                Edge new_edge = new Edge(cur_node, node2, weight);

                graph.graph.get(cur_node).add(new_edge);
                graph.graph.get(node2).add(new_edge);
            } 
        }
        
        for (int i = 0; i < node_count; i++) {
            if (Math.random() >= 0.5) {
                graph.addEdge(Integer.toString(i), max_degree, max_weight);
            }
        }

        return graph;
    }


    public static void main(String[] args){
        Graph graph = random_graph(10, 3, 20);
        for (int i = 0; i < 10; i++) {
            System.out.println("cur_node " + i);
            for (int j = 0; j < graph.graph.get(Integer.toString(i)).size(); j++) {
                Edge cur_edge = graph.graph.get(Integer.toString(i)).get(j);
                System.out.print(cur_edge.node1 + " " + cur_edge.node2 + " " + cur_edge.weight);
                System.out.println("");
            }
        }
        // prints graph
        //graph.graph.forEach((key, value) -> System.out.println(key + " " + value));
       
    }
}
